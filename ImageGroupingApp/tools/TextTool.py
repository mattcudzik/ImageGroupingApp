
import cv2
from .ITool import ITool

class TextTool(ITool):
	def __init__(self, annotation, textInput):
		ITool.__init__(self, annotation)
		self.textInput = textInput

	def manageMouseEvents(self, event, x, y):
		if event == cv2.EVENT_LBUTTONDOWN:
			text = self.textInput.text()

			if text:
				cv2.putText(self.annotationLayer,text,(x,y),cv2.FONT_HERSHEY_SIMPLEX, self.size, self.color,5)



