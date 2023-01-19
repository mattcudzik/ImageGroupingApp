import shutil
import Images
import IMetric
import os
from os.path import exists

class GroupingModel:

    def __init__(self, dir, thr, opt):
        self.folder_dir = dir #"./testimages" #sciezka do folderu
        self.threshold = thr #0.8 #wartosc progowa dolna grupowania
        self.choosen = opt #1  

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
