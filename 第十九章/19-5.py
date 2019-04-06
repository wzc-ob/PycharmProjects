from  PIL import Image
from  PIL import ImageChops
imga = Image.open('b.jpg')
imgb = Image.open('b.jpg')
#相加
# ImageChops.add(imga,imgb,1,0).show()
#相减
# ImageChops.subtract(imga,imgb,1,0).show()
#变暗
# ImageChops.darker(imga,imgb).show()
#变亮
# ImageChops.lighter(imga,imgb).show()
#正片叠底
ImageChops.multiply(imga,imgb).show() #
#屏幕
ImageChops.screen(imga,imgb).show()
#反相
ImageChops.invert(imga).show()
#比较
ImageChops.difference(imga,imga).show()