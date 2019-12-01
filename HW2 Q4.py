#To do:use support vector machine in sklearn to classify MNIST
from sklearn.svm import LinearSVC
from sklearn import metrics
from sklearn.datasets import fetch_mldata
from sklearn.model_selection import train_test_split
mnist =fetch_mldata('MNIST original')

images=mnist.data     
targets=mnist.target 

X=mnist.data / 255. 
Y=mnist.target
train_data,validation_data,train_labels,validation_labels=train_test_split(X[::10],Y[::10],test_size=1000)
#模型训练(在线性Kernel中，C用于调整惩罚参数，惩罚参数越大，训练集准确率提高，但泛化能力变弱)
lns =LinearSVC(C=0.45)
lns.fit(train_data,train_labels)
#模型评估
predict_labels=lns.predict(train_data)
training_accuracy=metrics.accuracy_score(train_labels,predict_labels)
predict_v_labels=lns.predict(validation_data)
testing_accuracy=metrics.accuracy_score(validation_labels,predict_v_labels)
print('training_accuracy:%0.2f%%'%(training_accuracy*100))
print('testing_accuracy:%0.2f%%'%(testing_accuracy*100))