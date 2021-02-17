from ui_splash_screen import Ui_SplashScreen
from ui_main_window import Ui_MainWindow

import time

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


counter = 0

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        self.maximized = False

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
        self.ui.toggleBtn.clicked.connect(lambda: UIFunctions.toggle(self, 270, True))

        self.new_icon = QPixmap('assets/buttons/new_medium.png')
        self.ui.newBtn.setIcon(self.new_icon)
        self.ui.newBtn.setFont(self.font)

        self.show_password_icon = QPixmap('assets/buttons/show_password_small.png')
        self.hide_password_icon = QPixmap('assets/buttons/hide_password_small.png')
        self.ui.showHideBtn.setIcon(self.show_password_icon)

    def maximize_window(self):
        if self.maximized:
            self.showNormal()
            self.ui.maximizeBtn.setIcon(self.maximize_icon)
            self.maximized = False
        else:
            self.showMaximized()
            self.ui.maximizeBtn.setIcon(self.maximize2_icon)
            self.maximized = True
        

class SplashScreen(QMainWindow):
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
        global counter

        self.ui.progressBar.setValue(counter)

        if counter > 101:
            self.timer.stop()

            self.main = MainWindow()
            self.main.show()

            self.close()
        
        counter += 3

class UIFunctions(MainWindow):

    def toggle(self, maxWidth, enable):
        if enable:
            width = self.ui.sideMenuFrame.width()
            scrollWidth = self.ui.scrollArea.width()
            standart = 70

            if width == 70:
                widthExtended = maxWidth
                scrollExtended = self.ui.centralwidget.width() - widthExtended
                icon = self.menu_open_icon
                new_text = QApplication.translate("mainWindow", u"      New")
            else:
                widthExtended = standart
                scrollExtended = self.ui.centralwidget.width() - widthExtended
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