import numpy as np
import cv2
import os,imutils


images=[]                                



directory_path=input("Enter the path of the database\n")
dir_path=os.listdir(directory_path)



for path in os.listdir(directory_path):
        track=os.path.join(directory_path,path)
        img = cv2.imread(track,cv2.IMREAD_COLOR)
        images.append(img)
    
print(len(images))
imageStitcher = cv2.Stitcher_create()
ret,stitchImg=imageStitcher.stitch(images)

if ret==0:
    cv2.imshow("stiched image",stitchImg)
    cv2.waitKey(0)

else:
    print("Stitching failed")
