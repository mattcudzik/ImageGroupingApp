from ctypes.wintypes import FLOAT
import abc
from .Image import Image

class IMetric:
    @abc.abstractmethod
    def compareImages(self, image1 :Image, image2 :Image) -> FLOAT:
        pass

