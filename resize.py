from PIL import Image

image = Image.open('images/img.jpg')
new_image = image.resize((832, 536))  #resizing as needed in pixels
new_image.save('images/img_resized.jpg')

print(image.size) 
print(new_image.size) 
