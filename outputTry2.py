from PIL import Image
import json
import csv

def dict_to_list(nested_dict):
    if isinstance(nested_dict, dict):
        return [dict_to_list(value) for value in nested_dict.values()]
    elif isinstance(nested_dict, list):
        return [dict_to_list(item) for item in nested_dict]
    else:
        return nested_dict

def find_careArea_coord(data):
    care_areas = data['care_areas']
    die_position = data['die']
    die_width = die_position['width']
    die_height = die_position['height']
    num_rows = die_position['rows']
    num_cols = die_position['columns']

    care_areas_coord = []

    for i in range(num_rows):
        for j in range(num_cols):
            top_left_x = die_width * j
            top_left_y = die_height * i
            bottom_right_x = top_left_x + die_width
            bottom_right_y = top_left_y + die_height
            care_areas_coord.append([top_left_x, bottom_right_x, top_left_y, bottom_right_y])

    return care_areas_coord

def find_die_index(die_coordinates, x, y):
    for index, coordinates in enumerate(die_coordinates):
        if coordinates[0] <= x <= coordinates[1] and coordinates[2] <= y <= coordinates[3]:
            return index + 1  
    return None  
'''
def find_defect_areas(data,care_areas_coord,wafer1_gray,wafer2_gray,threshold):
    defective_pixels = []
    die_coordinates = find_careArea_coord(data)
    # Iterate over each pixel
    for x in range(wafer1_gray.width):
        #print(x)
        #break
        for y in range(wafer1_gray.height):
            a=[]
            
            pixel1 = wafer1_gray.getpixel((x, y))
            pixel2 = wafer2_gray.getpixel((x, y))

            # Compare the pixel values
            if abs(pixel1 - pixel2) > threshold:
                die_index = find_die_index(die_coordinates, x, y)
                defective_pixels.append(f"{die_index},{x},{y}")

    return defective_pixels
'''
def find_defect_areas(data, care_areas_coord, wafer1_gray, wafer2_gray, threshold):
    defective_pixels = []
    die_coordinates = find_careArea_coord(data)
    for die_index, coordinates in enumerate(die_coordinates, start=1):
        top_left_x, bottom_right_x, top_left_y, bottom_right_y = coordinates
        for x in range(top_left_x, bottom_right_x):
            if x >= wafer1_gray.width:
                break

            for y in range(top_left_y, bottom_right_y):
                if y >= wafer1_gray.height:
                    break

                pixel1 = wafer1_gray.getpixel((x, y))
                pixel2 = wafer2_gray.getpixel((x, y))
                if abs(pixel1 - pixel2) > threshold:
                    defective_pixels.append(f"{die_index},{x},{y}")

    return defective_pixels

json_file_path = 'Level_1_Input_Data\\input.json'
with open(json_file_path, 'r') as json_file:
    data = json.load(json_file)
print(data)
find_careArea_coord(data)

threshold = 0.1
wafer1 = Image.open("Level_1_Input_Data\\wafer_image_1.png")
wafer2 = Image.open("Level_1_Input_Data\\wafer_image_2.png")
wafer3 = Image.open("Level_1_Input_Data\\wafer_image_3.png")
wafer4 = Image.open("Level_1_Input_Data\\wafer_image_4.png")
wafer5 = Image.open("Level_1_Input_Data\\wafer_image_5.png")

#convert to gray scale
wafer1_gray = wafer1.convert("L")
wafer2_gray = wafer2.convert("L")
wafer3_gray = wafer3.convert("L") 
wafer4_gray = wafer4.convert("L") 
wafer5_gray = wafer5.convert("L")   

care_areas_coord = find_careArea_coord(data)
print(care_areas_coord)
#defective_pixels_13 = find_defect_areas(data,care_areas_coord,wafer1_gray, wafer3_gray, threshold)
#defective_pixels_23 = find_defect_areas(data,care_areas_coord,wafer2_gray, wafer3_gray, threshold)
#defective_pixels_12 = find_defect_areas(data,care_areas_coord,wafer1_gray, wafer2_gray, threshold)

defective_pixels_35 = find_defect_areas(data,care_areas_coord,wafer3_gray, wafer5_gray, threshold)
defective_pixels_45 = find_defect_areas(data,care_areas_coord,wafer4_gray, wafer5_gray, threshold)

file_path = "output.csv"
with open(file_path, "w", newline="") as csvfile:
    csv_writer = csv.writer(csvfile)

    # Write the coordinates to the CSV file
    csv_writer.writerows([coordinate.split(",") for coordinate in defective_pixels_35])
    csv_writer.writerows([coordinate.split(",") for coordinate in defective_pixels_45])


print("CSV file saved successfully.")

