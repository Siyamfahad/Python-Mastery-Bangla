



# #Image Processing In Python

# from PIL import Image,ImageFilter

# img = Image.open('images\\audi.jpg')

# # img.show()
# print(img.size)
# print(img.height)
# print(img.width)

# rotated = img.rotate(45)
# # rotated.show()

# cropped = img.crop((30,30,500,500))

# # cropped.show()
# filtered = img.filter(ImageFilter.BLUR)

# # filtered.show()
# b = img.convert("L")
# b.show()
# print(img.mode)

import sys 
import os
from PIL import Image
images_folder = sys.argv[1]
output_folder = sys.argv[2]

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for  file in os.listdir(images_folder):
    img = Image.open(f"{images_folder}{file}")
    clean_name = os.path.splitext(file)[0]
    img.save(f"{output_folder}{clean_name}.png")
    print("done!")
