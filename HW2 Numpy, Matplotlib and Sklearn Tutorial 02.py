import numpy as np 
import matplotlib.pyplot as plt 
#arange(初始值，结束值（不包括)，步长）
x=np.arange(2,10,0.2)
#r-:红色 g:绿色虚线 b:蓝色
plt.plot(x,x**1.5*.5,'r-',x,np.log(x)*5,'g--',x,x,'b')
plt.show()