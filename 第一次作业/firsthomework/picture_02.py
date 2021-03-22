"""
把lena 512*512图像灰度级逐级递减8-1显示
"""

import numpy as np
from ReadBMPFile import ReadBMPFile
import matplotlib.pyplot as plt

# 命令行传入的文件路径
filePath1 = r'D:\A_learn\大三下数字图像处理\第一次作业\7.bmp'
filePath2 = r'D:\A_learn\大三下数字图像处理\第一次作业\elain1.bmp'
filePath3 = r'D:\A_learn\大三下数字图像处理\第一次作业\lena.bmp'
# 读取 第一张 BMP 文件
bmpFile = ReadBMPFile(filePath3)
data = bmpFile.bmp_data
Data = np.array(data, dtype=np.uint8)
plt.imshow(Data, cmap="gray")
plt.title("gray_level = 8")
plt.savefig('./gray_level8.jpg')

# img7 = np.floor(Data/2) * 2  # 灰度等级为7
# plt.imshow(img7, cmap="gray")
# plt.title("gray_level = 7")
# plt.savefig('./gray_level7.jpg')
#
# img6 = np.floor(Data/4) * 4  # 灰度等级为6
# plt.imshow(img6, cmap="gray")
# plt.title("gray_level = 6")
# plt.savefig('./gray_level6.jpg')
#
# img5 = np.floor(Data/8) * 8  # 灰度等级为5
# plt.imshow(img5, cmap="gray")
# plt.title("gray_level = 5")
# plt.savefig('./gray_level5.jpg')
#
#
# img4 = np.floor(Data/16) * 16  # 灰度等级为4
# plt.imshow(img4, cmap="gray")
# plt.title("gray_level = 4")
# plt.savefig('./gray_level4.jpg')
#
#
# img3 = np.floor(Data/32) * 32  # 灰度等级为3
# plt.imshow(img3, cmap="gray")
# plt.title("gray_level = 3")
# plt.savefig('./gray_level3.jpg')
#
# img2 = np.floor(Data/64) * 64  # 灰度等级为2
# plt.imshow(img2, cmap="gray")
# plt.title("gray_level = 2")
# plt.savefig('./gray_level2.jpg')
#
# img1 = np.floor(Data/128) * 128  # 灰度等级为1
# plt.imshow(img1, cmap="gray")
# plt.title("gray_level = 1")
# plt.savefig('./gray_level1.jpg')

