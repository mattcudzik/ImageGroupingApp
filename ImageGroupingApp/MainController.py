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
        self.currentWidget = ImageViewController('assets/cat.png', self) #MainMenuController(self)
        self.layout.addWidget(self.currentWidget)
        self.window.show()
        self.app.exec()

    def changeMenu(self, newMenu):
        self.layout.removeWidget(self.currentWidget)
        self.currentWidget.deleteLater()
        self.layout.addWidget(newMenu)
        self.currentWidget = newMenu




