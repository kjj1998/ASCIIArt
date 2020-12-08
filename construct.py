
def construct_pixel_matrix(height, width, flattened_data):
    """ Function to contstruct the pixel matrix of the picture
    in the form of a 2D array
    """

    pixel_matrix, internal_matrix = [], []
    count = 0

    for i in range(height):
        for j in range(width):
            internal_matrix.append(flattened_data[count])
            count += 1

        pixel_matrix.append(internal_matrix)
        internal_matrix = []

    print("Successfully constructed pixel matrix!")
    print("Pixel matrix size: " + str(width) + " x " + str(height))
    print()

    return pixel_matrix

def construct_brightness_matrix(height, width, pixel_matrix):
   brightness_matrix = [[0 for i in range(len(pixel_matrix[0]))] for j in range(len(pixel_matrix))]
   for x in range(len(pixel_matrix)):
   	for y in range(len(pixel_matrix[x])):
	    pixel = pixel_matrix[x][y]
	    sum_value = 0
	    avg_value = 0
	    for i,z in enumerate(pixel):
	        sum_value += z
	    avg_value = sum_value // len(pixel)
	    brightness_matrix[x][y] = avg_value

   print("Successfully constructed brightness matrix!")
   print("Brightness matrix size: " + str(width) + " x " + str(height))
   print()

   return brightness_matrix

def construct_ascii_matrix(height, width, brightness_matrix, ASCII):
    ASCII_matrix = [[0 for i in range(len(brightness_matrix[0]))] for j in range(len(brightness_matrix))]
    for x in range(len(brightness_matrix)):
        for y in range(len(brightness_matrix[x])):
            ASCII_matrix[x][y] = ASCII[int(len(ASCII)/256 * brightness_matrix[x][y])]
            print(ASCII_matrix[x][y]*3, end='')
        print()

    print("Successfully constructed ASCII matrix!")
    print("ASCII matrix size: " + str(width) + " x " + str(height))
    print()




   

