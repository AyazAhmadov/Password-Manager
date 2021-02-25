# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowuZiWxc.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1282, 720)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.sideMenuFrame = QFrame(self.centralwidget)
        self.sideMenuFrame.setObjectName(u"sideMenuFrame")
        self.sideMenuFrame.setMinimumSize(QSize(70, 0))
        self.sideMenuFrame.setMaximumSize(QSize(70, 16777215))
        self.sideMenuFrame.setStyleSheet(u"background-color:rgb(33, 100, 69);")
        self.sideMenuFrame.setFrameShape(QFrame.NoFrame)
        self.sideMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.sideMenuFrame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleFrame = QFrame(self.sideMenuFrame)
        self.toggleFrame.setObjectName(u"toggleFrame")
        self.toggleFrame.setMaximumSize(QSize(16777215, 40))
        self.toggleFrame.setStyleSheet(u"background-color:rgb(33, 100, 69);")
        self.toggleFrame.setFrameShape(QFrame.NoFrame)
        self.toggleFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.toggleFrame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.toggleBtn = QPushButton(self.toggleFrame)
        self.toggleBtn.setObjectName(u"toggleBtn")
        self.toggleBtn.setMinimumSize(QSize(0, 40))
        self.toggleBtn.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"	color: rgb(231, 255, 231);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(43, 144, 122);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(86, 172, 155);\n"
"}")
        self.toggleBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_2.addWidget(self.toggleBtn)


        self.verticalLayout.addWidget(self.toggleFrame)

        self.menuFrame = QFrame(self.sideMenuFrame)
        self.menuFrame.setObjectName(u"menuFrame")
        self.menuFrame.setStyleSheet(u"background-color:rgb(33, 100, 69);")
        self.menuFrame.setFrameShape(QFrame.NoFrame)
        self.menuFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.menuFrame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.menuFrame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.newBtn = QPushButton(self.frame)
        self.newBtn.setObjectName(u"newBtn")
        self.newBtn.setMinimumSize(QSize(0, 70))
        self.newBtn.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"	color: rgb(231, 255, 231);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(43, 144, 122);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(86, 172, 155);\n"
"}")
        self.newBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.newBtn)

        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 70))
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"	color: rgb(231, 255, 231);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(43, 144, 122);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(86, 172, 155);\n"
"}")
        self.pushButton_3.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.pushButton_3)


        self.verticalLayout_3.addWidget(self.frame, 0, Qt.AlignTop)


        self.verticalLayout.addWidget(self.menuFrame)


        self.horizontalLayout.addWidget(self.sideMenuFrame)

        self.mainFrame = QFrame(self.centralwidget)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setStyleSheet(u"background-color: rgb(123, 189, 173);")
        self.mainFrame.setFrameShape(QFrame.NoFrame)
        self.mainFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.mainFrame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.topFrame = QFrame(self.mainFrame)
        self.topFrame.setObjectName(u"topFrame")
        self.topFrame.setMaximumSize(QSize(16777215, 40))
        self.topFrame.setStyleSheet(u"background-color: rgb(71, 129, 108);")
        self.topFrame.setFrameShape(QFrame.NoFrame)
        self.topFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.topFrame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.container = QFrame(self.topFrame)
        self.container.setObjectName(u"container")
        self.container.setMinimumSize(QSize(0, 40))
        self.container.setFrameShape(QFrame.NoFrame)
        self.container.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.container)

        self.windowFrame = QFrame(self.topFrame)
        self.windowFrame.setObjectName(u"windowFrame")
        self.windowFrame.setMinimumSize(QSize(0, 30))
        self.windowFrame.setMaximumSize(QSize(120, 30))
        self.windowFrame.setStyleSheet(u"")
        self.windowFrame.setFrameShape(QFrame.NoFrame)
        self.windowFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.windowFrame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.windowBtns = QFrame(self.windowFrame)
        self.windowBtns.setObjectName(u"windowBtns")
        self.windowBtns.setMaximumSize(QSize(16777215, 30))
        self.windowBtns.setStyleSheet(u"background-color:rgb(33, 100, 69);")
        self.windowBtns.setFrameShape(QFrame.NoFrame)
        self.windowBtns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.windowBtns)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.minimizeBtn = QPushButton(self.windowBtns)
        self.minimizeBtn.setObjectName(u"minimizeBtn")
        self.minimizeBtn.setMinimumSize(QSize(0, 30))
        self.minimizeBtn.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"	color: rgb(231, 255, 231);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(43, 144, 122);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(86, 172, 155);\n"
"}")

        self.horizontalLayout_3.addWidget(self.minimizeBtn)

        self.maximizeBtn = QPushButton(self.windowBtns)
        self.maximizeBtn.setObjectName(u"maximizeBtn")
        self.maximizeBtn.setMinimumSize(QSize(0, 30))
        self.maximizeBtn.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"	color: rgb(231, 255, 231);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(43, 144, 122);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(86, 172, 155);\n"
"}")

        self.horizontalLayout_3.addWidget(self.maximizeBtn)

        self.closeBtn = QPushButton(self.windowBtns)
        self.closeBtn.setObjectName(u"closeBtn")
        self.closeBtn.setMinimumSize(QSize(0, 30))
        self.closeBtn.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"	color: rgb(231, 255, 231);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(43, 144, 122);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(86, 172, 155);\n"
"}")

        self.horizontalLayout_3.addWidget(self.closeBtn)


        self.verticalLayout_6.addWidget(self.windowBtns)


        self.horizontalLayout_2.addWidget(self.windowFrame, 0, Qt.AlignTop)


        self.verticalLayout_5.addWidget(self.topFrame)

        self.contentFrame = QFrame(self.mainFrame)
        self.contentFrame.setObjectName(u"contentFrame")
        self.contentFrame.setFrameShape(QFrame.NoFrame)
        self.contentFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.contentFrame)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.contentContainer = QFrame(self.contentFrame)
        self.contentContainer.setObjectName(u"contentContainer")
        self.contentContainer.setFrameShape(QFrame.StyledPanel)
        self.contentContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.contentContainer)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.contentContainer)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QSize(1210, 0))
        self.scrollArea.setMaximumSize(QSize(16777215, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1208, 636))
        self.verticalLayout_9 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.allPaswordsFrame = QFrame(self.scrollAreaWidgetContents)
        self.allPaswordsFrame.setObjectName(u"allPaswordsFrame")
        self.allPaswordsFrame.setFrameShape(QFrame.StyledPanel)
        self.allPaswordsFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.allPaswordsFrame)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_9.addWidget(self.allPaswordsFrame, 0, Qt.AlignTop)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_4.addWidget(self.scrollArea)


        self.verticalLayout_7.addWidget(self.contentContainer)


        self.verticalLayout_5.addWidget(self.contentFrame)

        self.numOfPasswordsFrame = QFrame(self.mainFrame)
        self.numOfPasswordsFrame.setObjectName(u"numOfPasswordsFrame")
        self.numOfPasswordsFrame.setMinimumSize(QSize(0, 40))
        self.numOfPasswordsFrame.setMaximumSize(QSize(16777215, 40))
        self.numOfPasswordsFrame.setFrameShape(QFrame.NoFrame)
        self.numOfPasswordsFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.numOfPasswordsFrame)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.numOfPasswordsLabel = QLabel(self.numOfPasswordsFrame)
        self.numOfPasswordsLabel.setObjectName(u"numOfPasswordsLabel")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(11)
        self.numOfPasswordsLabel.setFont(font)
        self.numOfPasswordsLabel.setStyleSheet(u"color:rgb(33, 100, 69);")

        self.verticalLayout_11.addWidget(self.numOfPasswordsLabel, 0, Qt.AlignRight)


        self.verticalLayout_5.addWidget(self.numOfPasswordsFrame)


        self.horizontalLayout.addWidget(self.mainFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.toggleBtn.setText("")
        self.newBtn.setText("")
        self.pushButton_3.setText("")
        self.minimizeBtn.setText("")
        self.maximizeBtn.setText("")
        self.closeBtn.setText("")
        self.numOfPasswordsLabel.setText("")
    # retranslateUi

