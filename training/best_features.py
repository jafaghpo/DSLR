# Feature Extraction with RFE
from __future__ import print_function
from tools import *
from pandas import read_csv
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression


# load data
path = get_path(__file__, '../dataset/dataset_train.csv')
df = read_csv(path).drop(columns=['Index', 'First Name', 'Last Name', 'Birthday', 'Best Hand'])
df = df.replace(['Gryffindor', 'Slytherin', 'Ravenclaw', 'Hufflepuff'], [0, 1, 2, 3])
df = df.fillna(df.mean())
house = df['Hogwarts House']
df = df.drop(columns=['Hogwarts House'])
# print(df)
# print(house)
array = df.values
#print(array)

X = df.values
Y = house.values
# print(Y)
# feature extraction
model = LogisticRegression()
rfe = RFE(model, 8)
fit = rfe.fit(X, Y)
select = []
print("Num Features: {}".format(fit.n_features_))
for i, f in enumerate(fit.support_):
	if f == True:
		select.append(all_features[i])
print(select)
# print("Selected Features: %s") % fit.support_
print("Feature Ranking: {}".format(fit.ranking_))