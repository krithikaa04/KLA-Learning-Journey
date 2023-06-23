from PIL import Image

def find_defect_areas(wafer1_gray,wafer2_gray,threshold):
    defective_pixels = []

    # Iterate over each pixel
    for x in range(wafer1_gray.width):
        for y in range(wafer1_gray.height):
            pixel1 = wafer1_gray.getpixel((x, y))
            pixel2 = wafer2_gray.getpixel((x, y))

            # Compare the pixel values
            if abs(pixel1 - pixel2) > threshold:
                defective_pixels.append((x, y))

    return defective_pixels

threshold = 1  # Adjust the threshold value based on your requirements
wafer1 = Image.open("Level_1_Input_Data\\wafer_image_1.png")
wafer2 = Image.open("Level_1_Input_Data\\wafer_image_2.png")
wafer3 = Image.open("Level_1_Input_Data\\wafer_image_3.png")

#convert to gray scale
wafer1_gray = wafer1.convert("L")
wafer2_gray = wafer2.convert("L")
wafer3_gray = wafer3.convert("L")   #consider as reference image

defective_pixels_13 = find_defect_areas(wafer1_gray, wafer3_gray, threshold)
defective_pixels_23 = find_defect_areas(wafer2_gray, wafer3_gray, threshold)

print(defective_pixels_13)
print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print(defective_pixels_23)
