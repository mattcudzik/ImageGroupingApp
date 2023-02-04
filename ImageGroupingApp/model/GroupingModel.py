import os

from . import IMetric
from .ExampleMetric import ExampleMetric
from .Image import Image
from .Group import Group
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore

class GroupingModel(object):
	#allowed file types
	ALLOWED_FILE_TYPES = [".png", ".jpg", ".jpeg", ".bmp", ".tiff" , ".tif"]
	#path to main images folder
	folderDir = ""
	
	THUMBNAIL_SIZE = (290,250)

	#Singleton
	__instance = None
	@staticmethod 
	def getInstance() -> 'GroupingModel':
		if GroupingModel.__instance == None:
			GroupingModel(0.8)
		return GroupingModel.__instance

	def __init__(self, thr):
		if GroupingModel.__instance != None:
			raise Exception("This class is a singleton!")
		else:
			GroupingModel.__instance = self

			self.threshold = thr #lower threshold value for grouping
			self.choosenMetric = ExampleMetric
			
			self.loadedImages = []
			self.groups = []
			self.progressBarMenu = None

	def loadImages(self):
		filesAmount = 0
		for root,d_names,f_names in os.walk(self.folderDir):
			for f in f_names:
				#count only supported images
				filename, fileExtension = os.path.splitext(f)
				if fileExtension in self.ALLOWED_FILE_TYPES:
					filesAmount += 1

		counter = 0

		#recursively searching for images from the root folder
		for root,d_names,f_names in os.walk(self.folderDir):
			for f in f_names:

				#skip not supported files
				filename, fileExtension = os.path.splitext(f)
				if fileExtension in self.ALLOWED_FILE_TYPES:

					#update progress bar
					if self.progressBarMenu != None:
						progress = (counter * 100) /filesAmount
						self.progressBarMenu.updateProgresBar(progress)
					imgToAdd = Image(os.path.join(root, f), f)
					w = self.THUMBNAIL_SIZE[0]
					h = self.THUMBNAIL_SIZE[1]
					imgToAdd.thumbnail = QPixmap(imgToAdd.imagePath).scaled(w,h, QtCore.Qt.KeepAspectRatio)
					self.loadedImages.append(imgToAdd)
					counter += 1

	def groupImages(self):
		#inform controller about current state
		if self.progressBarMenu != None:
			self.progressBarMenu.calculationStarted()

		resultsMatrix = []

		rowCounter = 0
		for img1 in self.loadedImages:
			#skip first and last img - self comparison is pointless
			if rowCounter == 0 or rowCounter == len(self.loadedImages)-1 :
				rowCounter += 1
				continue

			rowResults = []
			for img2 in self.loadedImages:
				if(img1 == img2):
					break
				else:
					#update progress bar
					if self.progressBarMenu != None:
						progress =(rowCounter * 100)/ len(self.loadedImages)
						self.progressBarMenu.updateProgresBar(progress)
					rowResults.append(self.choosenMetric.compareImages(img1, img2))
			resultsMatrix.append(rowResults)
			rowCounter += 1

		'''
		#MAX method
		for resultI in resultsMatrix:
			#find max similarity for resultI image
			maxSimilarity = max(resultI)
			maxIndex = resultI.index(maxSimilarity)

			#check if another image isn't more similar
			for resultJ in resultsMatrix:
				#skip part of the matrix that doesn't contain this image
				if len(resultJ) <= maxIndex+1:
					continue
		'''

		#list of indexes of images to add to groups
		imagesToAdd = [*range(0,len(self.loadedImages))]
		
		while(len(imagesToAdd) > 0):

			tmpGroup = Group()
			tmpGroup.addImage(self.loadedImages[imagesToAdd[0]])
			
			rowNumber = 1
			for row in resultsMatrix:
				if len(row) <= imagesToAdd[0]:
					rowNumber += 1
					continue
				#skip already added images
				if not (rowNumber in imagesToAdd):
					rowNumber += 1
					continue
				if row[imagesToAdd[0]] >= self.threshold:
					tmpGroup.addImage(self.loadedImages[rowNumber])
					#delete added image from queue
					imagesToAdd.remove(rowNumber)
				rowNumber += 1
			
			imagesToAdd.pop(0)
			self.groups.append(tmpGroup)

		self.onProcessFinished()

	def onProcessFinished(self):
		self.progressBarMenu.onGroupingFinished()

	def resetModel(self):
		self.progressBarMenu = None
		self.loadedImages = []
		self.groups = []

	'''
	def process(self):
		paths = []
		fullpaths = []

		images = Images.Images()
		paths = images.loadImage(self.folder_dir)
		fullpaths = images.joinPaths(self.folder_dir)

		metric = []
		imetric = IMetric.IMetric()
		metric.append(imetric.get_Values(fullpaths, self.choosen))

		tempmetric = metric[0]

		#grupowanie folderow
		for i in range((len(tempmetric))):
			rangea = range((int(i)), (len(tempmetric[i])))
			for j in rangea:
				a = int(j)
				print(tempmetric[i][a])
				if (tempmetric[i][j] == 1):
					temppath = paths[i][:-4]
					if not os.path.exists(self.folder_dir + "\\" + temppath):
						os.mkdir(self.folder_dir + "\\" + temppath)

				if (tempmetric[i][j] > self.threshold):
					file = self.folder_dir + "\\" + paths[j]
					if (exists(self.folder_dir + "\\" + paths[j])):
						shutil.move(file, self.folder_dir + "\\" +
									paths[i][:-4] + "\\" + paths[j])
						tempmetric[i][j] = 0

		#usuwanie pustych folderow
		folders = list(os.walk(self.folder_dir))[1:]
		for folder in folders:
			if not folder[2]:
				os.rmdir(folder[0])

	def get_Values(self, paths, choosen):
		metric = ExampleMetric.ExampleMetric()

		metricArray = []
		for path in paths:
			metricArray.append(metric.Compare(path, paths))  # wybor metryki

		return metricArray
	'''