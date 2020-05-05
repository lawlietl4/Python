from PIL import Image
import os

img = Image.open(
    'C:/Users/lawliet/source/repos/DevInThirdPartyFW\Python/exercise 3-3/team.jpg')

print(img.size)

x = int(img.size[0] / 2 - 1800)
y = int(img.size[1] / 2 - 700)

w = x + 500
h = y + 650

box = (x, y, w, h)
img = img.crop(box)

newSize = (100, 100)
img = img.resize(newSize)

img.save('C:/Users/lawliet/source/repos/DevInThirdPartyFW/Python/exercise 3-3/test.png')
