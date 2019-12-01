#To do:use naive bayes (Bernoulli) in sklearn to classify MNIST
from sklearn.naive_bayes import BernoulliNB
from sklearn import metrics
from sklearn.datasets import fetch_mldata
from sklearn.model_selection import train_test_split
mnist =fetch_mldata('MNIST original')

images=mnist.data     
targets=mnist.target 

X=mnist.data / 255. 
Y=mnist.target
train_data,validation_data,train_labels,validation_labels=train_test_split(X[::10],Y[::10],test_size=1000)
#模型训练
bnl=BernoulliNB(binarize=0.5).fit(train_data,train_labels)
#模型评估
training_accuracy=bnl.score(train_data,train_labels)
testing_accuracy=bnl.score(validation_data,validation_labels)
print('training_accuracy:%0.2f%%'%(training_accuracy*100))
print('testing_accuracy:%0.2f%%'%(testing_accuracy*100))