from sklearn.datasets import load_iris

iris = load_iris()
print(iris.feature_names)
print(iris.target_names)
print(iris.data[0])
print(iris.target[51])

for i in range(len(iris.target)):
    print("example %d : label %s , feature %s" % (i,iris.target , iris.data[i]))
you are the on
