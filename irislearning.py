import numpy as np
from sklearn.datasets import load_iris
from sklearn import tree

iris = load_iris()
test_idx = [0,50,100]

#training data 
train_target = np.delete(iris.target, test_idx)
train_data = np.delete(iris.data, test_idx, axis=0)


print(test_target) 
print(clf.predict(test_data))

print(test_data[2],test_target[1])
print(iris.feature_names, iris.target_names)




