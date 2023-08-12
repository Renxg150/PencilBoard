from PIL import Image
import numpy as np


def convert_image_to_array(path):
    im1 = Image.open('111.png').convert("L")
    im2 = im1.copy()
    im2.thumbnail((28, 28))
    im2_array = np.array(im2)
    im2_array = 255 - im2_array
    return im2_array



if __name__ == '__main__':
    im1 = Image.open('111.png').convert("L")
    im2 = im1.copy()
    im2.thumbnail((28,28))
    im2.save('222.png')
    print("im1的大小：",im1.size)
    print("im2的大小：",im2.size)

    im2_array = np.array(im2)
    im2_array = 255 - im2_array

    print(im2_array)