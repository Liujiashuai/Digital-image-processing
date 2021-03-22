"""
计算图像lena的均值方差
"""

import numpy as np
from ReadBMPFile import ReadBMPFile
# 传入的文件路径
filePath1 = r'D:\A_learn\大三下数字图像处理\第一次作业\7.bmp'
filePath2 = r'D:\A_learn\大三下数字图像处理\第一次作业\elain1.bmp'
filePath3 = r'D:\A_learn\大三下数字图像处理\第一次作业\lena.bmp'
# 读取 第一张 BMP 文件
bmpFile = ReadBMPFile(filePath3)
data = bmpFile.bmp_data
Data = np.array(data, dtype=np.uint8)
pic_mean = np.mean(Data)
print("图像的均值为", pic_mean)
pic_var = np.var(Data)
print("图像的方差为", pic_var)
pic_std = np.std(Data)
print("图像的标准差为", pic_std)

