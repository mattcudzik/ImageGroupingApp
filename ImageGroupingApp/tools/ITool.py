import abc

class ITool(object):
	@abc.abstractmethod
	def __init__(self, annotation):
		self.size = 50
		self.color = (0, 0, 0, 255)
		self.annotation = annotation
		self.annotationLayer = annotation.annotationLayer

	@abc.abstractmethod
	def manageMouseEvents(self,event,x,y):
		pass
