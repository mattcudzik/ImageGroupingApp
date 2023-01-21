from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout
from MainMenuController import MainMenuController
from model.GroupingModel import  GroupingModel

from PyQt5.uic import loadUi
import sys

class MainController(object):
	#Singleton
	__instance = None

	@staticmethod 
	def getInstance():
		if MainController.__instance == None:
			MainController()
		return MainController.__instance


	def __init__(self):
		if MainController.__instance != None:
			raise Exception("This class is a singleton!")
		else:
			MainController.__instance = self
			self.app = QApplication(sys.argv)
			self.window = QMainWindow()
			loadUi('ui/mainWindow.ui', self.window)
			self.layout = self.window.findChild(QVBoxLayout, "layout")
			self.currentWidget = MainMenuController()
			self.window.setCentralWidget(self.currentWidget)

			self.window.show()
			self.app.exec()

	def changeMenu(self, newMenu):
		self.currentWidget.deleteLater()
		self.window.setCentralWidget(newMenu)
		self.window.adjustSize()

		self.currentWidget = newMenu
		self.currentWidget.mainLoop()

