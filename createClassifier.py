import csv
from sklearn import tree
from sklearn.tree import _tree

def tree_to_code(tree, feature_names):
	tree_ = tree.tree_
	feature_name = [
		feature_names[i] if i != _tree.TREE_UNDEFINED else "undefined!"
		for i in tree_.feature
	]
	print "def tree({}):".format(", ".join(feature_names))

	def recurse(node, depth):
		indent = "\t" * depth
		if tree_.feature[node] != _tree.TREE_UNDEFINED:
			name = feature_name[node]
			threshold = tree_.threshold[node]
			print "{}if {} <= {}:".format(indent, name, threshold)
			recurse(tree_.children_left[node], depth + 1)
			print "{}else:  # if {} > {}".format(indent, name, threshold)
			recurse(tree_.children_right[node], depth + 1)
		else:
			val = "False"
			if tree_.value[node][0][0]<1:
				val = "True"
			print "{}return {}".format(indent, val)
	recurse(0, 1)

# Lists to hold Feature and Result values
x = []
y = []

with open('data.csv','rb') as csvfile:
	reader = csv.reader(csvfile,delimiter=' ',quotechar='|')
	for row in reader:
		if len(row)==9:
			row = [int(float(n)) for n in row]
			if row[-1]==0 or row[-1]==1: # We only want final values of 0 or 1 as they are the training data
				x.append(row[:-1])
				y.append(row[-1])

clf = tree.DecisionTreeClassifier()
clf = clf.fit(x,y)

tree_to_code(clf,["blueConns","greenConns","redConns","darkBlueConns","OpenConnectors","Layers","yValue","diff"])

with open("NaoDecisionTree.dot",'w') as f:
	f = tree.export_graphviz(clf,out_file=f)
