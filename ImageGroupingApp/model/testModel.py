import unittest
import os
import cv2
from ddt import data, ddt, unpack
from . import ExampleMetric
from . import Image

#Tests for application
#To properly run tests, it is required to create folder in path given in ROOT attribute
#All files of which names are given in parameterized tests should really exist in given folder or tests will fail

@ddt
class TestModel(unittest.TestCase):
    testMetric = ExampleMetric.ExampleMetric()
    #path to subfolder with images for tests
    ROOT = os.path.join(os.path.abspath(os.getcwd()), "tests")
    #expected value of dimensions of resized picture
    EXPECTED_RESIZE_VALUE = 400

    #Test if comparing equal images with metric works properly (outputs value 1.0)
    #Files of which names are given in this test should exist
    @data("big.jpg", "cat.png", "forest.jpg", "back.png")
    def testCompareImagesEqual(self, filename):
        try:
            img1 = Image.Image(os.path.join(self.ROOT, filename), filename)
            img2 = Image.Image(os.path.join(self.ROOT, filename), filename)
            result = self.testMetric.compareImages(img1, img2)
            self.assertEqual(1.0, result, "Compare calculations should not be equal.")
        except cv2.error:
            self.fail("Given image (" + filename + ") does not exist on " + self.ROOT + " folder.")

    #Test if comparing unequal images with metric works properly (outputs value different than 1.0)
    #Files of which names are given in this test should exist
    @data(("big.jpg", "cat.png"), ("cat.png", "forest.jpg"))
    @unpack
    def testCompareImagesNotEqual(self, filename1, filename2):
        try:
            img1 = Image.Image(os.path.join(self.ROOT, filename1), filename1)
            img2 = Image.Image(os.path.join(self.ROOT, filename2), filename2)
            result = self.testMetric.compareImages(img1, img2)
            self.assertNotEqual(1.0, result, "Compare calculations should not be equal.")
        except cv2.error:
            self.fail("Given image/images does/do not exist on " + self.ROOT + " folder.")
            
    #Test if proper error is thrown when given image does not exist
    #Files of which names are given in this test should not exist
    @data("doesNotExist.png", "doesntExist.jpg", "NoFile.jpg")
    def testImageInitThrows(self, filename):
        try:
            img1 = Image.Image(os.path.join(self.ROOT, filename), filename)
            self.fail("Such image should throw an exception.")
        except cv2.error:
            pass

    #Test if files are resized correctly
    #Files of which names are given in this test should exist
    @data("big.jpg", "cat.png", "forest.jpg", "back.png")
    def testImageResize(self, filename):
        try:
            img1 = Image.Image(os.path.join(self.ROOT, filename), filename)
            self.assertEqual(self.EXPECTED_RESIZE_VALUE,
                            img1.imageForCalculations.shape[0], 
                            "Resized dimension does not equal " + str(self.EXPECTED_RESIZE_VALUE))
            self.assertEqual(self.EXPECTED_RESIZE_VALUE, 
                             img1.imageForCalculations.shape[1],
                             "Resized dimension does not equal " + str(self.EXPECTED_RESIZE_VALUE))
        except cv2.error:
            self.fail("Given image (" + filename + ") does not exist on " + self.ROOT + " folder.") 


if __name__ == '__main__':
    unittest.main()
