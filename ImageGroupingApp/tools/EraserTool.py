import cv2
from .ITool import ITool

class EraserTool(ITool):
	def __init__(self, annotation):
		ITool.__init__(self, annotation)
		self.color = (0,0,0,0)
		self.isDrawing = False
		self.prevPosition = (-1,-1)

	def manageMouseEvents(self, event, x, y):
		if event == cv2.EVENT_LBUTTONDOWN:
			self.prevPosition = (x,y)
			self.isDrawing = True
		elif event == cv2.EVENT_LBUTTONUP:
			self.isDrawing = False
		elif event == cv2.EVENT_MOUSEMOVE and self.isDrawing:
			cv2.line(self.annotationLayer,self.prevPosition,(x,y), self.color,self.size)
			self.prevPosition = (x,y)



