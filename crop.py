from PIL import Image

image = Image.open('images/RC/rc1_resized.jpg')
box = (5,5,10,10)
cropped_image = image.crop(box)
cropped_image.save('cropped_image.jpg')
