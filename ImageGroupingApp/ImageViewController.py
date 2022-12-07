from PyQt5.QtWidgets import QLabel, QPushButton
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap
from IMenuController import IMenuController

import MainMenuController

class ImageViewController(IMenuController):
    def __init__(self, imgPath, mainController):
        IMenuController.__init__(self, mainController)
        loadUi('ui/imageMenu.ui', self)

        self.imgPath = imgPath
        self.imageLabel = self.findChild(QLabel, "imageLabel")

        self.image = QPixmap(self.imgPath)
        self.imageLabel.setPixmap(self.image)

        self.testButton = self.findChild(QPushButton, "testButton")
        self.testButton.clicked.connect(self.onTestButtonClicked)

    def onTestButtonClicked(self):
        self.mainController.changeMenu(MainMenuController.MainMenuController(self.mainController))




