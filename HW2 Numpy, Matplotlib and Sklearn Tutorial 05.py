#Based on numpy, Scikit-learn(sklearn) provides a lot of tools for
#machine learning. It is a very powerful machine learning library.
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_mldata 
#download and read mnist
mnist=fetch_mldata('MNIST original')

#'mnist.data' is 70k x 784 array, each row represents the pixels from a 28x28=784 image
#'mnist.target' is 70k x 1 array, each row represents the target class of the corresponding image
images=mnist.data
targets=mnist.target

#归一化
X=mnist.data / 255.
Y=mnist.target

#print the first image of the dataset
img1=X[0].reshape(28,28)
plt.imshow(img1,cmap='gray')
plt.show()

#print the images after simple transformation
img2=1-img1
plt.imshow(img2,cmap='gray')
plt.show()
#transpose:求矩阵转置
img3=img1.transpose()
plt.imshow(img3,cmap='gray')
plt.show()