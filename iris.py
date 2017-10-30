from sklearn.datasets import load_iris

iris = load_iris()

for i in range(len(iris.target)):
    print("example %d : label %s , feature %s" % (i,iris.target , iris.data[i]))
