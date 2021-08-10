import os
import numpy as np
from PIL import Image
from PIL import ImageEnhance
import cv2

def Enhance_Brightness(image):
    # 变亮，增强因子为0.0将产生黑色图像,为1.0将保持原始图像。
    # 亮度增强
    enh_bri = ImageEnhance.Brightness(image)
    brightness = np.random.uniform(1.4, 1.6)
    image_brightened = enh_bri.enhance(brightness)
    # image_brightened.show()
    return image_brightened


def Enhance_Color(image):
    # 色度,增强因子为1.0是原始图像
    # 色度增强
    enh_col = ImageEnhance.Color(image)
    color = np.random.uniform(0.9,2.6)
    image_colored = enh_col.enhance(color)
    # image_colored.show()
    return image_colored


def Enhance_contrasted(image):
    # 对比度，增强因子为1.0是原始图片
    # 对比度增强
    enh_con = ImageEnhance.Contrast(image)
    contrast = np.random.uniform(0.6, 1.6)
    image_contrasted = enh_con.enhance(contrast)
    # image_contrasted.show()
    return image_contrasted


def Enhance_sharped(image):
    # 锐度，增强因子为1.0是原始图片
    # 锐度增强
    enh_sha = ImageEnhance.Sharpness(image)
    sharpness = np.random.uniform(0.4, 4)
    image_sharped = enh_sha.enhance(sharpness)
    # image_sharped.show()
    return image_sharped


def Add_pepper_salt(image):
    # 增加椒盐噪声
    img = np.array(image)
    rows, cols, _ = img.shape

    random_int = np.random.randint(500, 1000)
    for _ in range(random_int):
        x = np.random.randint(0, rows)
        y = np.random.randint(0, cols)
        if np.random.randint(0, 2):
            img[x, y, :] = 255
        else:
            img[x, y, :] = 0
    img = Image.fromarray(img)
    img.show()
    return img

def letterbox_image(image, size):
    # 对图片进行resize，使图片不失真。在空缺的地方进行padding
    iw, ih = image.size
    w, h = size
    scale = min(w/iw, h/ih)
    nw = int(iw*scale)
    nh = int(ih*scale)

    image = image.resize((nw,nh), Image.BICUBIC)
    new_image = Image.new('RGB', size, (128,128,128))
    new_image.paste(image, ((w-nw)//2, (h-nh)//2))
    new_image = letterbox_image(new_image, [416, 416])
    return new_image

def Enhance(image_path, change_bri=1, change_color=1, change_contras=1, change_sha=1, add_noise=1):
    # 读取图片
    image = Image.open(image_path)
    # image.show()
    if change_bri == 1:
        image = Enhance_Brightness(image)
    if change_color == 1:
        image = Enhance_Color(image)
    if change_contras == 1:
        image = Enhance_contrasted(image)
    if change_sha == 1:
        image = Enhance_sharped(image)
    if add_noise == 1:
        image = Add_pepper_salt(image)
    # image.save("0.jpg")

path = '/home/meroke/图片/test/Complete/Image/1.jpg'
Enhance(path)
