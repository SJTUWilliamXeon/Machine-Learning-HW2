import numpy as np 

a=np.array([[1,2,3],[2,3,4]])
#ndim:数组维数的个数.输出结果为2
#shape:数组的维度.这是一个整数的元组，表示每个维度中数组的大小。输出结果为(2,3)
#size:数组元素的总数。输出结果为6.
#dtype:一个描述数组中元素类型。输出结果为int32.
#type():数组类型。输出结果为<class 'numpy.ndarray'>
print(a.ndim,'\n', a.shape,'\n', a.size,'\n', a.dtype,'\n', type(a),'\n')

#zeros:创建0矩阵
#random.randn:返回一个或者一组样本，具有标准正态分布
#dot():返回两数组的点积（内积）
#mean():求数组中的元素平均值
#max(axis=0):求每一列的最大值  axis=1:求每一行的最大值
b=np.zeros((3,4))
c=np.zeros((3,4))
d=np.random.randn(2,3)
e=np.array([[1,2],[2,3],[3,4]])
f=b*2-c*3
g=2*c*f
h=np.dot(a,e)
i=d.mean()
j=d.max(axis=1)
k=a[-1][:2]
print(b,'\n',c,'\n',d,'\n',e,'\n',f,'\n',g,'\n',h,'\n',i,'\n',j,'\n',k,'\n')