from PIL import Image
from numpy import asarray
from copy import deepcopy
from copy import copy


im = Image.open("top_gun.jpg")
im_resized = im.resize((im.width//30, im.height//30))
height = im_resized.height
width = im_resized.width

print("Successfully loaded image!")
print("Image size: " + str(width) + " x " + str(height))
print()

flattened_data = list(im_resized.getdata()) 
pixel_matrix = []
internal_matrix = []
count = 0

for i in range(height):
    for j in range(width):
        internal_matrix.append(flattened_data[count])
        count += 1
    pixel_matrix.append(internal_matrix)
    internal_matrix = []

print("Successfully constructed pixel matrix!")
print("Pixel matrix size: " + str(width) + " x " + str(height))
print("Iterating through pixel contents ...")
print()

print("Successfully constructed brightness matrix!")
print("Brightness matrix size: " + str(width) + " x " + str(height))
print("Iterating through pixel brightness ...")
print()

brightness_matrix = deepcopy(pixel_matrix)
for x in range(len(pixel_matrix)):
    for y in range(len(pixel_matrix[x])):
        pixel = pixel_matrix[x][y]
        sum_value = 0
        avg_value = 0
        for i,z in enumerate(pixel):
            sum_value += z
        avg_value = sum_value // len(pixel)
        brightness_matrix[x][y] = avg_value

ascii_char = "`^\",:;Il!i~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
ascii_len = len(ascii_char)

print("Successfully constructed ASCII matrix!")
print("ASCII matrix size: " + str(width) + " x " + str(height))
print("Iterating through pixel ASCII characters ...")
print()

ASCII_matrix = copy(pixel_matrix)
for x in range(len(brightness_matrix)):
    for y in range(len(brightness_matrix[x])):
        ASCII_matrix[x][y] = ascii_char[int(ascii_len/256 * brightness_matrix[x][y])]
        print(ASCII_matrix[x][y]*5, end='')
    print()




    
