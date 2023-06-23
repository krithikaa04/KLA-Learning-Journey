import cv2
from PIL import Image

img1 = cv2.imread('Level_1_Input_Data\\wafer_image_1.png', 0)  
img2 = cv2.imread('Level_1_Input_Data\\wafer_image_2.png', 0)  
img3 = cv2.imread('Level_1_Input_Data\\wafer_image_3.png', 0)  
img4 = cv2.imread('Level_1_Input_Data\\wafer_image_4.png', 0)  
img5 = cv2.imread('Level_1_Input_Data\\wafer_image_5.png', 0)  

#get pixel data from images
wafer1 = img1.load()
wafer2 = img2.load()