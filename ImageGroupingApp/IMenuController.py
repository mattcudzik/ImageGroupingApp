from PyQt5.QtWidgets import QWidget
import abc


class IMenuController(QWidget):
	#@abc.abstractmethod
	#def __init__(self, mainController):
	#	super(QWidget, self).__init__()
	#	self.mainController = mainController

	@abc.abstractmethod
	def mainLoop(self):
		pass
