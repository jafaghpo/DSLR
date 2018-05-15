#!/usr/bin/env python
# coding: utf-8

from __future__ import print_function

__author__ = 'John Afaghpour'

import sys
import csv
import numpy as np
import matplotlib.pyplot as plt


def debug_data(data, features):
	
	houses_idx = {'Gryffindor':0, 'Slytherin':1, 'Ravenclaw':2, 'Hufflepuff':3}
	houses_name = ['Gryffindor', 'Slytherin', 'Ravenclaw', 'Hufflepuff']
	for i, row in enumerate(data):
		print('Feature: {}'.format(features[i]))
		for i, elem in enumerate(row):
			print('House: {}'.format(houses_name[i]))
			print(elem)

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
		for i, elem in enumerate(row):
			if elem:
				elem = int(float(elem))
				data[i][houses_idx[house]].append(elem)
	return data, features


def display(data, features):

	fig = plt.figure(figsize=(25, 15), facecolor='beige')
	fig.canvas.set_window_title('[Histogram] Quel cours de Poudlard a une repartition des notes homogenes entre les quatres maisons ?')
	houses_name = ['Gryffindor', 'Slytherin', 'Ravenclaw', 'Hufflepuff']
	c = {'Gryffindor':'crimson', 'Slytherin':'green', 'Ravenclaw':'teal', 'Hufflepuff':'purple'}
	plt.subplot(5, 3, 1)
	plt.text(0.3, 0.1, 'Gryffindor', fontdict={'color':c['Gryffindor'],'size':12})
	plt.text(0.3, 0.3, 'Ravenclaw', fontdict={'color':c['Ravenclaw'],'size':12})
	plt.text(0.3, 0.5, 'Hufflepuff', fontdict={'color':c['Hufflepuff'],'size':12})
	plt.text(0.3, 0.7, 'Slytherin', fontdict={'color':c['Slytherin'],'size':12})
	plt.title('Legend')
	
	for i, feature in enumerate(features):
		plt.subplot(5, 3, i + 2)
		plt.title(feature)
		plt.grid(True)
		for idx, house in enumerate(data[i]):
			plt.hist(house, 50, normed=1, facecolor=c[houses_name[idx]], alpha=0.5)
	plt.subplots_adjust(top=0.9, bottom=0.1, left=0.1, right=0.9, hspace=0.5, wspace=0.3)
	plt.show()


def main():

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