from asyncio.windows_events import NULL
from PyQt5.QtWidgets import QPushButton, QFileDialog
from PyQt5.uic import loadUi
from IMenuController import IMenuController

import GroupedMenuController
import ImageViewController
import MainController
import ProgressBarMenuController
from model.GroupingModel import GroupingModel

class MainMenuController(IMenuController):
    def __init__(self):
        IMenuController.__init__(self)
        loadUi('ui/mainMenu.ui', self)

        self.createButton = self.findChild(QPushButton, "createButton")
        self.createButton.clicked.connect(self.onCreateButtonClicked)

        self.loadButton = self.findChild(QPushButton, "loadButton")
        self.loadButton.clicked.connect(self.onLoadButtonClicked)

    def onLoadButtonClicked(self):
        #MainController.MainController.getInstance().changeMenu(ImageViewController.ImageViewController(img))
        pass


    def onCreateButtonClicked(self):
        path = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        if len(path) != 0:
            GroupingModel.folderDir = path
        
            MainController.MainController.getInstance().changeMenu(ProgressBarMenuController.ProgressBarMenuController())




