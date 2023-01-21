from PyQt5.QtWidgets import QPushButton, QColorDialog, QSlider, QLabel, QFrame, QLineEdit
from PyQt5.uic import loadUi
from IMenuController import IMenuController

import GroupedMenuController
import MainController

from model.Annotation import Annotation
from tools.PaintBrushTool import PaintBrushTool
from tools.EraserTool import EraserTool
from tools.TextTool import TextTool

from model.Image import Image
import cv2


class ImageViewController(IMenuController):
	def __init__(self, image :Image):
		IMenuController.__init__(self)
		loadUi('ui/imageMenu.ui', self)

		self.annotation = Annotation(image)

		self.brushButton = self.findChild(QPushButton, "brushButton")
		self.brushButton.clicked.connect(self.onBrushButtonClicked)
		

		self.eraserButton = self.findChild(QPushButton, "eraserButton")
		self.eraserButton.clicked.connect(self.onEraserButtonClicked)
		

		self.textButton = self.findChild(QPushButton, "textButton")
		self.textButton.clicked.connect(self.onTextButtonClicked)
		self.textInputFrame = self.findChild(QFrame,"textInputFrame")
		self.textInput = self.findChild(QLineEdit,"textInput")


		self.colorButton = self.findChild(QPushButton, "colorButton")
		self.colorButton.clicked.connect(self.onColorButtonClicked)


		self.backButton = self.findChild(QPushButton, "backButton")
		self.backButton.clicked.connect(self.onBackButtonClicked)

		self.sizeSlider = self.findChild(QSlider,"sizeSlider")
		self.sizeSlider.valueChanged[int].connect(self.onSizeSlideChanged)
		self.sizeLabel = self.findChild(QLabel,"sizeLabel")

		

		#height = self.cvImg.shape[0]
		#width = self.cvImg.shape[1]

		#ratio = width/height
		#newHeight = 720
		#newWidth = int(newHeight*ratio)
		#self.ratio = (newWidth,newHeight)
		#self.cvImg = cv2.resize(self.cvImg,(newWidth,newHeight))

		
		self.brushTool = PaintBrushTool(self.annotation) 
		self.eraserTool = EraserTool(self.annotation)
		self.textTool = TextTool(self.annotation, self.textInput)

		self.selectedTool = self.brushTool
		self.tools = list((self.brushTool,self.eraserTool,self.textTool))

		cv2.namedWindow("Image window")
		cv2.setMouseCallback("Image window", self.cv2MouseEvents)
		cv2.imshow("Image window",self.annotation.getMergedLayers())

		self.windowOpened = True

	def onBrushButtonClicked(self):

		self.textInputFrame.setEnabled(False)
		self.selectedTool = self.brushTool
	
	def onEraserButtonClicked(self):
		self.textInputFrame.setEnabled(False)
		self.selectedTool = self.eraserTool

	def onTextButtonClicked(self):
		self.textInputFrame.setEnabled(True)
		self.selectedTool = self.textTool

	def onColorButtonClicked(self):
		color = QColorDialog.getColor()

		if color.isValid():  
			color = color.getRgb()
			color = (color[2],color[1],color[0], 255)
			self.brushTool.color = color
			self.textTool.color = color


	def onBackButtonClicked(self):
		MainController.MainController.getInstance().changeMenu(GroupedMenuController.GroupedMenuController()) 
		
		self.windowOpened = False
		cv2.destroyAllWindows()
		self.annotation.saveAnnotation()
	
	def onSizeSlideChanged(self, value):
		for tool in self.tools:
			tool.size = value

		self.sizeLabel.setText(str(value))

	def cv2MouseEvents(self, event,x,y,flags,param):
		self.selectedTool.manageMouseEvents(event,x,y)
		
	def mainLoop(self):
		while(self.windowOpened):
			cv2.imshow("Image window",self.annotation.getMergedLayers())
			cv2.waitKey(1)
				
		
   

	


