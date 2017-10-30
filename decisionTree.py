#viz code 

from sklearn.externals.six import StringIO
import pydotplus
dot_data = StringIO()

graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_pdf("iris.pdf")

