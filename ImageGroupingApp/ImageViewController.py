from PyQt5.QtWidgets import QPushButton, QColorDialog, QSlider, QLabel, QFrame
from PyQt5.uic import loadUi
from IMenuController import IMenuController

import MainMenuController
from model.Annotation import Annotation
from tools.PaintBrushTool import PaintBrushTool
from tools.EraserTool import EraserTool

import cv2


class ImageViewController(IMenuController):
    def __init__(self, imgPath, mainController):
        IMenuController.__init__(self, mainController)
        loadUi('ui/imageMenu.ui', self)

        self.annotation = Annotation(imgPath)

        self.brushButton = self.findChild(QPushButton, "brushButton")
        self.brushButton.clicked.connect(self.onBrushButtonClicked)
        

        self.eraserButton = self.findChild(QPushButton, "eraserButton")
        self.eraserButton.clicked.connect(self.onEraserButtonClicked)
        

        self.textButton = self.findChild(QPushButton, "textButton")
        self.textButton.clicked.connect(self.onTextButtonClicked)

        self.colorButton = self.findChild(QPushButton, "colorButton")
        self.colorButton.clicked.connect(self.onColorButtonClicked)


        self.backButton = self.findChild(QPushButton, "backButton")
        self.backButton.clicked.connect(self.onBackButtonClicked)

        self.sizeSlider = self.findChild(QSlider,"sizeSlider")
        self.sizeSlider.valueChanged[int].connect(self.onSizeSlideChanged)


        self.sizeLabel = self.findChild(QLabel,"sizeLabel")

        #frame = self.findChild(QLabel,"sizeLabe")
        #height = self.cvImg.shape[0]
        #width = self.cvImg.shape[1]

        #ratio = width/height
        #newHeight = 720
        #newWidth = int(newHeight*ratio)
        #self.cvImg = cv2.resize(self.cvImg,(newWidth,newHeight))

        
        self.brushTool = PaintBrushTool(self.annotation) 
        self.eraserTool = EraserTool(self.annotation)

        self.selectedTool = self.brushTool
        self.tools = list((self.brushTool,self.eraserTool))

        cv2.namedWindow("Image window")
        cv2.setMouseCallback("Image window", self.cv2MouseEvents)
        cv2.imshow("Image window",self.annotation.getMergedLayers())

        self.windowOpened = True

    def onBrushButtonClicked(self):
        self.selectedTool = self.brushTool
    
    def onEraserButtonClicked(self):
        self.selectedTool = self.eraserTool

    def onTextButtonClicked(self):
        pass

    def onColorButtonClicked(self):
        color = QColorDialog.getColor()

        if color.isValid():  
            color = color.getRgb()
            color = (color[2],color[1],color[0], 255)
            self.brushTool.color = color


    def onBackButtonClicked(self):
        self.mainController.changeMenu(MainMenuController.MainMenuController(self.mainController)) 
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
                
        
   

    


