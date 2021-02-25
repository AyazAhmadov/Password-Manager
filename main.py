from ui_splash_screen import Ui_SplashScreen
from ui_main_window import Ui_MainWindow
from account import Account

from pyperclip import copy as pyCopy

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

counter = 0

class MainWindow(QMainWindow):
        '''Main class responsible for showing the main window with all account'''
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        self.maximized = False
        self.hidden = True

        with open('passwords.csv', 'r') as f:
            data = [i.strip('\n') for i in f.readlines()]

        self.all_accounts = []

        for i in range(1, len(data)):
            values = data[i].split(',')
            a = Account(*values)
            self.all_accounts.append(a)

        ## ==> Font
        self.font = QFont()
        self.font.setFamily(u"Segoe UI")
        self.font.setPointSize(15)
        self.font.setBold(False)
        self.font.setWeight(50)

        close_icon = QPixmap('assets/buttons/close_small.png')
        self.ui.closeBtn.setIcon(close_icon)
        self.ui.closeBtn.clicked.connect(lambda: self.close())

        minimize_icon = QPixmap('assets/buttons/minimize_small.png')
        self.ui.minimizeBtn.setIcon(minimize_icon)
        self.ui.minimizeBtn.clicked.connect(lambda: self.showMinimized())

        self.maximize2_icon = QPixmap('assets/buttons/maximize2_small.png')
        self.maximize_icon = QPixmap('assets/buttons/maximize_small.png')
        self.ui.maximizeBtn.setIcon(self.maximize_icon)
        self.ui.maximizeBtn.clicked.connect(lambda: self.maximize_window())

        self.menu_open_icon = QPixmap('assets/buttons/menu_open_medium.png')
        self.menu_closed_icon = QPixmap('assets/buttons/menu_closed_medium.png')
        self.ui.toggleBtn.setIcon(self.menu_closed_icon)
        self.ui.toggleBtn.clicked.connect(lambda: UIFunctions.toggle(self, 180, True))

        self.new_icon = QPixmap('assets/buttons/new_medium.png')
        self.ui.newBtn.setIcon(self.new_icon)
        self.ui.newBtn.setFont(self.font)

        self.show_password_icon = QPixmap('assets/buttons/show_password_small.png')
        self.hide_password_icon = QPixmap('assets/buttons/hide_password_small.png')

        self.ui.numOfPasswordsLabel.setText(f'<strong>Number of accounts:</strong> {len(self.all_accounts)} ')

        self.load_passwords()

    def maximize_window(self):
            '''Maximizes or minimizes the window'''
        if self.maximized:
            self.showNormal()
            self.ui.maximizeBtn.setIcon(self.maximize_icon)
            self.maximized = False
        else:
            self.showMaximized()
            self.ui.maximizeBtn.setIcon(self.maximize2_icon)
            self.maximized = True

    def show_hide_password(self, account, label, button):
            '''Function responsible for showing or hiding the password in a QLabel'''
        if account.hidden:
            label.setText(account.shown_password)
            button.setIcon(self.hide_password_icon)
            account.hidden = False
        else:
            label.setText(account.hidden_password)
            button.setIcon(self.show_password_icon)
            account.hidden = True

    def copy_password(self, account):
        print(type(account))
        pyCopy(account.shown_password)
        print(f'Copied {account.shown_password}')

    def edit_account(self, account):
            '''Method responsible for editing an account. Loads a new frame replacing the main one'''
        self.ui.contentContainer.setHidden(True)
        editWindow = EditFrame(self, account)
        editWindow.show_frame()

    def load_passwords(self):
            '''Loads all passwords from self.all_accounts to show on the main window'''
        count = 1

        font = QFont()
        font.setFamily(u"Nirmala UI")
        font.setPointSize(10)

        for account in self.all_accounts:
            frame = QFrame(self.ui.allPaswordsFrame)
            frame.setObjectName(u'accountFrame ' + str(count))
            frame.setMinimumSize(QSize(0, 40))
            frame.setMaximumSize(QSize(16777215, 40))
            frame.setStyleSheet(u"color: rgb(30, 68, 42);\n""background-color: rgb(221, 255, 240);\n""border: 1px solid rgb(33, 100, 69);")
            frame.setFrameShape(QFrame.NoFrame)
            frame.setFrameShadow(QFrame.Raised)

            horizontalLayout = QHBoxLayout(frame)
            horizontalLayout.setSpacing(0)
            horizontalLayout.setObjectName(u"accountLayout " + str(count))
            horizontalLayout.setContentsMargins(0, 0, 0, 0)

            logoContainer = QFrame(frame)
            logoContainer.setObjectName(u'logoContainer ' + str(count))
            logoContainer.setMinimumSize(QSize(38, 38))
            logoContainer.setMaximumSize(QSize(38, 38))
            logoContainer.setStyleSheet(u'border:none')
            logoContainer.setFrameShape(QFrame.NoFrame)
            logoContainer.setFrameShadow(QFrame.Raised)

            logoContainerLayout = QVBoxLayout(logoContainer)
            logoContainerLayout.setSpacing(0)
            logoContainerLayout.setObjectName(u'logoContainerLayout ' + str(count))
            logoContainerLayout.setContentsMargins(0, 0, 0, 0)
            logoFrame = QFrame(logoContainer)

            logoFrame.setObjectName(u'logoFrame ' + str(count))
            logoFrame.setMinimumSize(QSize(38, 38))
            logoFrame.setMaximumSize(QSize(38, 38))
            logoFrame.setStyleSheet(u'border:none')
            logoFrame.setFrameShape(QFrame.NoFrame)
            logoFrame.setFrameShadow(QFrame.Raised)

            logoLayout = QVBoxLayout(logoFrame)
            logoLayout.setSpacing(0)
            logoLayout.setObjectName(u'logoLayout ' + str(count))
            logoLayout.setContentsMargins(0, 0, 0, 0)

            logoLabel = QLabel(frame)
            logoLabel.setObjectName(u"logoLabel " + str(count))
            logoLabel.setMinimumSize(QSize(38, 38))
            logoLabel.setMaximumSize(QSize(38, 38))
            logoLabel.setStyleSheet(u"border: none")
            logoLabel.setPixmap(QPixmap(account.logo))
            logoLayout.addWidget(logoLabel, 0, Qt.AlignHCenter|Qt.AlignVCenter)

            logoContainerLayout.addWidget(logoFrame, 0, Qt.AlignHCenter|Qt.AlignVCenter)

            horizontalLayout.addWidget(logoContainer)

            line1 = QFrame(frame)
            line1.setObjectName(u"line1_" + str(count))
            line1.setMaximumSize(QSize(1, 16777215))
            line1.setStyleSheet(u"border: none;\n""background-color:rgb(33, 100, 69);")
            line1.setFrameShape(QFrame.VLine)
            line1.setFrameShadow(QFrame.Sunken)
            horizontalLayout.addWidget(line1)

            nameLabel = QLabel(frame)
            nameLabel.setObjectName(u"nameLabel " + str(count))
            nameLabel.setMaximumSize(QSize(66, 16777215))
            nameLabel.setFont(font)
            nameLabel.setStyleSheet(u"border: none")
            nameLabel.setText(account.name)
            horizontalLayout.addWidget(nameLabel, 0, Qt.AlignHCenter)

            line2 = QFrame(frame)
            line2.setObjectName(u"line2_" + str(count))
            line2.setMaximumSize(QSize(1, 16777215))
            line2.setStyleSheet(u"border: none;\n""background-color:rgb(33, 100, 69);")
            line2.setFrameShape(QFrame.VLine)
            line2.setFrameShadow(QFrame.Sunken)
            horizontalLayout.addWidget(line2)

            domainLabel = QLabel(frame)
            domainLabel.setObjectName(u"domainLabel " + str(count))
            domainLabel.setFont(font)
            domainLabel.setStyleSheet(u"border:none")
            domainLabel.setText(account.domain)
            horizontalLayout.addWidget(domainLabel, 0, Qt.AlignHCenter)

            line3 = QFrame(frame)
            line3.setObjectName(u"line3_" + str(count))
            line3.setMaximumSize(QSize(1, 16777215))
            line3.setStyleSheet(u"border: none;\n""background-color:rgb(33, 100, 69);")
            line3.setFrameShape(QFrame.VLine)
            line3.setFrameShadow(QFrame.Sunken)
            horizontalLayout.addWidget(line3)

            usernameLabel = QLabel(frame)
            usernameLabel.setObjectName(u"usernameLabel " + str(count))
            usernameLabel.setFont(font)
            usernameLabel.setMinimumSize(QSize(150, 0))
            usernameLabel.setStyleSheet(u"border: none")
            usernameLabel.setText(account.username)
            usernameLabel.setTextInteractionFlags(Qt.TextSelectableByMouse)
            usernameLabel.setCursor(QtCore.Qt.IBeamCursor)
            horizontalLayout.addWidget(usernameLabel, 0, Qt.AlignHCenter)

            line4 = QFrame(frame)
            line4.setObjectName(u"line4_" + str(count))
            line4.setMaximumSize(QSize(1, 16777215))
            line4.setStyleSheet(u"border: none;\n""background-color:rgb(33, 100, 69);")
            line4.setFrameShape(QFrame.VLine)
            line4.setFrameShadow(QFrame.Sunken)
            horizontalLayout.addWidget(line4)

            dateLabel = QLabel(frame)
            dateLabel.setObjectName(u"dateLabel " + str(count))
            dateLabel.setFont(font)
            dateLabel.setStyleSheet(u"border: none")
            dateLabel.setText(account.date)
            horizontalLayout.addWidget(dateLabel, 0, Qt.AlignHCenter)

            line5 = QFrame(frame)
            line5.setObjectName(u"line5_" + str(count))
            line5.setMaximumSize(QSize(1, 16777215))
            line5.setStyleSheet(u"border: none;\n""background-color:rgb(33, 100, 69);")
            line5.setFrameShape(QFrame.VLine)
            line5.setFrameShadow(QFrame.Sunken)
            horizontalLayout.addWidget(line5)

            passwordLabel = QLabel(frame)
            passwordLabel.setObjectName(u"passwordLabel " + str(count))
            passwordLabel.setFont(font)
            passwordLabel.setStyleSheet(u"border:none")
            passwordLabel.setText(account.hidden_password)
            horizontalLayout.addWidget(passwordLabel, 0, Qt.AlignHCenter)

            line6 = QFrame(frame)
            line6.setObjectName(u"line6_" + str(count))
            line6.setMaximumSize(QSize(1, 16777215))
            line6.setStyleSheet(u"border: none;\n""background-color:rgb(33, 100, 69);")
            line6.setFrameShape(QFrame.VLine)
            line6.setFrameShadow(QFrame.Sunken)
            horizontalLayout.addWidget(line6)

            copyBtn = QPushButton(frame)
            copyBtn.setObjectName(u'copyBtn ' + str(count))
            copyBtn.setMinimumSize(QSize(0, 38))
            copyBtn.setMaximumSize(QSize(60, 16777215))
            copyBtn.setFont(font)
            copyBtn.setStyleSheet(u"QPushButton{\n""	border: none;\n""	background-color: rgb(26, 156, 124);\n""}\n""\n""QPushButton:hover{\n""	background-color: rgb(97, 176, 147);\n""}\n""\n""QPushButton:pressed{\n""	background-color: rgb(145, 218, 190);\n""}")
            copyBtn.setText('Copy')
            copyBtn.clicked.connect(lambda: pyCopy(account.shown_password))
            horizontalLayout.addWidget(copyBtn)

            line7 = QFrame(frame)
            line7.setObjectName(u"line7_" + str(count))
            line7.setMaximumSize(QSize(1, 16777215))
            line7.setStyleSheet(u"border: none;\n""background-color:rgb(33, 100, 69);")
            line7.setFrameShape(QFrame.VLine)
            line7.setFrameShadow(QFrame.Sunken)
            horizontalLayout.addWidget(line7)            

            editBtn = QPushButton(frame)
            editBtn.setObjectName(u"editBtn" + str(count))
            editBtn.setMinimumSize(QSize(0, 38))
            editBtn.setMaximumSize(QSize(70, 16777215))
            editBtn.setFont(font)
            editBtn.setStyleSheet(u"QPushButton{\n""	border: none;\n""	background-color: rgb(26, 156, 124);\n""}\n""\n""QPushButton:hover{\n""	background-color: rgb(97, 176, 147);\n""}\n""\n""QPushButton:pressed{\n""	background-color: rgb(145, 218, 190);\n""}")
            editBtn.setText('Edit')
            editBtn.clicked.connect(lambda account=account: self.edit_account(account))
            horizontalLayout.addWidget(editBtn)

            line8 = QFrame(frame)
            line8.setObjectName(u"line8_" + str(count))
            line8.setMaximumSize(QSize(1, 16777215))
            line8.setStyleSheet(u"border: none;\n""background-color:rgb(33, 100, 69);")
            line8.setFrameShape(QFrame.VLine)
            line8.setFrameShadow(QFrame.Sunken)
            horizontalLayout.addWidget(line8)

            deleteBtn = QPushButton(frame)
            deleteBtn.setObjectName(u"deleteBtn" + str(count))
            deleteBtn.setMinimumSize(QSize(0, 38))
            deleteBtn.setMaximumSize(QSize(70, 16777215))
            deleteBtn.setFont(font)
            deleteBtn.setStyleSheet(u"QPushButton{\n""	border: none;\n""	background-color: rgb(26, 156, 124);\n""}\n""\n""QPushButton:hover{\n""	background-color: rgb(97, 176, 147);\n""}\n""\n""QPushButton:pressed{\n""	background-color: rgb(145, 218, 190);\n""}")
            deleteBtn.setText('Delete')
            horizontalLayout.addWidget(deleteBtn)

            line9 = QFrame(frame)
            line9.setObjectName(u"line8_" + str(count))
            line9.setMaximumSize(QSize(1, 16777215))
            line9.setStyleSheet(u"border: none;\n""background-color:rgb(33, 100, 69);")
            line9.setFrameShape(QFrame.VLine)
            line9.setFrameShadow(QFrame.Sunken)
            horizontalLayout.addWidget(line9)

            showHideBtn = QPushButton(frame)
            showHideBtn.setObjectName(u"showHideBtn " + str(count))
            showHideBtn.setMinimumSize(QSize(40, 38))
            showHideBtn.setMaximumSize(QSize(40, 16777215))
            showHideBtn.setStyleSheet(u"QPushButton{\n""	border: none;\n""	background-color: rgb(26, 156, 124);\n""}\n""\n""QPushButton:hover{\n""	background-color: rgb(97, 176, 147);\n""}\n""\n""QPushButton:pressed{\n""	background-color: rgb(145, 218, 190);\n""}")
            showHideBtn.setIconSize(QSize(96, 96))
            showHideBtn.setIcon(self.show_password_icon)
            showHideBtn.clicked.connect(lambda account=account, label=passwordLabel, button=showHideBtn: self.show_hide_password(account, label, button))
            horizontalLayout.addWidget(showHideBtn)

            self.ui.verticalLayout_10.addWidget(frame)
        

class SplashScreen(QMainWindow):
        '''Class for displating a splash screen before the main window is shown'''
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(35)

        self.show()

    def progress(self):
            '''Method responsible for the progress bar'''
        global counter

        self.ui.progressBar.setValue(counter)

        if counter > 101:
            self.timer.stop()

            self.main = MainWindow()
            self.main.show()

            self.close()
        
        counter += 3

class EditFrame:
        '''Class responsible for edit frame. Shown when editBtn is clicked in MainWindow class'''
    def __init__(self, mainwindow, account):
        self.account = account

        self.editContainer = QFrame(mainwindow.ui.contentFrame)
        self.editContainer.setObjectName(u"editContainer")
        self.editContainer.setFrameShape(QFrame.StyledPanel)
        self.editContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.editContainer)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.separator1 = QFrame(self.editContainer)
        self.separator1.setObjectName(u"separator1")
        self.separator1.setMinimumSize(QSize(403, 0))
        self.separator1.setStyleSheet(u"")
        self.separator1.setFrameShape(QFrame.NoFrame)
        self.separator1.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.separator1)

        self.editSeparator = QFrame(self.editContainer)
        self.editSeparator.setObjectName(u"editSeparator")
        self.editSeparator.setStyleSheet(u"")
        self.editSeparator.setFrameShape(QFrame.NoFrame)
        self.editSeparator.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.editSeparator)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.editFrame = QFrame(self.editSeparator)
        self.editFrame.setObjectName(u"editFrame")
        self.editFrame.setStyleSheet(u"color: rgb(30, 68, 42);\n""border: 2px solid rgb(30, 68, 42);")
        self.editFrame.setFrameShape(QFrame.NoFrame)
        self.editFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.editFrame)
        self.gridLayout.setObjectName(u"gridLayout")

        self.domainEditLabel = QLabel(self.editFrame)
        self.domainEditLabel.setObjectName(u"domainEditLabel")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        self.domainEditLabel.setFont(font)
        self.domainEditLabel.setStyleSheet(u"border: none")
        self.domainEditLabel.setText('Domain')

        self.gridLayout.addWidget(self.domainEditLabel, 2, 0, 1, 1)

        self.domainEdit = QLineEdit(self.editFrame)
        self.domainEdit.setObjectName(u"domainEdit")
        self.domainEdit.setMinimumSize(QSize(0, 30))
        self.domainEdit.setFont(font)
        self.domainEdit.setStyleSheet(u"border: 2px solid rgb(30, 68, 42);\n""background-color: rgb(221, 255, 240)")
        self.domainEdit.setText(account.domain)

        self.gridLayout.addWidget(self.domainEdit, 2, 2, 1, 1)

        self.passwordEdit = QLineEdit(self.editFrame)
        self.passwordEdit.setObjectName(u"passwordEdit")
        self.passwordEdit.setMinimumSize(QSize(0, 30))
        self.passwordEdit.setFont(font)
        self.passwordEdit.setStyleSheet(u"border: 2px solid rgb(30, 68, 42);\n""background-color: rgb(221, 255, 240)")

        self.gridLayout.addWidget(self.passwordEdit, 4, 2, 1, 1)

        self.nameEdit = QLineEdit(self.editFrame)
        self.nameEdit.setObjectName(u"nameEdit")
        self.nameEdit.setMinimumSize(QSize(0, 30))
        self.nameEdit.setFont(font)
        self.nameEdit.setStyleSheet(u"border: 2px solid rgb(30, 68, 42);\n""background-color: rgb(221, 255, 240)")
        self.nameEdit.setText(account.name)

        self.gridLayout.addWidget(self.nameEdit, 1, 2, 1, 1)

        self.logoEditLabel = QLabel(self.editFrame)
        self.logoEditLabel.setObjectName(u"logoEditLabel")
        self.logoEditLabel.setFont(font)
        self.logoEditLabel.setStyleSheet(u"border: none")
        self.logoEditLabel.setText('Logo')

        self.gridLayout.addWidget(self.logoEditLabel, 0, 0, 1, 1)

        self.passwordEditLabel = QLabel(self.editFrame)
        self.passwordEditLabel.setObjectName(u"passwordEditLabel")
        self.passwordEditLabel.setFont(font)
        self.passwordEditLabel.setStyleSheet(u"border: none")
        self.passwordEditLabel.setText('Password')

        self.gridLayout.addWidget(self.passwordEditLabel, 4, 0, 1, 1)

        self.btnsFrame = QFrame(self.editFrame)
        self.btnsFrame.setObjectName(u"btnsFrame")
        self.btnsFrame.setMinimumSize(QSize(0, 30))
        self.btnsFrame.setStyleSheet(u"border: none")
        self.btnsFrame.setFrameShape(QFrame.NoFrame)
        self.btnsFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.btnsFrame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.saveBtn = QPushButton(self.btnsFrame)
        self.saveBtn.setObjectName(u"saveBtn")
        self.saveBtn.setMinimumSize(QSize(0, 30))
        self.saveBtn.setMaximumSize(QSize(80, 16777215))
        self.saveBtn.setFont(font)
        self.saveBtn.setStyleSheet(u"QPushButton{\n""    border: none;\n""    background-color: rgb(26, 156, 124);\n""    }\n""\n""QPushButton:hover{\n""    background-color: rgb(97, 176, 147);\n""    }\n""\n""QPushButton:pressed{\n""    background-color: rgb(145, 218, 190);\n""    }")
        self.saveBtn.setText('Save')

        self.horizontalLayout_6.addWidget(self.saveBtn)

        self.cancelBtn = QPushButton(self.btnsFrame)
        self.cancelBtn.setObjectName(u"cancelBtn")
        self.cancelBtn.setMinimumSize(QSize(0, 30))
        self.cancelBtn.setMaximumSize(QSize(80, 16777215))
        self.cancelBtn.setStyleSheet(u"QPushButton{\n""    border: none;\n""    background-color: rgb(26, 156, 124);\n""    }\n""\n""QPushButton:hover{\n""    background-color: rgb(97, 176, 147);\n""    }\n""\n""QPushButton:pressed{\n""    background-color: rgb(145, 218, 190);\n""    }")
        self.cancelBtn.setText('Cancel')

        self.horizontalLayout_6.addWidget(self.cancelBtn)


        self.gridLayout.addWidget(self.btnsFrame, 5, 0, 1, 3)

        self.usernameEdit = QLineEdit(self.editFrame)
        self.usernameEdit.setObjectName(u"usernameEdit")
        self.usernameEdit.setMinimumSize(QSize(0, 30))
        self.usernameEdit.setFont(font)
        self.usernameEdit.setStyleSheet(u"border: 2px solid rgb(30, 68, 42);\n""background-color: rgb(221, 255, 240)")
        self.usernameEdit.setText(account.username)

        self.gridLayout.addWidget(self.usernameEdit, 3, 2, 1, 1)

        self.usernameEditLabel = QLabel(self.editFrame)
        self.usernameEditLabel.setObjectName(u"usernameEditLabel")
        self.usernameEditLabel.setFont(font)
        self.usernameEditLabel.setStyleSheet(u"border: none")
        self.usernameEditLabel.setText('Username')

        self.gridLayout.addWidget(self.usernameEditLabel, 3, 0, 1, 1)

        self.nameEditLabel = QLabel(self.editFrame)
        self.nameEditLabel.setObjectName(u"nameEditLabel")
        self.nameEditLabel.setFont(font)
        self.nameEditLabel.setStyleSheet(u"border: none")
        self.nameEditLabel.setText('Name')

        self.gridLayout.addWidget(self.nameEditLabel, 1, 0, 1, 1)

        self.logoEditFrame = QFrame(self.editFrame)
        self.logoEditFrame.setObjectName(u"logoEditFrame")
        self.logoEditFrame.setMinimumSize(QSize(0, 30))
        self.logoEditFrame.setFrameShape(QFrame.NoFrame)
        self.logoEditFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.logoEditFrame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")

        logo = QPixmap(account.logo)
        self.logoPicLabel = QLabel(self.logoEditFrame)
        self.logoPicLabel.setObjectName(u"logoEditLabel_2")
        self.logoPicLabel.setMinimumSize(QSize(130, 130))
        self.logoPicLabel.setMaximumSize(QSize(130, 130))
        self.logoPicLabel.setStyleSheet(u"border: 1px solid rgb(30, 68, 42);")
        self.logoPicLabel.setPixmap(logo)

        self.horizontalLayout_5.addWidget(self.logoPicLabel)

        self.browseBtn = QPushButton(self.logoEditFrame)
        self.browseBtn.setObjectName(u"browseBtn")
        self.browseBtn.setMinimumSize(QSize(0, 30))
        self.browseBtn.setMaximumSize(QSize(90, 16777215))
        self.browseBtn.setStyleSheet(u"QPushButton{\n""    border: none;\n""    background-color: rgb(26, 156, 124);\n""    }\n""\n""QPushButton:hover{\n""    background-color: rgb(97, 176, 147);\n""    }\n""\n""QPushButton:pressed{\n""    background-color: rgb(145, 218, 190);\n""    }")
        self.browseBtn.setText('Browse')

        self.horizontalLayout_5.addWidget(self.browseBtn, 0, Qt.AlignBottom)


        self.gridLayout.addWidget(self.logoEditFrame, 0, 2, 1, 1)


        self.verticalLayout_8.addWidget(self.editFrame, 0, Qt.AlignVCenter)


        self.horizontalLayout_4.addWidget(self.editSeparator)

        self.separator2 = QFrame(self.editContainer)
        self.separator2.setObjectName(u"separator2")
        self.separator2.setMinimumSize(QSize(403, 0))
        self.separator2.setStyleSheet(u"")
        self.separator2.setFrameShape(QFrame.NoFrame)
        self.separator2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.separator2)

        mainwindow.ui.verticalLayout_7.addWidget(self.editContainer)

        self.editContainer.setHidden(True)

    def show_frame(self):
        self.editContainer.setHidden(False)

    def hide_frame(self):
        self.editContainer.setHidden(True)

class UIFunctions(MainWindow):
        '''Class holding ui methods'''
    def toggle(self, maxWidth, enable):
            '''Extends or minimizes the side menu'''
        if enable:
            width = self.ui.sideMenuFrame.width()
            scrollWidth = self.ui.scrollArea.width()
            standart = 70

            if width == 70:
                widthExtended = maxWidth
                scrollExtended = self.ui.centralwidget.width() - widthExtended - 2
                icon = self.menu_open_icon
                new_text = QApplication.translate("mainWindow", u"      New")
            else:
                widthExtended = standart
                scrollExtended = self.ui.centralwidget.width() - widthExtended - 2
                icon = self.menu_closed_icon
                new_text = ""

            self.side_menu_animation = QPropertyAnimation(self.ui.sideMenuFrame, b'maximumWidth')
            self.side_menu_animation.setDuration(250)
            self.side_menu_animation.setStartValue(width)
            self.side_menu_animation.setEndValue(widthExtended)

            self.scroll_area_animation = QPropertyAnimation(self.ui.scrollArea, b'minimumWidth')
            self.scroll_area_animation.setDuration(250)
            self.scroll_area_animation.setStartValue(scrollWidth)
            self.scroll_area_animation.setEndValue(scrollExtended)

            self.side_menu_animation.start()
            self.scroll_area_animation.start()

            self.ui.toggleBtn.setIcon(icon)
            self.ui.newBtn.setText(new_text)



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())