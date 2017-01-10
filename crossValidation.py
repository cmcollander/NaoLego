import csv
import numpy as np
from sklearn import tree
from sklearn import grid_search

features = ["blueConns","greenConns","redConns","darkBlueConns","OpenConnectors","Layers","yValue","diff"]

x = []
y = []
with open('data.csv','rb') as csvfile:
	reader = csv.reader(csvfile,delimiter=',',quotechar='|')
	for row in reader:	
		if len(row)==9:
			row = [int(float(n)) for n in row]
			if row[-1]==0 or row[-1]==1:
				x.append(row[:-1])
				y.append(row[-1])

parameters = {'max_depth':range(3,20)}
clf = grid_search.GridSearchCV(tree.DecisionTreeClassifier(),parameters,n_jobs=4)
clf.fit(X=x,y=y)
tree_model = clf.best_estimator_
print (clf.best_score_,clf.best_params_)
