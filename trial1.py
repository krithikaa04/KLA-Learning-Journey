import json
from PIL import Image
import cv2


json_file_path = 'Level_1_Input_Data\\input.json'
with open(json_file_path, 'r') as json_file:
    data = json.load(json_file)

def dict_to_list(nested_dict):
    if isinstance(nested_dict, dict):
        return [dict_to_list(value) for value in nested_dict.values()]
    elif isinstance(nested_dict, list):
        return [dict_to_list(item) for item in nested_dict]
    else:
        return nested_dict
print(data)
care_areas = data['care_areas']
die_position = data['die']
#print(die_position)
die_width = (die_position.get('width'))
die_height = (die_position.get('height'))
num_rows = (die_position.get('rows'))
num_col = (die_position.get('columns'))
#print(die_height)
print(care_areas)

for i in care_areas:
    result = i
    top_right = {'x': result['bottom_right']['x'], 'y': result['top_left']['y']}
    bottom_left = {'x': result['top_left']['x'], 'y': result['bottom_right']['y']}
    result['top_right'] = top_right
    result['bottom_left'] = bottom_left

for i in care_areas:
    #nested_dict = i
    care_areas_coord = dict_to_list(i)
    

print(care_areas_coord)
#Extract the pixel data within the die region from the wafer image.
img1 = cv2.imread('Level_1_Input_Data\wafer_image_1.png', 0)  
img2 = cv2.imread('Level_1_Input_Data\wafer_image_2.png', 0)  
img3 = cv2.imread('Level_1_Input_Data\wafer_image_3.png', 0)  
img4 = cv2.imread('Level_1_Input_Data\wafer_image_4.png', 0)  
img5 = cv2.imread('Level_1_Input_Data\wafer_image_5.png', 0)  
 

