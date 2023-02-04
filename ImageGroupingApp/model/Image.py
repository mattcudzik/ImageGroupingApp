import cv2
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore


class Image(object):
	#static constants
	CALC_IMAGE_SIZE = (400, 400)

	thumbnail = QPixmap

	def __init__(self, imagePath, imageName):
		self.imagePath = imagePath
		self.imageName = str(imageName)
		self.imageForCalculations = cv2.resize(cv2.imread(self.imagePath),self.CALC_IMAGE_SIZE, cv2.INTER_AREA)




