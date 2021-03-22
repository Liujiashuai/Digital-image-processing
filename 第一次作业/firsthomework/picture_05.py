"""
使用python 内置函数实现三次插值
"""
import cv2
import numpy as np
from ReadBMPFile import ReadBMPFile
import matplotlib.pyplot as plt
if __name__ == "__main__":
    # 传入的文件路径
    filePath1 = r'D:\A_learn\大三下数字图像处理\第一次作业\7.bmp'
    filePath2 = r'D:\A_learn\大三下数字图像处理\第一次作业\elain1.bmp'
    filePath3 = r'D:\A_learn\大三下数字图像处理\第一次作业\lena.bmp'
    # 读取 第一张 BMP 文件
    bmpFile = ReadBMPFile(filePath3)
    data = bmpFile.bmp_data
    Data = np.array(data, dtype=np.uint8)
    shape = (2048, 2048)  # 定义放大的大小
    pic_cubic = cv2.resize(Data, shape, interpolation=cv2.INTER_CUBIC)
    plt.imshow(pic_cubic, cmap="gray")
    plt.title("INTER_CUBIC")
    plt.savefig('./INTER_CUBIC.jpg')

