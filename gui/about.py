# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/about.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(771, 376)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(768, 376))
        Dialog.setMaximumSize(QtCore.QSize(2000, 2000))
        Dialog.setModal(True)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lblTitle = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.lblTitle.setFont(font)
        self.lblTitle.setTextFormat(QtCore.Qt.RichText)
        self.lblTitle.setScaledContents(False)
        self.lblTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTitle.setOpenExternalLinks(False)
        self.lblTitle.setObjectName("lblTitle")
        self.verticalLayout_2.addWidget(self.lblTitle)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, 6, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, -1, 6, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnMascot = QtWidgets.QPushButton(Dialog)
        self.btnMascot.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/lokkat_256.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnMascot.setIcon(icon)
        self.btnMascot.setIconSize(QtCore.QSize(256, 256))
        self.btnMascot.setAutoDefault(False)
        self.btnMascot.setFlat(True)
        self.btnMascot.setObjectName("btnMascot")
        self.verticalLayout.addWidget(self.btnMascot)
        self.stackedEggs = QtWidgets.QStackedWidget(Dialog)
        self.stackedEggs.setObjectName("stackedEggs")
        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        self.stackedEggs.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget()
        self.widget_2.setObjectName("widget_2")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 54, 17))
        self.label_2.setObjectName("label_2")
        self.stackedEggs.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget()
        self.widget_3.setObjectName("widget_3")
        self.label_3 = QtWidgets.QLabel(self.widget_3)
        self.label_3.setGeometry(QtCore.QRect(200, 10, 54, 17))
        self.label_3.setObjectName("label_3")
        self.stackedEggs.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget()
        self.widget_4.setObjectName("widget_4")
        self.label_4 = QtWidgets.QLabel(self.widget_4)
        self.label_4.setGeometry(QtCore.QRect(170, 20, 54, 17))
        self.label_4.setObjectName("label_4")
        self.stackedEggs.addWidget(self.widget_4)
        self.widget_5 = QtWidgets.QWidget()
        self.widget_5.setObjectName("widget_5")
        self.label_5 = QtWidgets.QLabel(self.widget_5)
        self.label_5.setGeometry(QtCore.QRect(50, 20, 54, 17))
        self.label_5.setObjectName("label_5")
        self.stackedEggs.addWidget(self.widget_5)
        self.widget_6 = QtWidgets.QWidget()
        self.widget_6.setObjectName("widget_6")
        self.label = QtWidgets.QLabel(self.widget_6)
        self.label.setGeometry(QtCore.QRect(70, 10, 151, 31))
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.stackedEggs.addWidget(self.widget_6)
        self.verticalLayout.addWidget(self.stackedEggs)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.lblAbout = QtWidgets.QLabel(Dialog)
        self.lblAbout.setTextFormat(QtCore.Qt.RichText)
        self.lblAbout.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.lblAbout.setWordWrap(True)
        self.lblAbout.setOpenExternalLinks(True)
        self.lblAbout.setObjectName("lblAbout")
        self.horizontalLayout.addWidget(self.lblAbout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        self.stackedEggs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Über Lokkat"))
        self.lblTitle.setText(_translate("Dialog", "Lokkat v0.5"))
        self.label_2.setText(_translate("Dialog", "nya!"))
        self.label_3.setText(_translate("Dialog", "nya!"))
        self.label_4.setText(_translate("Dialog", "nya!"))
        self.label_5.setText(_translate("Dialog", "nya!"))
        self.label.setText(_translate("Dialog", "...Katzen können sehr verschwiegen sein, nya!"))
        self.lblAbout.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Danke, dass du Lokkat nutzt. Lokkat ist <a href=\"https://de.wikipedia.org/wiki/Freie_Software\"><span style=\" text-decoration: underline; color:#0000ff;\">freie Software</span></a> und unter der <a href=\"https://www.gnu.org/licenses/gpl-3.0.html\"><span style=\" text-decoration: underline; color:#0000ff;\">GNU Public License v3</span></a> lizensiert. </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Das Ziel bei der Entwicklung dieser Anwendung war es, der Öffentlichkeit eine einfach nutzbare, kostenfreie und quelloffene Möglichkeit zu bieten, die starke <a href=\"https://de.wikipedia.org/wiki/One-Time-Pad\"><span style=\" text-decoration: underline; color:#0000ff;\">OTP-Verschlüsselung</span></a> zu nutzen. Ich hoffe, das habe ich erreicht.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Falls du dir den Quellcode anschauen möchtest, findest du ihn hier.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Die Projektwebseite findest du <a href=\"http://redneptun.net/Lokkat\"><span style=\" text-decoration: underline; color:#0000ff;\">hier</span></a>.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Wenn du mir als Dankeschön einen Kaffee oder ein Bier spendieren möchtest, weil dir die Software gefällt und du so etwas unterstützen möchtest, dann klick <a href=\"https://www.paypal.com/signin?returnUri=https://www.paypal.com/myaccount/transfer/send/external/ppme?profile%3Dredneptun%26currencyCode%3DEUR%26amount%3D3.5%26locale.x%3Den-US%26country.x%3DUS%26flowType%3Dsend&amp;onboardData=%7B%22country.x%22%3A%22US%22%2C%22locale.x%22%3A%22en-US%22%2C%22intent%22%3A%22paypalme%22%2C%22redirect_url%22%3A%22https%3A%2F%2Fwww.paypal.com%2Fmyaccount%2Ftransfer%2Fsend%2Fexternal%2Fppme%3Fprofile%253Dredneptun%2526currencyCode%253DEUR%2526amount%253D3.5%2526locale.x%253Den-US%2526country.x%253DUS%2526flowType%253Dsend%22%2C%22sendMoneyText%22%3A%22Philipp%2520B%25C3%25B6ckmann%2520%25E2%2582%25AC3.50%22%7D\"><span style=\" text-decoration: underline; color:#0000ff;\">hier</span></a>.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Wenn du mir etwas Nettes schreiben möchtest, kannst du das <a href=\"mailto:lokkat@redneptun.net\"><span style=\" text-decoration: underline; color:#0000ff;\">hier</span></a> tun.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Lokkat Copyright © 2019 Philipp Böckmann</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Dieses Programm wird OHNE JEGLICHE GEWÄHRLEISTUNG bereitgestellt; Es handelt sich um freie Software und du darfst sie gern unter bestimmten Bedingungen weiterverbreiten. Mehr hierzu findest du in der <a href=\"https://www.gnu.org/licenses/gpl-3.0.en.html\"><span style=\" text-decoration: underline; color:#0000ff;\">Lizenz</span></a>.</p></body></html>"))
from gui import resources_rc
