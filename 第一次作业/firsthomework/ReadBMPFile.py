# -*- coding: UTF-8 -*-
from struct import unpack


# 读取并存储 bmp 文件
class ReadBMPFile:
    def __init__(self, filePath):
        file = open(filePath, "rb")
        # 读取 bmp 文件的文件头    14 字节
        # 其中<表示Bmp是小端，h表示用16进制表示
        self.bfType = unpack("<h", file.read(2))[0]  # 0x4d42 对应BM 表示这是Windows支持的位图格式
        self.bfSize = unpack("<i", file.read(4))[0]  # 位图文件大小
        self.bfReserved1 = unpack("<h", file.read(2))[0]  # 保留字段 必须设为 0
        self.bfReserved2 = unpack("<h", file.read(2))[0]  # 保留字段 必须设为 0
        self.bfOffBits = unpack("<i", file.read(4))[0]  # 偏移量 从文件头到位图数据需偏移多少字节（位图信息头、调色板长度等不是固定的，这时就需要这个参数了）
        # 读取 bmp 文件的位图信息头 40 字节
        self.biSize = unpack("<i", file.read(4))[0]  # 所需要的字节数
        self.biWidth = unpack("<i", file.read(4))[0]  # 图像的宽度 单位 像素
        self.biHeight = unpack("<i", file.read(4))[0]  # 图像的高度 单位 像素
        self.biPlanes = unpack("<h", file.read(2))[0]  # 说明颜色平面数 总设为 1
        self.biBitCount = unpack("<h", file.read(2))[0]  # 说明比特数

        self.biCompression = unpack("<i", file.read(4))[0]  # 图像压缩的数据类型
        self.biSizeImage = unpack("<i", file.read(4))[0]  # 图像大小
        self.biXPelsPerMeter = unpack("<i", file.read(4))[0]  # 水平分辨率
        self.biYPelsPerMeter = unpack("<i", file.read(4))[0]  # 垂直分辨率
        self.biClrUsed = unpack("<i", file.read(4))[0]  # 实际使用的彩色表中的颜色索引数
        self.biClrImportant = unpack("<i", file.read(4))[0]  # 对图像显示有重要影响的颜色索引的数目
        self.bmp_data = []
        # # 对前面得到的结果进行输出
        # print("self.bfType", self.bfType)
        # print("self.bfSize", self.bfSize)
        # print("self.bfReserved1", self.bfReserved1)
        # print("self.bfReserved2", self.bfReserved2)
        # print("self.bfOffBits", self.bfOffBits)
        #
        # print("self.biSize", self.biSize)
        # print("self.biWidth", self.biWidth)
        # print("self.biHeight", self.biHeight)
        # print("self.biPlanes", self.biPlanes)
        # print("self.biBitCount", self.biBitCount)
        # print("self.biCompression", self.biCompression)
        # print("self.biSizeImage", self.biSizeImage)
        # print("self.biXPelsPerMeter", self.biXPelsPerMeter)
        # print("self.biYPelsPerMeter", self.biYPelsPerMeter)
        # print("self.biClrUsed", self.biClrUsed)
        # print("self.biClrImportant", self.biClrImportant)

        for height in range(self.biHeight):
            bmp_data_row = []
            # 四字节填充位检测
            count = 0
            for width in range(self.biWidth):
                bmp_data_row.append(unpack("<B", file.read(1))[0])
                count = count + 3
            # bmp 四字节对齐原则
            while count % 4 != 0:
                file.read(1)
                count = count + 1
            self.bmp_data.append(bmp_data_row)
        self.bmp_data.reverse()
        file.close()
        # print("self.bmp_data", self.bmp_data)

