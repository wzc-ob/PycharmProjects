from PIL import Image

def div2(v):
    return v//2
imga = Image.open('a.jpg')
imga.resize((500,500)).save('d.jpg')
Image.eval(imga,div2).show()
