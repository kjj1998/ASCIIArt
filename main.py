from PIL import Image
from construct import construct_pixel_matrix
from construct import construct_brightness_matrix
from construct import construct_ascii_matrix

ASCII = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft//\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
ASCII = ASCII[::-1]

im = Image.open("ntu_logo.png")
im_resized = im.resize((im.width//10, im.height//10))
height = im_resized.height
width = im_resized.width

print("Successfully loaded image!")
print("Image size: " + str(width) + " x " + str(height))
print()

flattened_data = list(im_resized.getdata()) 
pixel_matrix = construct_pixel_matrix(height, width, flattened_data)
brightness_matrix = construct_brightness_matrix(height, width, pixel_matrix)
construct_ascii_matrix(height, width, brightness_matrix, ASCII)

