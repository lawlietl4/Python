import os

from PIL import Image

if os.path.exists('Lab 3/new_images'):
    print('the directory already exists, overwriting previous contents')
else:
    os.makedirs('Lab 3/new_images')


class imageConverter():
    def gatherImages(self):
        image = os.listdir('images')
        return image

    def imgConvert(self):
        num = 0
        image = os.listdir('images')
        for images in image:
            num += 1
            openImage = Image.open('images/' + images)
            openImage = openImage.transpose(Image.ROTATE_270)
            x = int(openImage.size[0] / 2 - 75)
            y = int(openImage.size[1] / 2 - 75)
            w = x + 150
            h = y + 150
            size = (x, y, w, h)
            openImage = openImage.crop(size)
            newSize = (75, 75)
            openImage = openImage.resize(newSize)
            openImage = openImage.convert('L')
            openImage.save(
                'Lab 3/new_images/' + f'pic0{num:03d}.png')
