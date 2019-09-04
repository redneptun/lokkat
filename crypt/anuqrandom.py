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

import json
import sys
import urllib.request
from datetime import datetime
from enum import Enum
from secrets import token_bytes
import certifi

MAX_LEN = 1024 * 1024  # 1MiB


class Message(Enum):
    ERROR_NO_CONNECTION = 0
    INFO_SUCCESS = 1
    ERROR_TOO_MUCH_DATA = 2


def getRandBytes(amount, result):
    passed_time = None
    rnd = None
    if amount > MAX_LEN:
        message = Message.ERROR_TOO_MUCH_DATA
        passed_time = None
        result['rnd'] = rnd
        result['message'] = message
        result['passed_time'] = passed_time
        return
    else:
        request_size = 1
        while request_size * 1024 < amount:
            request_size += 1

        try:
            start = datetime.now()
            with urllib.request.urlopen(
                    f"https://qrng.anu.edu.au/API/jsonI.php?length=1024&type=hex16&size={request_size}",
                    timeout=60,
                    cafile=certifi.where()) as url:
                data = json.loads(url.read().decode())['data']
                rnd = bytearray()
                for hex_b in data:
                    b = bytes.fromhex(hex_b)
                    int_r = int.from_bytes(b, sys.byteorder)
                    # This should serve as an additional layer of protection if the communication
                    # to the ANU servers or the servers themselves were compromised:
                    added_crypto = token_bytes(1)
                    int_added_crypto = int.from_bytes(added_crypto, sys.byteorder)
                    rnd += (int_r ^ int_added_crypto).to_bytes(len(b), sys.byteorder)

                if len(rnd) < request_size * 1024:
                    raise ValueError('I did not receive enough random data from the ANU.')
                delta = datetime.now() - start
                passed_time = delta.seconds
        except Exception as e:
            print(e)
            message = Message.ERROR_NO_CONNECTION
        else:
            message = Message.INFO_SUCCESS

        result['rnd'] = rnd
        result['message'] = message
        result['passed_time'] = passed_time
        return
