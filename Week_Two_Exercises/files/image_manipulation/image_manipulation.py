from matplotlib import image
from matplotlib import pyplot
import os
import numpy as py

script_path = os.path.dirname(os.path.abspath(__file__))
usa_image = script_path + "/" + "usa.png"
usa_image_data = image.imread(usa_image)
lenna_image = script_path + "/" + "lenna.bmp"
lenna_image_data = image.imread(lenna_image)

edited_image_data = lenna_image_data.copy()

edited_image_data[
    : usa_image_data.shape[0], lenna_image_data.shape[1] - usa_image_data.shape[1]:
] = (255 * usa_image_data)

print(f"Image type is {type(usa_image_data)}")
print(f"Image shape is {usa_image_data.shape}")

# for width in range(usa_image_data.shape[1]):
#    for height in range(usa_image_data.shape[0]):
#        edited_image_data[height][512 - 250 + width] = [
# int(255 * usa_image_data[height][width][0]),
#     int(255 * usa_image_data[height][width][1]),
#     int(255 * usa_image_data[height][width][2]),
# ]

image.imsave(script_path + "/" + "edited_image.jpg", edited_image_data)

pyplot.imshow(edited_image_data)
pyplot.show()
