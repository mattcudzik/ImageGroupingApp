from PyQt5.QtWidgets import QLabel, QPushButton, QWidget, QGridLayout, QFrame, QVBoxLayout
from PyQt5.uic import loadUi
from IMenuController import IMenuController

import MainMenuController
import MainController
import ImageViewController
from model.Image import Image

class GroupedMenuController(IMenuController):
	def __init__(self):
		IMenuController.__init__(self)
		loadUi('ui/groupedMenu.ui', self)

		self.layout = self.findChild(QVBoxLayout, "verticalLayout")

		self.backButton = self.findChild(QPushButton, "backButton")
		self.backButton.clicked.connect(self.onBackButtonClicked)

		testGroup = ImageGroupWidget()
		testGroup.debugCreateGroup('assets/img1.png')
		
		testGroup2 = ImageGroupWidget()
		testGroup2.debugCreateGroup('assets/cat.png')
		
		self.layout.addWidget(testGroup)
		self.layout.addWidget(testGroup2)
	
		

	def onBackButtonClicked(self):
		MainController.MainController.getInstance().changeMenu(MainMenuController.MainMenuController())
	
class ImageGroupWidget(QWidget):
	def __init__(self):
		QWidget.__init__(self)
		loadUi('ui/imageGroupWidget.ui', self)
		self.layout = self.findChild(QGridLayout, "gridLayout")

	def debugCreateGroup(self, imgPath):
		tmpImg = Image(imgPath)
		for i in range(8):
			for j in range(3):
				tmp = SingleImageWidget(tmpImg)
				self.layout.addWidget(tmp,i,j)

		
		rows = self.layout.rowCount()

		#5,10 - padding
		minHeight = rows * (300 + 5) + 10
		self.setMinimumHeight(minHeight)

	
class SingleImageWidget(QWidget):
		def __init__(self, image: Image):
			QWidget.__init__(self)
			loadUi('ui/singleImageWidget.ui', self)

			self.image = image

			self.enterEvent = self.onEnter
			self.leaveEvent = self.onLeave
			self.mouseReleaseEvent = self.onClick

			self.frame = self.findChild(QFrame, "frame")
			self.nameLabel = self.findChild(QLabel, "nameLabel")
			#self.nameLabel.setText(self.image.imageName)


			self.imageLabel = self.findChild(QLabel, "imageLabel")
			
			self.imageLabel.setPixmap(self.image.thumbnail)

		def onEnter(self, event):
			self.frame.setLineWidth(3)

		def onLeave(self, event):
			self.frame.setLineWidth(0)

		def onClick(self, event):
			MainController.MainController.getInstance().changeMenu(ImageViewController.ImageViewController(self.image))


	
	
			