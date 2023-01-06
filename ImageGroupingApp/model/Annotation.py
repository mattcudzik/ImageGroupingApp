import cv2
import os
import numpy as np
from .Image import Image

class Annotation(object):
	def __init__(self, image: Image):
		self.image = image
		self.imageLayer = cv2.imread(self.image.imagePath)
		
		self.annotationPath = "annotations/" + self.image.imagePath

		words = self.annotationPath.split('.')
		words[-1] = ".png"

		self.annotationPath = ''.join(words)
		
		words = self.annotationPath.split('/')
		
		words[-1] = ""
		directionPath = '/'.join(words)

		if not os.path.exists(directionPath):
			os.makedirs(directionPath)

		if not os.path.exists(self.annotationPath):
			imgShape = self.imageLayer.shape
			self.annotationLayer = np.zeros((imgShape[0],imgShape[1],4), np.uint8)
			cv2.imwrite(self.annotationPath, self.annotationLayer)
		else:
			self.annotationLayer = cv2.imread(self.annotationPath, -1)

		self.merged = self.imageLayer.copy()

	def getMergedLayers(self):
		x = 0
		y = 0
		# Extract the alpha mask of the RGBA image, convert to RGB 
		b,g,r,a = cv2.split(self.annotationLayer)
		overlay_color = cv2.merge((b,g,r))
	
		# Apply some simple filtering to remove edge noise
		mask = cv2.medianBlur(a,5)

		h, w, _ = overlay_color.shape
		roi = self.imageLayer[y:y+h, x:x+w]

		# Black-out the area behind the logo in our original ROI
		img1_bg = cv2.bitwise_and(roi.copy(),roi.copy(),mask = cv2.bitwise_not(mask))
	
		# Mask out the logo from the logo image.
		img2_fg = cv2.bitwise_and(overlay_color,overlay_color,mask = mask)

		# Update the original image with our new ROI
		self.merged[y:y+h, x:x+w] = cv2.add(img1_bg, img2_fg)

		return self.merged

	def saveAnnotation(self):
		cv2.imwrite(self.annotationPath, self.annotationLayer)

	def scaleToSize(self, size):
		pass
