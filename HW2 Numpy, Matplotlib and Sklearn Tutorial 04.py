import numpy as np 
import matplotlib.pyplot as plt 
#定义一个长度为32*32的向量
img=np.arange(0,1,1/32/32)
#将img变换为一个32*32的矩阵，用于表示32*32的图片
img=img.reshape(32,32)

plt.imshow(img,cmap='gray')
plt.show()