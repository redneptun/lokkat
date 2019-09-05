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

import os
import sys
import threading
import time
import webbrowser

from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QTranslator, QCoreApplication, QDir, QLocale, QLibraryInfo
from PyQt5.QtWidgets import QFileDialog, QApplication, QActionGroup, QMessageBox

from config.config import Language
from crypt import anuqrandom
from crypt import crypt
from crypt.rngsource import RngSource
from gui.aboutdialog import AboutDialog
from gui.gui import Ui_MainWindow
from gui.iconsetter import setIcon
from pathlib import Path

from gui.report_bug_dialog import ReportBugDialog

ENCDEC_SLEEP_TIME = 0.2


def tr(string):
    return QtCore.QCoreApplication.translate("MainWindow", string)


def clearList(listWidget):
    for i in range(listWidget.count())[::-1]:
        listWidget.takeItem(i)


def getPathsFromList(listWidget):
    items = []
    for index in range(listWidget.count()):
        items.append(listWidget.item(index))
    paths = [i.text() for i in items]
    return paths


def closeApp():
    sys.exit()


def openProjectWebsite():
    # todo insert proper project page address
    url = 'http://redneptun.net/lokkat'
    webbrowser.open(url, new=2)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, activeConfig, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # pure UI

        self.setupUi(self)

        setIcon(self)

        self.setupLanguageActions()

        # set the language of the UI by looking it up in the config
        self.activeConfig = activeConfig
        self.translator = QTranslator()

        self.file_dialog_translator = QTranslator()

        self.setLanguage(self.activeConfig.language)

        # setup initial values
        self.rngSource = RngSource.CSPRNG
        self.busy = False
        self.encProgress = 0
        self.decProgress = 0
        self.encText = ''
        self.decText = ''

        self.slotActionsIn()

    def slotActionsIn(self):
        # from here on: slotting
        # MENU
        self.actionClose.triggered.connect(closeApp)
        self.actionOpenHelpFile.triggered.connect(self.openHelpFile)
        self.actionOpenOnlineHelp.triggered.connect(openProjectWebsite)
        self.actionAbout.triggered.connect(self.about)
        self.actionGerman.triggered.connect(self.setLanguageGerman)
        self.actionEnglish.triggered.connect(self.setLanguageEnglish)
        self.actionReportBug.triggered.connect(self.reportBug)
        # ENCRYPTION
        self.btnAddInputFilesEnc.clicked.connect(self.addInputFilesEnc)
        self.btnRemoveInputFilesEnc.clicked.connect(self.removeInputFilesEnc)
        self.rbANU.clicked.connect(self.rngSourceChanged)
        self.rbCSPRNG.clicked.connect(self.rngSourceChanged)
        self.btnEncrypt.clicked.connect(self.startEncryption)
        # DECRYPTION
        self.btnAddInputFilesDec.clicked.connect(self.addInputFilesDec)
        self.btnRemoveInputFilesDec.clicked.connect(self.removeInputFilesDec)
        self.btnDecrypt.clicked.connect(self.startDecryption)

    def slotActionsOut(self):
        # from here on: slotting
        # MENU
        self.actionClose.triggered.disconnect(closeApp)
        self.actionOpenHelpFile.triggered.disconnect(self.openHelpFile)
        self.actionOpenOnlineHelp.triggered.disconnect(openProjectWebsite)
        self.actionAbout.triggered.disconnect(self.about)
        self.actionGerman.triggered.disconnect(self.setLanguageGerman)
        self.actionEnglish.triggered.disconnect(self.setLanguageEnglish)
        self.actionReportBug.triggered.disconnect(self.reportBug)
        # ENCRYPTION
        self.btnAddInputFilesEnc.clicked.disconnect(self.addInputFilesEnc)
        self.btnRemoveInputFilesEnc.clicked.disconnect(self.removeInputFilesEnc)
        self.rbANU.clicked.disconnect(self.rngSourceChanged)
        self.rbCSPRNG.clicked.disconnect(self.rngSourceChanged)
        self.btnEncrypt.clicked.disconnect(self.startEncryption)
        # DECRYPTION
        self.btnAddInputFilesDec.clicked.disconnect(self.addInputFilesDec)
        self.btnRemoveInputFilesDec.clicked.disconnect(self.removeInputFilesDec)
        self.btnDecrypt.clicked.disconnect(self.startDecryption)

    def setupLanguageActions(self):
        languageActionGroup = QActionGroup(self)
        languageActionGroup.addAction(self.actionEnglish)
        languageActionGroup.addAction(self.actionGerman)
        languageActionGroup.setExclusive(True)

    def openHelpFile(self):
        path = Path().absolute()
        url = f'file://{path}/help/user_manual_{self.activeConfig.language.value}.html'
        webbrowser.open(url, new=2)

    def setLanguageGerman(self):
        self.setLanguage(Language.GERMAN)

    def setLanguageEnglish(self):
        self.setLanguage(Language.ENGLISH)

    def setLanguage(self, language):
        # file dialog
        if not self.file_dialog_translator.isEmpty():
            QApplication.removeTranslator(self.file_dialog_translator)

        qmfile = "qtbase_" + QLocale.system().name().split('_')[0] + '.qm'
        self.file_dialog_translator.load(qmfile,
                                         QLibraryInfo.location(QLibraryInfo.TranslationsPath))
        # todo: remove
        print(qmfile + '  location: ' + QLibraryInfo.location(QLibraryInfo.TranslationsPath))
        QApplication.installTranslator(self.file_dialog_translator)

        # rest of app
        if language == Language.ENGLISH:
            self.actionEnglish.setChecked(True)

        elif language == Language.GERMAN:
            self.actionGerman.setChecked(True)

        else:
            # Fall back to english
            self.actionEnglish.setChecked(True)
            language = Language.ENGLISH

        self.activeConfig.language = language
        self.activeConfig.saveConfig()
        if not self.translator.isEmpty():
            QApplication.removeTranslator(self.translator)
        self.translator.load(f':/l10n/gui_{self.activeConfig.language.value}.qm')
        QApplication.installTranslator(self.translator)
        self.retranslateUi(self)
        self.resetEncText()
        self.resetDecText()

    def about(self):
        diag = AboutDialog(activeconfig=self.activeConfig)
        diag.exec()

    def reportBug(self):
        diag = ReportBugDialog(activeconfig=self.activeConfig)
        diag.exec()

    def addEncText(self, text):
        if text is not None and len(text) > 0:
            # if len(self.encText) > 0:
            #     self.encText += os.linesep
            # self.encText += text

            self.encText += '<p>'
            self.encText += text
            self.encText += '</p>'
            self.txtEncryptionResult.setText(self.encText)

    def resetEncText(self):
        self.encText = ''
        self.txtEncryptionResult.setText(self.encText)

    def addDecText(self, text):
        if text is not None and len(text) > 0:
            # if len(self.decText) > 0:
            #     self.decText += os.linesep
            # self.decText += text
            self.decText += '<p>'
            self.decText += text
            self.decText += '</p>'
            self.txtDecryptionResult.setText(self.decText)

    def resetDecText(self):
        self.decText = ''
        self.txtDecryptionResult.setText(self.decText)

    def setEncProgress(self, progress):
        self.encProgress = progress

    def setDecProgress(self, progress):
        self.decProgress = progress

    def updateProgressEnc(self):
        while 1:
            self.prgEnc.setValue(self.encProgress)
            time.sleep(0.1)
            if self.encProgress >= 100:
                time.sleep(3)
                break

    def updateProgressDec(self):
        while 1:
            self.prgDec.setValue(self.decProgress)
            time.sleep(0.1)
            if self.decProgress >= 100:
                time.sleep(3)
                break

    def addInputFilesEnc(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self,
                                                tr(self.trWhichFilesEnc.text()), QDir.homePath(),
                                                tr(self.trWhichFilesEncFileTypes.text()),
                                                options=options)
        for path in files:
            if len(self.lsInputFilesEnc.findItems(path, Qt.MatchExactly)) == 0:
                self.lsInputFilesEnc.addItem(path)

        if len(files) > 0:
            self.resetEncText()

    def addInputFilesDec(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self,
                                                tr(self.trWhichFilesDec.text()), QDir.homePath(),
                                                tr(self.trWhichFilesDecFileTypes.text()),
                                                options=options)
        for path in files:
            if len(self.lsInputFilesDec.findItems(path, Qt.MatchExactly)) == 0:
                self.lsInputFilesDec.addItem(path)

        if len(files) > 0:
            self.resetDecText()

    def removeInputFilesEnc(self):
        for item in self.lsInputFilesEnc.selectedItems():
            self.lsInputFilesEnc.takeItem(self.lsInputFilesEnc.row(item))
        if len(self.lsInputFilesEnc.selectedItems()) > 0:
            self.resetEncText()

    def removeInputFilesDec(self):
        for item in self.lsInputFilesDec.selectedItems():
            self.lsInputFilesDec.takeItem(self.lsInputFilesDec.row(item))
        if len(self.lsInputFilesDec.selectedItems()) > 0:
            self.resetDecText()

    def rngSourceChanged(self):
        if self.rbANU.isChecked():
            self.rngSource = RngSource.ANU
        elif self.rbCSPRNG.isChecked():
            self.rngSource = RngSource.CSPRNG
        else:
            self.rngSource = RngSource.CSPRNG

    def switchEncMode(self, busy=False, resetFiles=False):
        if self.busy != busy:
            self.setEncProgress(0)
            self.stackEnc.setCurrentIndex(1 if busy else 0)
            if not self.busy:
                self.resetEncText()
                self.setCursor(Qt.WaitCursor)
                self.slotActionsOut()
            else:
                if resetFiles:
                    clearList(self.lsInputFilesEnc)
                self.setCursor(Qt.ArrowCursor)
                self.slotActionsIn()
            self.busy = busy
            self.enableUserInput(not busy)

    def switchDecMode(self, busy=False, resetFiles=False):
        if self.busy != busy:
            self.setDecProgress(0)
            self.stackDec.setCurrentIndex(1 if busy else 0)
            if not self.busy:
                self.resetDecText()
                self.setCursor(Qt.WaitCursor)
                self.slotActionsOut()
            else:
                if resetFiles:
                    clearList(self.lsInputFilesDec)
                self.setCursor(Qt.ArrowCursor)
                self.slotActionsIn()

            self.busy = busy
            self.enableUserInput(not busy)

    def enableUserInput(self, enable):

        # FILE ACTIONS
        self.actionClose.setEnabled(enable)

        # LANGUAGES
        self.actionGerman.setEnabled(enable)
        self.actionEnglish.setEnabled(enable)

        # HELP ACTIONS
        self.actionOpenHelpFile.setEnabled(enable)
        self.actionOpenOnlineHelp.setEnabled(enable)
        self.actionAbout.setEnabled(enable)

        # ENCRYPT
        self.btnEncrypt.setEnabled(enable)
        self.btnAddInputFilesEnc.setEnabled(enable)
        self.btnRemoveInputFilesEnc.setEnabled(enable)
        self.rbANU.setEnabled(enable)
        self.rbCSPRNG.setEnabled(enable)

        # DECRYPT
        self.btnDecrypt.setEnabled(enable)
        self.btnAddInputFilesDec.setEnabled(enable)
        self.btnRemoveInputFilesDec.setEnabled(enable)

    def startEncryption(self):
        self.switchEncMode(busy=True)
        progressUpdateThread = threading.Thread(None, self.updateProgressEnc, None)
        progressUpdateThread.start()

        # getPaths
        plainPaths = getPathsFromList(self.lsInputFilesEnc)
        if len(plainPaths) == 0:
            self.addEncText(tr(self.trErrorNoEncFiles.text()))
            self.switchEncMode(busy=False)
            return

        self.addEncText(tr(self.trInfoLetsGo.text()))
        # get random bytes
        rndBytes = None
        if self.rngSource == RngSource.ANU:
            self.addEncText(tr(self.trRetrievingANUData.text()))
            total = sum(os.path.getsize(p) for p in plainPaths)
            if total > anuqrandom.MAX_LEN:
                self.addEncText(tr(self.trErrorTooBigForANU.text()))
                self.switchEncMode(busy=False, resetFiles=False)
                return
            anuResult = {'rnd': None, 'message': None}
            anuThread = threading.Thread(None, anuqrandom.getRandBytes, None, (total, anuResult))
            anuThread.start()
            anustep = 0.5
            anumax = 10
            while anuThread.isAlive():
                if self.encProgress <= anumax:
                    self.setEncProgress(self.encProgress + anustep)
                time.sleep(1)
                QCoreApplication.processEvents()
            anuMessage = anuResult['message']
            if anuMessage == anuqrandom.Message.INFO_SUCCESS:
                passed_time = anuResult['passed_time']
                output = tr(self.trInfoANUSuccess.text()).format(passed_time)
            elif anuMessage == anuqrandom.Message.ERROR_TOO_MUCH_DATA:
                output = tr(self.trErrorANUTooMuchData.text())
            elif anuMessage == anuqrandom.Message.ERROR_NO_CONNECTION:
                output = tr(self.trErrorANUNoConnection.text())
            else:
                output = tr(self.trErrorANUUnknown.text())
            self.addEncText(output)
            if anuResult['rnd'] is None:
                self.switchEncMode(busy=False)
                return
            else:
                rndBytes = anuResult['rnd']
        self.setEncProgress(10)

        # encrypt files
        encThread = threading.Thread(None, crypt.encryptPathsWithProgress, None, (plainPaths, self.setEncProgress,
                                                                                  rndBytes, 90, 10))
        self.addEncText(tr(self.trInfoStartingEnc.text()))
        encThread.start()

        while encThread.is_alive():
            time.sleep(ENCDEC_SLEEP_TIME)
            QCoreApplication.processEvents()

        self.setEncProgress(100)
        time.sleep(1)

        self.addEncText(tr(self.trSuccessEnc.text()))
        self.addEncText(tr(self.trInfoAfterSuccess.text()))

        self.switchEncMode(busy=False, resetFiles=True)

    def startDecryption(self):
        self.switchDecMode(busy=True)
        progressUpdateThread = threading.Thread(None, self.updateProgressDec, None)
        progressUpdateThread.start()

        # get crypt paths
        cryptPaths = getPathsFromList(self.lsInputFilesDec)
        if len(cryptPaths) == 0:
            self.addDecText(tr(self.trErrorNoDecFiles.text()))
            self.switchDecMode(busy=False)
            return

        # get OTPs
        otpPaths = ['.'.join(p.split('.')[:-1]) + '.otp' for p in cryptPaths]
        missingOTPs = []
        for p in otpPaths:
            if not os.path.exists(p):
                missingOTPs.append(p)

        if len(missingOTPs) > 0:
            self.addDecText(tr(self.trErrorEncMissingKeys.text()))
            for p in missingOTPs:
                self.addDecText(p)

            self.addDecText(tr(self.trInfoDecryptExample.text()))
            self.switchDecMode(busy=False)
            return

        self.addDecText(tr(self.trInfoLetsGo.text()))

        # decrypt files
        decThread = threading.Thread(None, crypt.decryptPathsWithProgress, None,
                                     (cryptPaths, otpPaths, self.setDecProgress,
                                      100, 0))
        self.addDecText(tr(self.trStartingDec.text()))
        decThread.start()

        while decThread.is_alive():
            time.sleep(ENCDEC_SLEEP_TIME)
            QCoreApplication.processEvents()

        self.setDecProgress(100)
        time.sleep(1)

        self.addDecText(tr(self.trSuccessDec.text()))
        self.switchDecMode(busy=False, resetFiles=True)
