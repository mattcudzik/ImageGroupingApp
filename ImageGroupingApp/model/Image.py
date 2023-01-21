import cv2
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore


class Image(object):
	#static constants
	THUMBNAIL_SIZE = (290,250)
	CALC_IMAGE_SIZE = (400, 400)

	def __init__(self, imagePath, imageName):
		self.imagePath = imagePath
		self.imageName = str(imageName)

		#scale to fit
		w = self.THUMBNAIL_SIZE[0]
		h = self.THUMBNAIL_SIZE[1]
		self.thumbnail = QPixmap(self.imagePath).scaled(w,h, QtCore.Qt.KeepAspectRatio)

		self.imageForCalculations = cv2.resize(cv2.imread(self.imagePath),self.CALC_IMAGE_SIZE, cv2.INTER_AREA)







