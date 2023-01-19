import os
from os import listdir


class Images:

    images_fullpath = []
    images = []

    def loadImage(self, folder_dir):
        for image in os.listdir(folder_dir):
            if (image.endswith(".png")):
                self.images.append(image)
        return self.images

    def joinPaths(self, folder_dir):
        relativepath = self.images
        for x in self.images:
            fullpath = os.path.join(folder_dir, x)
            self.images_fullpath.append(fullpath)
        return self.images_fullpath
