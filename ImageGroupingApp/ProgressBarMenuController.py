from asyncio.windows_events import NULL
from ctypes.wintypes import INT
from email.charset import QP
from PyQt5.QtWidgets import QProgressBar, QApplication, QLabel, QPushButton
from PyQt5.uic import loadUi
from IMenuController import IMenuController

import GroupedMenuController
import MainController
from model.GroupingModel import GroupingModel

class ProgressBarMenuController(IMenuController):
    def __init__(self):
        IMenuController.__init__(self)
        loadUi('ui/progressBarMenu.ui', self)

        self.progressBar: QProgressBar = self.findChild(QProgressBar, "progressBar")
        self.infoLabel: QLabel = self.findChild(QLabel, "infoLabel")

        self.startButton: QPushButton = self.findChild(QPushButton, "startButton")
        self.startButton.clicked.connect(self.onStartButtonClicked)
    
    def calculationStarted(self):
        self.infoLabel.setText("Calculating...")
        self.progressBar.setValue(0)
        QApplication.processEvents()

    def updateProgresBar(self, progress : INT):
        self.progressBar.setValue(progress)
        QApplication.processEvents()

    def onGroupingFinished(self):
        MainController.MainController.getInstance().changeMenu(GroupedMenuController.GroupedMenuController())
  
    def onStartButtonClicked(self):
        self.infoLabel.setText("Loading images...")
        GroupingModel.getInstance().progressBarMenu = self
        GroupingModel.getInstance().loadImages()
        GroupingModel.getInstance().groupImages()
