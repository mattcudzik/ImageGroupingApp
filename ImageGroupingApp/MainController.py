from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout
from MainMenuController import MainMenuController
from ImageViewController import ImageViewController
from PyQt5.uic import loadUi
import sys

class MainController(object):

    def __init__(self):
        self.app = QApplication(sys.argv)
        self.window = QMainWindow()
        loadUi('ui/mainWindow.ui', self.window)
        self.layout = self.window.findChild(QVBoxLayout, "layout")
        self.currentWidget = MainMenuController(self)
        self.window.setCentralWidget(self.currentWidget)

        self.window.show()
        self.app.exec()

    def changeMenu(self, newMenu):
        self.currentWidget.deleteLater()
        self.window.setCentralWidget(newMenu)
        self.window.adjustSize()

        self.currentWidget = newMenu
        self.currentWidget.mainLoop()



