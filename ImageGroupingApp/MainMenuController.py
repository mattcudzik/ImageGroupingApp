from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5.uic import loadUi
from IMenuController import IMenuController

import ImageViewController

class MainMenuController(IMenuController):
    def __init__(self, mainController):
        IMenuController.__init__(self, mainController)
        loadUi('ui/mainMenu.ui', self)

        self.testButton = self.findChild(QPushButton, "testButton")
        self.label = self.findChild(QLabel, "label")

        self.testButton.clicked.connect(self.onTestButtonClicked)

    def onTestButtonClicked(self):
        self.label.setText("TEST")

        self.mainController.changeMenu(ImageViewController.ImageViewController('assets/img1.png', self.mainController))



