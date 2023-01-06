import cv2
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore
import os


class Image(object):
	#static variable
	thumbnailSize = (290,250)

	def __init__(self, imagePath):
		self.imagePath = imagePath

		words = self.imagePath.split('/')
		self.imageName = words[-1]

		#scale to fit
		w = self.thumbnailSize[0]
		h = self.thumbnailSize[1]
		self.thumbnail = QPixmap(self.imagePath).scaled(w,h, QtCore.Qt.KeepAspectRatio)




