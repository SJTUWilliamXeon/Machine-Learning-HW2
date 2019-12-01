import numpy as np 
import matplotlib.pyplot as plt  
def f(x):
    return np.sin(np.pi*x)

x1=np.arange(0,5,0.1)
x2=np.arange(0,5,0.01)
#subplot(211):分割行数，分割列数，在哪个坐标系中画图
#go:g表示颜色，o表示点型
#画图时默认为实线
plt.subplot(211)
plt.plot(x1,f(x1),'go',x2,f(x2-1))

plt.subplot(212)
plt.plot(x2,f(x2),'r--')
plt.show()