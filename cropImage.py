from PIL import Image

# Open the wafer image
wafer_image = Image.open("Level_1_Input_Data\wafer_image_1.png")  # Replace "wafer_image.jpg" with the actual file path

# Define the coordinates
top_left = (100, 200)  # Example coordinates
bottom_right = (300, 400)  # Example coordinates

# Crop the image based on the coordinates
cropped_image = wafer_image.crop((top_left[0], top_left[1], bottom_right[0], bottom_right[1]))

# Get the pixel data of the cropped image
pixel_data = list(cropped_image.getdata())

# Print the pixel data
print(pixel_data)