# Lokkat is an encryption software to make One-Time Pad encryption available to the public
# Copyright (C) 2019 Philipp Böckmann
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from secrets import token_bytes
from datetime import datetime
import os
import sys
import concurrent.futures
import threading
import time
from typing import Callable, ByteString, List
import platform

MAX_PART_SIZE = 32 * 1024 * 1024  # 32MiB
MAX_SUBPART_SIZE = 16 * 1024  # 16KiB
SLEEP_TIME = 0.2  # 100ms
curr_OS = None


def shit_am_I_on_Windows():
    global curr_OS
    if curr_OS is None:
        curr_OS = get_OS()
    return curr_OS == 'Windows'


def get_OS():
    return platform.system()


def encryptPathsWithProgress(plainPaths: List[str], progressReporter: Callable[[float], None],
                             randomBytesExt: ByteString = None,
                             progressMod: int = 100, progressOffset: int = 0):
    cryptPathsWithProgress(plainPaths, None, encryptPaths, watchEncryptionProgress, True, progressReporter,
                           randomBytesExt, progressMod, progressOffset)


def decryptPathsWithProgress(cryptPaths: List[str], otpPaths: List[str], progressReporter: Callable[[], None],
                             progressMod: int = 100, progressOffset: int = 0):
    cryptPathsWithProgress(cryptPaths, otpPaths, decryptPaths, watchDecryptionProgress, False, progressReporter, None,
                           progressMod, progressOffset)


def cryptPathsWithProgress(paths: List[str], otpPaths: List[str], cryptFunc: Callable, watcherFunc: Callable,
                           isEncryption: bool,
                           progressReporter: Callable[[], None],
                           randomBytesExt: ByteString, progressMod: int = 100, progressOffset: int = 0):
    if isEncryption:
        cThread = threading.Thread(None, cryptFunc, None, (paths, randomBytesExt,))
    else:
        cThread = threading.Thread(None, cryptFunc, None, (paths, otpPaths,))
    watcherThread = threading.Thread(None, watcherFunc, None,
                                     (paths, progressReporter, progressMod, progressOffset))
    watcherThread.start()
    cThread.start()

    while cThread.is_alive():
        time.sleep(SLEEP_TIME)

    while watcherThread.is_alive():
        time.sleep(SLEEP_TIME)


def watchEncryptionProgress(paths: str, progressReporter: Callable[[float], None], progressMod: int = 100,
                            progressOffset: int = 0):
    sizes = [os.path.getsize(p) for p in paths]
    totalSize = sum(s for s in sizes)
    pathSizes = dict(zip(paths, sizes))

    while 1:
        progressSum = 0
        for p in paths:
            size = pathSizes[p]
            # print(size)
            partCount = int(size / MAX_PART_SIZE) + 1
            stitching = False

            if size <= MAX_PART_SIZE:
                # single file
                try:
                    progressSum += os.path.getsize(f'{p}.crypt')
                except:
                    pass
            else:
                # split file
                if os.path.exists(f'{p}.crypt'):
                    # already stitching/stitched
                    try:
                        progressSum += os.path.getsize(f'{p}.crypt') / 2
                    except:
                        pass
                    stitching = True
                else:
                    for i in range(partCount):
                        # still crypting
                        try:
                            progressSum += os.path.getsize(f'{p}.{i}.crypt') / 2
                        except:
                            pass
            if stitching:
                progressSum += size / 2

        progressReporter(progressSum / totalSize * progressMod + progressOffset)
        time.sleep(SLEEP_TIME)
        if progressSum >= totalSize:
            break


def watchDecryptionProgress(cryptPaths: str, progressReporter: Callable[[float], None], progressMod: int = 100,
                            progressOffset: int = 0):
    plainPaths = ['.'.join(p.split('.')[:-1]) for p in cryptPaths]
    sizes = [os.path.getsize(p) for p in cryptPaths]
    totalSize = sum(s for s in sizes)
    pathSizes = dict(zip(plainPaths, sizes))

    while 1:
        progressSum = 0
        for p in plainPaths:
            size = pathSizes[p]
            # print(size)
            partcount = int(size / MAX_PART_SIZE) + 1
            stitching = False

            if size <= MAX_PART_SIZE:
                # single file
                try:
                    progressSum += os.path.getsize(f'{p}')
                except FileNotFoundError:
                    # aw well nvm
                    pass
            else:
                # split file
                if os.path.exists(p):
                    # already stitching/stitched
                    try:
                        progressSum += os.path.getsize(p) / 2
                    except FileNotFoundError:
                        # aw well nvm
                        pass
                    stitching = True
                else:
                    for i in range(partcount):
                        # still crypting
                        try:
                            progressSum += os.path.getsize(f'{p}.{i}.part') / 2
                        except FileNotFoundError:
                            # aw well nvm
                            pass
            if stitching:
                progressSum += size / 2

        progressReporter(progressSum / totalSize * progressMod + progressOffset)
        time.sleep(SLEEP_TIME)
        if progressSum >= totalSize:
            break


def encryptPaths(paths: str, randomBytesExt: ByteString = None):
    toStitch = []
    pathSizes = zip(paths, [os.path.getsize(p) for p in paths])
    executor = getExecutor()

    doneBytes = 0
    for (path, size) in pathSizes:
        partBytes = None if randomBytesExt is None else randomBytesExt[doneBytes:doneBytes + size]
        if size > MAX_PART_SIZE:
            partCount = int(size / MAX_PART_SIZE) + 1
            lsFutures = []
            for i in range(partCount):
                lsFutures.append(executor.submit(encryptPart, path, i, partBytes))
            toStitch.append((path, partCount, lsFutures))
        else:
            # do it in a single process
            executor.submit(encryptPart, path, None, partBytes)
        doneBytes += size
    executor.shutdown()

    executor = getExecutor()

    for path, partCount, lsFutures in toStitch:
        executor.submit(stitchEncryptionParts, path, partCount)
    executor.shutdown()

    for p in paths:
        os.remove(p)


def encryptPart(plainPath: str, partNo: int = None, randomBytesExt: ByteString = None):
    if partNo is None:
        start_pos_plain = 0
        otp_path = f'{plainPath}.otp'
        crypt_path = f'{plainPath}.crypt'
    else:
        start_pos_plain = partNo * MAX_PART_SIZE
        otp_path = f'{plainPath}.{partNo}.otp'
        crypt_path = f'{plainPath}.{partNo}.crypt'

    with open(plainPath, 'rb') as fPlain, \
            open(otp_path, 'wb') as fOtp, \
            open(crypt_path, 'wb') as fCrypt:

        if partNo is not None:
            fPlain.seek(start_pos_plain)

        plainBytes = fPlain.read(MAX_SUBPART_SIZE)
        done = 0
        while done < MAX_PART_SIZE and plainBytes:
            readCount = len(plainBytes)
            if randomBytesExt is None:
                subKeyPart = token_bytes(readCount)
            else:
                if partNo is None:
                    s = 0 + done
                else:
                    s = partNo * MAX_PART_SIZE + done
                e = s + MAX_SUBPART_SIZE
                subKeyPart = randomBytesExt[s:e]
            int_plain = int.from_bytes(plainBytes, sys.byteorder)
            int_keypart = int.from_bytes(subKeyPart, sys.byteorder)
            int_crypt = int_plain ^ int_keypart
            cryptBytes = int_crypt.to_bytes(len(plainBytes), sys.byteorder)

            fOtp.write(subKeyPart)
            fCrypt.write(cryptBytes)
            done += readCount
            plainBytes = fPlain.read(MAX_SUBPART_SIZE)


def decryptPaths(cryptPaths: List[str], otpPaths: List[str]):
    if len(cryptPaths) != len(otpPaths):
        raise Exception()
    # otpPaths = ['.'.join(cryptPath.split('.')[:-1] + 'otp') for cryptPath in cryptpaths]
    cryptSizes = [os.path.getsize(p) for p in cryptPaths]
    otpSizes = [os.path.getsize(p) for p in otpPaths]
    for cryptSize, otpSize in zip(cryptSizes, otpSizes):
        if cryptSize != otpSize:
            print(f'cryptsize = {cryptSize}, otpsize = {otpSize}')
            raise Exception()
    pathPairSizes = zip(cryptPaths, otpPaths, cryptSizes)
    toStitch = []
    toDecrypt = [p for p in pathPairSizes]

    executor = getExecutor()
    for cryptPath, otpPath, size in toDecrypt:
        if size > MAX_PART_SIZE:
            partCount = int(size / MAX_PART_SIZE) + 1
            lsFutures = []
            for i in range(partCount):
                lsFutures.append(executor.submit(decryptPart, cryptPath, otpPath, i))
            plainPath = '.'.join(cryptPath.split('.')[:-1])
            toStitch.append((plainPath, partCount, lsFutures))
        else:
            # do it in a single process
            executor.submit(decryptPart, cryptPath, otpPath, None)
    executor.shutdown()

    executor = getExecutor()
    for plainPath, partCount, lsFutures in toStitch:
        executor.submit(stitchDecryptionParts, plainPath, partCount)
    executor.shutdown()

    for p in cryptPaths:
        os.remove(p)
    for p in otpPaths:
        os.remove(p)


def decryptPart(cryptPath: str, otpPath: str, partNo: int = None):
    if partNo is None:
        startPos = 0
        plainPath = '.'.join(cryptPath.split('.')[:-1])
    else:
        startPos = partNo * MAX_PART_SIZE
        plainPath = '.'.join(cryptPath.split('.')[:-1]) + f'.{partNo}.part'

    with open(plainPath, 'wb') as fPlain, \
            open(otpPath, 'rb') as fOtp, \
            open(cryptPath, 'rb') as fCrypt:

        if partNo is not None:
            fOtp.seek(startPos)
            fCrypt.seek(startPos)

        otpBytes = fOtp.read(MAX_SUBPART_SIZE)
        cryptBytes = fCrypt.read(MAX_SUBPART_SIZE)
        i = 0
        while i < MAX_PART_SIZE and otpBytes and cryptBytes:
            if len(otpBytes) == len(otpBytes):
                readCount = len(otpBytes)
            else:
                raise Exception()
            int_crypt = int.from_bytes(cryptBytes, sys.byteorder)
            int_otp = int.from_bytes(otpBytes, sys.byteorder)
            int_plain = int_crypt ^ int_otp
            plainBytes = int_plain.to_bytes(len(cryptBytes), sys.byteorder)

            fPlain.write(plainBytes)
            i += readCount
            otpBytes = fOtp.read(MAX_SUBPART_SIZE)
            cryptBytes = fCrypt.read(MAX_SUBPART_SIZE)


def getExecutor():
    if shit_am_I_on_Windows():
        executor = concurrent.futures.ThreadPoolExecutor()
    else:
        executor = concurrent.futures.ProcessPoolExecutor()
    return executor


def stitchEncryptionParts(path: str, partCount: int = None):
    types = ('otp', 'crypt')
    for t in types:
        targetPath = path + f'.{t}'

        with open(f'{targetPath}', 'wb') as targetFile:
            for i in range(partCount):
                partPath = f'{path}.{i}.{t}'
                with open(partPath, 'rb') as partFile:
                    targetFile.write(partFile.read())
                os.remove(partPath)


def stitchDecryptionParts(targetPath: str, partCount: int = None):
    t = 'part'
    with open(f'{targetPath}', 'wb') as targetFile:
        for i in range(partCount):
            partPath = f'{targetPath}.{i}.{t}'
            with open(partPath, 'rb') as partFile:
                targetFile.write(partFile.read())
            os.remove(partPath)


if __name__ == '__main__':
    start = datetime.now()
    # TEST_PLAIN_PATHS = ['../testfiles/test1.file']  # , '../testfiles/test2.file', '../testfiles/test3.file']
    # # encryptPathsWithProgress(TEST_PLAIN_PATHS)
    # encryptPathsWithProgress(TEST_PLAIN_PATHS)
    # elapsed = datetime.now() - start
    # print(elapsed)

    TEST_CRYPT_PATHS = [
        '../testfiles/test1.file.crypt', '../testfiles/test2.file.crypt', '../testfiles/test3.file.crypt']
    TEST_OTP_PATHS = ['../testfiles/test1.file.otp', '../testfiles/test2.file.otp', '../testfiles/test3.file.otp']

    # decryptPathsWithProgress(TEST_CRYPT_PATHS, TEST_OTP_PATHS, showProgress, 100)
    # decryptPaths(TEST_CRYPT_PATHS, TEST_OTP_PATHS)
    elapsed = datetime.now() - start
    print(elapsed)
