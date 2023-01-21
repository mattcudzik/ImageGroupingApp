from ctypes.wintypes import FLOAT
from .IMetric import IMetric
from .Image import Image
from image_similarity_measures.quality_metrics import ssim


class ExampleMetric(IMetric):

    @staticmethod
    def compareImages(image1: Image, image2: Image) -> FLOAT:
        return ssim(image1.imageForCalculations, image2.imageForCalculations)

    '''
    def Compare(self, path, paths):
        img = path

        test_img = cv2.imread(img)

        ssim_measures = {}

        scale_percent = 100
        width = int(test_img.shape[1] * scale_percent / 100)
        height = int(test_img.shape[0] * scale_percent / 100)
        dim = (width, height)

        for file in paths:
            data_img = cv2.imread(file)
            resized_img = cv2.resize(
                data_img, dim, interpolation=cv2.INTER_AREA)
            ssim_measures[file] = ssim(test_img, resized_img)        

        result = []

        for i in ssim_measures.values():
            result.append(i)

        return result
    '''
