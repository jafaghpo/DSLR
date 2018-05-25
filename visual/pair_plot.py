#!/usr/bin/env python
# coding: utf-8

__author__ = 'John Afaghpour'

import sys
import csv
import warnings
import matplotlib.pyplot as plt


def check_empty(row):

	for elem in row:
		if not elem:
			return True
	return False


def organize_data(file):

	houses_idx = {'Gryffindor':0, 'Slytherin':1, 'Ravenclaw':2, 'Hufflepuff':3}
	first = False
	for row in file:
		if first == False:
			features = row[6:]
			data = [[] for x in xrange(len(features))]
			for i, elem in enumerate(features):
				data[i] = [[] for x in xrange(4)]
			first = True
			continue
		house = row[1]
		row = row[6:]
		if check_empty(row):
			continue
		for i, elem in enumerate(row):
			elem = float(elem)
			data[i][houses_idx[house]].append(elem)
	return data, features


def display(data, features):

	i = 1
	Y = 0
	fig = plt.figure(figsize=(25, 15), facecolor='beige')
	fig.canvas.set_window_title('[Pair Plot] Quelles caracteristiques choisir pour la regression logistique ?')
	houses = ['Gryffindor', 'Slytherin', 'Ravenclaw', 'Hufflepuff']
	color = {'Gryffindor':'crimson', 'Slytherin':'green', 'Ravenclaw':'teal', 'Hufflepuff':'goldenrod'}
	for featureY in features:
		X = 0
		for featureX in features:
			plt.subplot(13, 13, i)
			plt.xticks([], [])
			plt.yticks([], [])
			if X == 0:
				plt.ylabel(featureY[:10])
			if Y == 12:
				plt.xlabel(featureX[:16])
			if featureY != featureX:
				for idx, house in enumerate(data[Y]):
					plt.scatter(data[Y][idx], data[X][idx], color=color[houses[idx]], alpha=0.5)
			else:
				for idx, house in enumerate(data[Y]):
					plt.hist(house, 20, facecolor=color[houses[idx]], alpha=0.5)
			i += 1
			X += 1
		Y += 1
	plt.subplots_adjust(top=0.9, bottom=0.1, left=0.1, right=0.9, hspace=0.5, wspace=0.3)
	plt.show()


def main():

	warnings.simplefilter(action='ignore', category=FutureWarning)
	if len(sys.argv) != 2:
		print('usage: {} file.csv'.format(__file__))
		sys.exit()
	try:
		fd = open(sys.argv[1], 'r')
	except:
	 	print('error: failed to open {}'.format(sys.argv[1]))
	 	sys.exit()
	file = csv.reader(fd, delimiter=',')
	try:
		data, features = organize_data(file)
	except:
		print('error: invalid data')
		sys.exit()
	display(data, features)

if __name__ == '__main__':
	main()