from PIL import Image
imga = Image.open('b.jpg')
print('图像格式：',imga.format)
print('图像模式：',imga.mode)
print('图像尺寸：',imga.size)
print('图像通道列表；',imga.getbands())
#print('统计直方图列表：',imga.histogram())
imgb = imga.copy()
imgb.thumbnail((224,168))
imgb.show()

# imgc = imga.copy()
# region = imga.crop((50,50,120,120))
# imgc.paste(region,(130,130))
# imgc.show()

img_output = Image.new('RGB',(448,168))
img_output.paste(imgb,(0,0))
img_output.show()
b =imgb.convert('CMYK')
img_output.paste(b,(224,0))
img_output.show()

# flip = b.transpose(Image.FLIP_LEFT_RIGHT)
# img_output.paste(flip,(224,0))
# img_output.show()

# b = imgb.convert('L')
# img_output.paste(b,(224,0))
# img_output.show()

# b = imgb.offset(10)
# img_output.paste(b,(224,0))
# img_output.show()

b = imgb.rotate(45)
img_output.paste(b,(224,0))
img_output.show()

chnls = imgb.split()
b  = Image.merge('RGB',chnls[::-1])
img_output.paste(b,(224,0))
img_output.show()

from  PIL import ImageFilter
b = imgb.filter(ImageFilter.GaussianBlur)
img_output.paste(b,(224,0))
img_output.show()

r,g,b = chnls
r_after = r.point(lambda i:i if i<100 else 255)
b = Image.merge('RGB',(r_after,g,b))
img_output.paste(b,(224,0))
img_output.show()