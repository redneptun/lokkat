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
import os

import certifi
from PyQt5 import QtCore
from PyQt5.QtCore import QTranslator, QCoreApplication, Qt
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox

from gui.report_bug import Ui_report_bug
import requests
import re


def tr(string):
    return QtCore.QCoreApplication.translate("ReportBugDialog", string)


class ReportBugDialog(QDialog, Ui_report_bug):

    def __init__(self, activeconfig):
        super(ReportBugDialog, self).__init__()
        self.setupUi(self)
        self.translator = QTranslator()
        self.setLanguage(activeconfig.language)

        self.btnSend.clicked.connect(self.send)

    def setLanguage(self, language):
        if not self.translator.isEmpty():
            QApplication.removeTranslator(self.translator)
        self.translator.load(f':/l10n/report_bug_{language.value}.qm')
        QApplication.installTranslator(self.translator)
        self.retranslateUi(self)

    def send(self):
        self.setCursor(Qt.WaitCursor)
        self.btnSend.setEnabled(False)
        QCoreApplication.processEvents()
        name = self.txtName.text()
        mail = self.txtMail.text()
        if mail is not None and len(mail.strip()) > 0:
            if not re.match(
                    r"^[-!#$%&'*+/0-9=?A-Z^_a-z{|}~](\.?[-!#$%&'*+/0-9=?A-Z^_a-z{|}~])*@[a-zA-Z](-?[a-zA-Z0-9])*(\.[a-zA-Z](-?[a-zA-Z0-9])*)+$",
                    mail):
                QMessageBox.information(self, tr(self.trError.text()), tr(self.trInvalidMail.text()))
                self.reset()
                return
        title = self.txtTitle.text()
        if title is None or len(title.strip()) == 0:
            QMessageBox.information(self, tr(self.trError.text()), tr(self.trInvalidTitle.text()))
            self.reset()
            return
        description = self.txtDescription.toPlainText()
        if description is None or len(description.strip()) == 0:
            QMessageBox.information(self, tr(self.trError.text()), tr(self.trInvalidDescription.text()))
            self.reset()
            return

        body = ''
        if len(name) > 0:
            body += f'*Reported by*: {name}' + os.linesep
        if len(mail) > 0:
            mail = mail.replace('@', ' [aŧ] ').replace('.', ' [doŧ] ')
            body += f'*Mail*: {mail}' + os.linesep
        if len(body) > 0:
            body += '___\n'

        body += description
        headers = {'Authorization': 'token 1edffb1271f4ac0bb48c67d0ac5b1e7cbc1dacdd'}
        url = 'https://api.github.com/repos/redneptun/lokkat/issues'
        data = {"title": title, "body": body}
        response = requests.post(url, data=json.dumps(data), headers=headers, verify=certifi.where())
        if response.status_code != 201:
            QMessageBox.information(self, tr(self.trError.text()), tr(self.trFailureText.text()))
            self.reset()
            return
        else:
            self.reset()
            link = response.json()['html_url']
            mb = QMessageBox()
            mb.setWindowTitle(tr(self.trSuccess.text()))
            mb.setTextFormat(Qt.RichText)
            link = f'<br><a href="{link}">{link}</a>'
            mb.setText(tr(self.trSuccessLink.text()).format(link))
            mb.setStandardButtons(QMessageBox.Ok);
            mb.exec()
            self.close()

    def reset(self):
        self.setCursor(Qt.ArrowCursor)
        self.btnSend.setEnabled(True)
        QCoreApplication.processEvents()
