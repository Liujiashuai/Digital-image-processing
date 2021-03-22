"""
实现最近邻法，线性插值
"""
import numpy as np
import matplotlib.pyplot as plt
from ReadBMPFile import ReadBMPFile

def nearest_neighbor_resize(img, new_w, new_h):
    # 定义最近邻
    h, w = img.shape[0], img.shape[1]
    # new image with rgb channel
    ret_img = np.zeros(shape=(new_h, new_w, 3), dtype='uint8')
    # scale factor
    s_h, s_c = (h * 1.0) / new_h, (w * 1.0) / new_w

    # insert pixel to the new img
    for i in range(new_h):
        for j in range(new_w):
            p_x = int(j * s_c)
            p_y = int(i * s_h)

            ret_img[i, j] = img[p_y, p_x]

    return ret_img

def saturate(num):
    # 定义越界函数
    if num >= 512:
        return 511
    if num <= 0:
        return 0
    return num

def BilinearInterpolation(img, new_h, new_w):
    # 实现双线性
    height, width = img.shape
    outimg = np.zeros(shape=(new_h, new_w))
    for i in range(new_h):
        sy = i*height/new_h
        i_sy = int(sy)
        j_sy = sy-i_sy
        for j in range(new_w):
            sx = j*width/new_w
            i_sx = int(sx)
            j_sx = sx-i_sx
            c1 = (1-j_sy)*(1-j_sx)
            c2 = j_sy*(1-j_sx)
            c3 = j_sy * j_sx
            c4 = (1-j_sy) * j_sx
            # Sji_x = saturate(int(np.round((j+0.5)*width/shape[1]-0.5)), width-1)
            # Sji_y = saturate(int(np.round((i+0.5)*height/shape[0]-0.5)), height-1)
            # Sji1_x = saturate(int(np.round((j+0.5)*width/shape[1]-0.5)), width-1)
            # Sji1_y = saturate(int(np.round((i+1.5)*height/shape[0]-0.5)), height-1)
            # Sj1i1_x = saturate(int(np.round((j+1.5)*width/shape[1]-0.5)), width-1)
            # Sj1i1_y = saturate(int(np.round((i+1.5)*height/shape[0]-0.5)), height-1)
            # Sj1i_x = saturate(int(np.round((j+1.5)*width/shape[1]-0.5)), width-1)
            # Sj1i_y = saturate(int(np.round((i+0.5)*height/shape[0]-0.5)), height-1)

            Sji_x = saturate(int(np.round((j+0.5)*width/new_w-0.5)))
            Sji_y = saturate(int(np.round((i+0.5)*height/new_h-0.5)))
            Sji1_x = saturate(int(np.round((j+0.5)*width/new_w-0.5)))
            Sji1_y = saturate(int(np.round((i+1.5)*height/new_h-0.5)))
            Sj1i1_x = saturate(int(np.round((j+1.5)*width/new_w-0.5)))
            Sj1i1_y = saturate(int(np.round((i+1.5)*height/new_h-0.5)))
            Sj1i_x = saturate(int(np.round((j+1.5)*width/new_w-0.5)))
            Sj1i_y = saturate(int(np.round((i+0.5)*height/new_h-0.5)))
            outimg[i, j] = int(img[Sji_y, Sji_x]*c1 + img[Sji1_y, Sji1_x]*c2 + img[Sj1i1_y, Sj1i1_x]*c3 + img[Sj1i_y, Sj1i_x]*c4)
    return np.array(outimg, dtype=np.uint8)


if __name__ == "__main__":
    # 传入的文件路径
    filePath1 = r'D:\A_learn\大三下数字图像处理\第一次作业\7.bmp'
    filePath2 = r'D:\A_learn\大三下数字图像处理\第一次作业\elain1.bmp'
    filePath3 = r'D:\A_learn\大三下数字图像处理\第一次作业\lena.bmp'
    # 读取 第一张 BMP 文件
    bmpFile = ReadBMPFile(filePath3)
    data = bmpFile.bmp_data
    Data = np.array(data, dtype=np.uint8)
    new_w, new_h = 2048, 2048  # 定义新的长宽

    # 使用最近邻绘制图像
    zoom_nn_pic = nearest_neighbor_resize(Data, new_w, new_h)
    plt.imshow(zoom_nn_pic, cmap="gray")
    plt.title("nearest_neighbor_resize")
    plt.savefig('./nearest_neighbor_resize.jpg')

    # # 使用双线性插值
    # zoom_bi_pic = BilinearInterpolation(Data, new_h, new_w)
    # plt.imshow(zoom_bi_pic, cmap="gray")
    # plt.title("BilinearInterpolation")
    # plt.savefig('./BilinearInterpolation.jpg')

