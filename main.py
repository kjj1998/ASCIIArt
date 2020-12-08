from PIL import Image
from construct import construct_pixel_matrix
from construct import construct_brightness_matrix
from construct import construct_ascii_matrix

# ASCII characters in order of density (thickest to thinnest)
ASCII = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft//\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
ASCII = ASCII[::-1]

# Open image using Pillow Image Processing Library and resize the image to be
# 10 times smaller
im = Image.open("ntu_logo.png")
im_resized = im.resize((im.width//5, im.height//5))

height = im_resized.height
width = im_resized.width

print("Successfully loaded image!")
print("Image size: " + str(width) + " x " + str(height))
print()

# Unpack all the pixel values into a single List
flattened_data = list(im_resized.getdata()) 

# Construct the 2D Pixel Matrix
pixel_matrix = construct_pixel_matrix(height, width, flattened_data)

# Construct the Brightness Matrix
brightness_matrix = construct_brightness_matrix(height, width, pixel_matrix)

# Construct and print the ASCII Matrix to console
construct_ascii_matrix(height, width, brightness_matrix, ASCII)

