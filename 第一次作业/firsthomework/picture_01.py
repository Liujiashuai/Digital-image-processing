"""
图像比特数是8，是黑白图像，不是RGB
参考：https://blog.csdn.net/rocketeerLi/article/details/84929516
"""
import numpy as np
import sys
from ReadBMPFile import ReadBMPFile
import cv2
# 传入的文件路径
filePath1 = r'D:\A_learn\大三下数字图像处理\第一次作业\7.bmp'
filePath2 = r'D:\A_learn\大三下数字图像处理\第一次作业\elain1.bmp'
filePath3 = r'D:\A_learn\大三下数字图像处理\第一次作业\lena.bmp'
# 读取 第一张 BMP 文件
bmpFile = ReadBMPFile(filePath1)
data = bmpFile.bmp_data
Data = np.array(data, dtype=np.uint8)
# Data = Data[0:256, :]
cv2.imshow("7", Data)
cv2.waitKey(0)  # 解决窗口不显示图像的问题
cv2.destroyAllWindows()

