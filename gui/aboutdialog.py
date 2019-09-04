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

from PyQt5.QtCore import QTranslator
from PyQt5.QtWidgets import QApplication, QDialog

from gui.about import Ui_Dialog
from gui.iconsetter import setIcon


class AboutDialog(QDialog, Ui_Dialog):

    def __init__(self, activeconfig):
        super(AboutDialog, self).__init__()
        self.setupUi(self)
        self.translator = QTranslator()
        self.setLanguage(activeconfig.language)

        setIcon(self)

        self.btnMascot.clicked.connect(self.nya)

    def setLanguage(self, language):
        if not self.translator.isEmpty():
            QApplication.removeTranslator(self.translator)
        self.translator.load(f':/l10n/about_{language.value}.qm')
        QApplication.installTranslator(self.translator)
        self.retranslateUi(self)

    def nya(self):
        i = self.stackedEggs.currentIndex()
        i += 1
        i %= 6
        self.stackedEggs.setCurrentIndex(i)
        if i != 0:
            pass
            # playNya()
