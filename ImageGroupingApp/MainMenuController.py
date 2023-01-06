from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5.uic import loadUi
from IMenuController import IMenuController

import GroupedMenuController
import ImageViewController
import MainController
from model.Image import Image

class MainMenuController(IMenuController):
    def __init__(self):
        #IMenuController.__init__(self, mainController)
        IMenuController.__init__(self)
        loadUi('ui/mainMenu.ui', self)

        self.testButton = self.findChild(QPushButton, "testButton")
        self.label = self.findChild(QLabel, "label")
        self.testButton.clicked.connect(self.onTestButtonClicked)

        self.nextButton = self.findChild(QPushButton, "pushButton")
        self.nextButton.clicked.connect(self.onNextButtonClicked)

    def onTestButtonClicked(self):
        self.label.setText("TEST")

        img = Image('assets/mountain1.jpg')
        MainController.MainController.getInstance().changeMenu(ImageViewController.ImageViewController(img))

    def onNextButtonClicked(self):
        MainController.MainController.getInstance().changeMenu(GroupedMenuController.GroupedMenuController())


