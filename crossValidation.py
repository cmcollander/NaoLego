import csv
import numpy as np
from sklearn import tree
from sklearn import grid_search

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

parameters = {'splitter':['best','random'],'min_samples_leaf':range(1,21),'criterion':['gini','entropy'],'max_depth':range(3,20)}
# specify parameters and distributions to sample from
param_dist = {
	"min_samples_leaf": range(1, 51),
	"criterion": ["gini", "entropy"],
	"max_depth": range(1,10)
}
clf = grid_search.GridSearchCV(tree.DecisionTreeClassifier(),param_dist,n_jobs = 8)
clf.fit(x,y)
tree_model = clf.best_estimator_
print (clf.best_score_,clf.best_params_)
