"""
通过仿射变换实现旋转和错切
"""
import cv2
import numpy as np
from ReadBMPFile import ReadBMPFile
import matplotlib.pyplot as plt
from math import sin, cos, fabs, radians
if __name__ == "__main__":
    # 传入的文件路径
    filePath1 = r'D:\A_learn\大三下数字图像处理\第一次作业\7.bmp'
    filePath2 = r'D:\A_learn\大三下数字图像处理\第一次作业\elain1.bmp'
    filePath3 = r'D:\A_learn\大三下数字图像处理\第一次作业\lena.bmp'
    # 读取 第一张 BMP 文件
    bmpFile = ReadBMPFile(filePath3)
    data = bmpFile.bmp_data
    Data = np.array(data, dtype=np.uint8)
    h, w = (512, 512)
    # size = (2048, 2048)
    size = (int(h + 1.5*h), w)
    # 实现错切
    Mat_rat = np.array([[1, 1.5, 0], [0, 1, 0]])
    # pic_shear = cv2.warpAffine(Data, Mat_rat, size, flags=cv2.INTER_CUBIC)
    # plt.imshow(pic_shear, cmap="gray")
    # plt.title("shear_elain1")
    # plt.savefig('./shear_elain1.jpg')
    pic_shear2 = cv2.warpAffine(Data, Mat_rat, size, flags=cv2.INTER_CUBIC)
    plt.imshow(pic_shear2, cmap="gray")
    plt.title("shear_lena")
    plt.savefig('./shear_lena.jpg')

    # 实现旋转
    angle = 30  # 定义旋转角度
    M = cv2.getRotationMatrix2D((w / 2, h / 2), angle, 1)
    newW = int(h * fabs(sin(radians(angle))) + w * fabs(cos(radians(angle))))
    newH = int(w * fabs(sin(radians(angle))) + h * fabs(cos(radians(angle))))
    M[0, 2] += (newW - w) / 2
    M[1, 2] += (newH - h) / 2

    # pic_rot = cv2.warpAffine(Data, M, (newW, newH), borderValue=(255, 255, 255))
    # plt.imshow(pic_rot, cmap="gray")
    # plt.title("rotation_elain1")
    # plt.savefig('./rotation_elain1.jpg')

    pic_rot2 = cv2.warpAffine(Data, M, (newW, newH), borderValue=(255, 255, 255))
    plt.imshow(pic_rot2, cmap="gray")
    plt.title("rotation_lena")
    plt.savefig('./rotation_lena.jpg')



