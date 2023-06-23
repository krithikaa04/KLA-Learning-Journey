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
'''    
def find_careArea_coord(data):
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
'''
def find_careArea_coord(data):
    care_areas = data
    
    care_areas_coord = []

    for area in care_areas:
        top_left_x = area['top_left']['x']
        top_left_y = area['top_left']['y']
        bottom_right_x = area['bottom_right']['x']
        bottom_right_y = area['bottom_right']['y']
        
        # Calculate the other corners
        top_right_x = bottom_right_x
        top_right_y = top_left_y
        bottom_left_x = top_left_x
        bottom_left_y = bottom_right_y
        top_left_lst=[]
        top_right_lst=[]
        bottom_left_lst=[]
        bottom_right_lst=[]
        top_left_lst.append((top_left_x,top_left_y))
        top_right_lst.append((top_right_x,top_right_y))
        bottom_left_lst.append((bottom_left_x,bottom_right_lst))
        bottom_right_lst.append((bottom_right_x,bottom_right_y))
        care_areas_coord.append((top_left_lst,top_right_lst,bottom_left_lst,bottom_right_lst))

    return care_areas_coord



def find_die_index(die_coordinates, x, y):
    for index, coordinates in enumerate(die_coordinates):
        if coordinates[0] <= x <= coordinates[1] and coordinates[2] <= y <= coordinates[3]:
            return index + 1  
    return None  

def find_defect_areas(data, care_areas_coord, wafer1_gray, wafer2_gray, wafer3_gray, threshold):
    defective_pixels = []
    die_coordinates = find_careArea_coord(data)

    # Iterate over each die area
    for die_index, coordinates in enumerate(die_coordinates, start=1):
        top_left_x, bottom_right_x, top_left_y, bottom_right_y = coordinates

        # Iterate over pixels within the die area
        for x in range(top_left_x, bottom_right_x):
            # Ensure x-coordinate is within image boundaries
            if x >= wafer1_gray.width:
                break

            for y in range(top_left_y, bottom_right_y):
                # Ensure y-coordinate is within image boundaries
                if y >= wafer1_gray.height:
                    break

                pixel1_wafer1 = wafer1_gray.getpixel((x, y))
                pixel1_wafer2 = wafer2_gray.getpixel((x, y))
                pixel1_wafer3 = wafer3_gray.getpixel((x, y))
                
                # Compare the pixel values between wafer 1 and wafer 2
                if abs(pixel1_wafer1 - pixel1_wafer2) > threshold:
                    # Check if the pixel values match between wafer 2 and wafer 3
                    if abs(pixel1_wafer1 - pixel1_wafer3) > threshold:
                        defective_pixels.append(f"{die_index},{x},{y}")

    return defective_pixels

json_file_path = 'Level_1_Input_Data\\input.json'
with open(json_file_path, 'r') as json_file:
    data = json.load(json_file)
print(data)
print(data['care_areas'])


#find_careArea_coord(data)

threshold = 0.1
wafer1 = Image.open("Level_1_Input_Data\\wafer_image_1.png")
wafer2 = Image.open("Level_1_Input_Data\\wafer_image_2.png")
wafer3 = Image.open("Level_1_Input_Data\\wafer_image_3.png")

#convert to gray scale
wafer1_gray = wafer1.convert("L")
wafer2_gray = wafer2.convert("L")
wafer3_gray = wafer3.convert("L")   

care_areas_coord = find_careArea_coord(data['care_areas'])
print(care_areas_coord)
defective_pixels_123 = find_defect_areas(data,care_areas_coord,wafer1_gray, wafer2_gray,wafer3_gray, threshold)
#defective_pixels_23 = find_defect_areas(data,care_areas_coord,wafer2_gray, wafer3_gray, threshold)

file_path = "output.csv"
with open(file_path, "w", newline="") as csvfile:
    csv_writer = csv.writer(csvfile)

    # Write the coordinates to the CSV file
    csv_writer.writerows([coordinate.split(",") for coordinate in defective_pixels_123])


print("CSV file saved successfully.")

