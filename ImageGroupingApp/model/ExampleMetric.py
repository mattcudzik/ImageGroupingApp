import cv2
import os
import image_similarity_measures
from image_similarity_measures.quality_metrics import rmse, ssim, sre

class ExampleMetric:

    
   

    def Compare(self):
        img = r'C:\Users\melec\Desktop\plotka\kot.png' #tutaj zast¹piæ tablic¹ zdjêæ i zrobiæ pêtle 

        test_img = cv2.imread(img)

        ssim_measures = {}
            
        scale_percent = 100 # percent of original img size
        width = int(test_img.shape[1] * scale_percent / 100)
        height = int(test_img.shape[0] * scale_percent / 100)
        dim = (width, height)

        data_dir = "C:\\Users\\melec\\Desktop\\plotka"
        for file in os.listdir(data_dir):
            if (file.endswith(".png")):
                img_path = os.path.join(data_dir, file)
                data_img = cv2.imread(img_path)
                resized_img = cv2.resize(data_img, dim, interpolation = cv2.INTER_AREA)
                ssim_measures[img_path]= ssim(test_img, resized_img)
                
        print(ssim_measures.values())
        print("######################################################################")


        
        result = []
        #if (True):
        #    closest = max(ssim_measures)
        #else:
        #    closest = min(ssim_measures)
                
        for i in ssim_measures.values():
            if(i > 0.7):
                result.append(i)
            
                
        print("The closest value: ", result)	    
        print("######################################################################")


    

    