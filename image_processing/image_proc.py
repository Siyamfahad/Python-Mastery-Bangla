




from PIL import Image, ImageFilter

img = Image.open("audi.jpg")
new_image = img.convert("L")
new_image.save("new.png",'png')
new_image.show()

print(new_image.mode)