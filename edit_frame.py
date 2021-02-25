class EditFrame:
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