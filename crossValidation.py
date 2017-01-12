import csv
import numpy as np
from sklearn import tree
from sklearn.tree import _tree
from sklearn import model_selection
import os

output_string = ""

def tree_to_code(tree, feature_names):
	global output_string
	output_string = ""
	tree_ = tree.tree_
	feature_name = [
		feature_names[i] if i != _tree.TREE_UNDEFINED else "undefined!"
		for i in tree_.feature
	]
	output_string += "def tree({}):\n".format(", ".join(feature_names))

	def recurse(node, depth):
		global output_string
		indent = "\t" * depth
		if tree_.feature[node] != _tree.TREE_UNDEFINED:
			name = feature_name[node]
			threshold = tree_.threshold[node]
			output_string+= "{}if {} <= {}:\n".format(indent, name, threshold)
			recurse(tree_.children_left[node], depth + 1)
			output_string+= "{}else:  # if {} > {}\n".format(indent, name, threshold)
			recurse(tree_.children_right[node], depth + 1)
		else:
			val = "False"
			if (3*tree_.value[node][0][1])>=(2*tree_.value[node][0][0]):
				val = "True"
			output_string+= "{}return {}\n".format(indent, val)
	recurse(0, 1)
	return output_string

features = ["Conns","OpenConnectors","Layers","yValue","diff"]

x = []
y = []
with open('data.csv','rb') as csvfile:
	reader = csv.reader(csvfile,delimiter=',',quotechar='|')
	for row in reader:	
		if len(row)==6:
			row = [int(float(n)) for n in row]
			if row[-1]==0 or row[-1]==1:
				x.append(row[:-1])
				y.append(row[-1])

# parameters = {'splitter':['best','random'],'min_samples_leaf':range(1,21),'criterion':['gini','entropy'],'max_depth':range(3,20)}
# specify parameters and distributions to sample from
param_dist = {
	"min_samples_leaf": range(1, 51),
	"criterion": ["gini", "entropy"],
	"max_depth": range(1,10)
}
clf = model_selection.GridSearchCV(tree.DecisionTreeClassifier(),param_dist,n_jobs = 8)
clf.fit(x,y)
tree_model = clf.best_estimator_
print (clf.best_score_,clf.best_params_)
st = tree_to_code(tree_model,features)
with open('classifier.py','w') as f:
	f.write(st)

with open("NaoDecisionTree.dot",'w') as f:
	f = tree.export_graphviz(tree_model,out_file=f)

os.system("dot -Tps NaoDecisionTree.dot -o out.pdf")
