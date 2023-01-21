from .Image import Image

class Group(object):
    def __init__(self) -> None:
        self.images :list[Image] = []

    def addImage(self, imageToAdd: Image):

        #don't add duplicates
        for img in self.images:
            if img.imagePath == imageToAdd.imagePath:
                return

        self.images.append(imageToAdd)


