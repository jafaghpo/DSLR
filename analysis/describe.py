#!/usr/bin/env python
# coding: utf-8

__author__ = 'John Afaghpour'

import sys
import csv
from get_stats import *


def valid_data(elem):
	
	if not elem:
		return False
	try:
		float(elem)
	except:
		return False
	return True


def organize_data(file):

	first = False
	for row in file:
		if first == False:
			features = row
			data = [[] for x in xrange(len(features))]
			first = True
			continue
		for i, elem in enumerate(row):
			data[i].append(elem)

	table = []
	category = []
	for i, elem in enumerate(data):
		if valid_data(elem[0]):
			for j, nb in enumerate(elem):
				data[i][j] = float(nb) if nb else ''
			table.append(data[i])
			category.append(features[i])
	return table, category


def display_data(argument, features, data):
	
	print('\nFile: {}'.format(argument))
	print('Features: {}'.format(features))
	print('Stats:')
	for elem in data:
		print(elem)


def get_stats(data, features):

	stats = [['Count'], ['Mean'], ['Std'], ['Min'], ['25%'], ['50%'], ['75%'], ['Max']]
	for feature in data:
		stats[0].append(get_count(feature))
		stats[1].append(get_mean(feature))
		stats[2].append(get_std(feature))
		stats[3].append(get_min(feature))
		stats[4].append(get_percentile(feature, 0.25))
		stats[5].append(get_percentile(feature, 0.50))
		stats[6].append(get_percentile(feature, 0.75))
		stats[7].append(get_max(feature))
	return stats

def main():

	if len(sys.argv) < 2:
		print('usage: {} file.csv'.format(__file__))
		sys.exit()
	del sys.argv[0]
	for argument in sys.argv:
		try:
			fd = open(argument, 'r')
		except:
		 	print('error: failed to open {}'.format(argument))
		 	sys.exit()
		file = csv.reader(fd, delimiter=',')
		data, features = organize_data(file)
		stats = get_stats(data, features)
		display_data(argument, features, stats)
		fd.close()


if __name__ == '__main__':
	main()