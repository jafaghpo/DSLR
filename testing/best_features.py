#!/usr/bin/env python
# coding: utf-8

from __future__ import print_function

__author__ = 'John Afaghpour'

import os
from pandas import read_csv
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression


def get_path(file, rel_path):

	script_dir = os.path.dirname(file)
	return os.path.join(script_dir, rel_path)


def main():

	all_features = ['Arithmancy', 'Astronomy', 'Herbology', 'Defense Against the Dark Arts', 'Divination', 'Muggle Studies', 'Ancient Runes', 'History of Magic', 'Transfiguration', 'Potions', 'Care of Magical Creatures', 'Charms', 'Flying']
	path = get_path(__file__, '../dataset/dataset_train.csv')
	df = read_csv(path).drop(columns=['Index', 'First Name', 'Last Name', 'Birthday', 'Best Hand'])
	df = df.replace(['Gryffindor', 'Slytherin', 'Ravenclaw', 'Hufflepuff'], [0, 1, 2, 3])
	df = df.fillna(df.mean())
	house = df['Hogwarts House']
	df = df.drop(columns=['Hogwarts House'])
	array = df.values
	X = df.values
	Y = house.values
	model = LogisticRegression()
	rfe = RFE(model, 8)
	fit = rfe.fit(X, Y)
	select = []
	print("Number of features: {}".format(fit.n_features_))
	print('Features selected: ', end='')
	for i, f in enumerate(fit.support_):
		if f == True:
			select.append(all_features[i])
	print(select)
	print("Feature Ranking: {}".format(fit.ranking_))

if __name__ == '__main__':
	main()