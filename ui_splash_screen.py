# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash_screenBwVRkK.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if not SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(680, 400)
        SplashScreen.setWindowOpacity(1.000000000000000)
        SplashScreen.setStyleSheet(u"")
        self.mainLayout = QWidget(SplashScreen)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.mainLayout)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.mainFrame = QFrame(self.mainLayout)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(123, 189, 173);\n"
"	border-radius: 10px\n"
"}")
        self.mainFrame.setFrameShape(QFrame.NoFrame)
        self.mainFrame.setFrameShadow(QFrame.Plain)
        self.mainLabel = QLabel(self.mainFrame)
        self.mainLabel.setObjectName(u"mainLabel")
        self.mainLabel.setGeometry(QRect(0, 90, 661, 81))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.mainLabel.setFont(font)
        self.mainLabel.setStyleSheet(u"QLabel {\n"
"	color: rgb(86, 100, 83);\n"
"}")
        self.mainLabel.setAlignment(Qt.AlignCenter)
        self.progressBar = QProgressBar(self.mainFrame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(40, 240, 571, 23))
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"	background-color: rgb(57, 115, 85);\n"
"	color: rgb(200, 200, 200);\n"
"	border-style: none;\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.477, x2:1, y2:0.483, stop:0 rgba(84, 176, 115, 255), stop:1 rgba(57, 145, 125, 100));\n"
"	border-radius: 10px\n"
"}")
        self.progressBar.setValue(24)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)
        self.loadingLabel = QLabel(self.mainFrame)
        self.loadingLabel.setObjectName(u"loadingLabel")
        self.loadingLabel.setGeometry(QRect(210, 270, 231, 21))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setWeight(50)
        self.loadingLabel.setFont(font1)
        self.loadingLabel.setStyleSheet(u"QLabel {\n"
"	color: rgb(86, 100, 83);\n"
"}")
        self.loadingLabel.setAlignment(Qt.AlignCenter)
        self.createdLabel = QLabel(self.mainFrame)
        self.createdLabel.setObjectName(u"createdLabel")
        self.createdLabel.setGeometry(QRect(20, 370, 651, 21))
        self.createdLabel.setFont(font1)
        self.createdLabel.setStyleSheet(u"QLabel {\n"
"	color: rgb(86, 100, 83);\n"
"}")
        self.createdLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.mainFrame)

        SplashScreen.setCentralWidget(self.mainLayout)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"MainWindow", None))
        self.mainLabel.setText(QCoreApplication.translate("SplashScreen", u"<strong>Password</strong> Manager", None))
        self.loadingLabel.setText(QCoreApplication.translate("SplashScreen", u"Loading...", None))
        self.createdLabel.setText(QCoreApplication.translate("SplashScreen", u"<strong>Created by</strong> Ayaz Ahmadov", None))
    # retranslateUi

