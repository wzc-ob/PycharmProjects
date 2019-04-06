from PIL import Image
imga = Image.open('b.jpg')
imgb = Image.open('c.jpg')
Image.blend(imga,imgb,0.5).show()