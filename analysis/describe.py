#!/usr/bin/env python
# coding: utf-8

from __future__ import print_function

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
		if valid_data(elem[0]) and i != 0:
			for j, nb in enumerate(elem):
				data[i][j] = float(nb) if nb else ''
			table.append(data[i])
			category.append(features[i])
	return table, category


def display_data(argument, features, stats):
	
	color = '\033[1;3{}m'
	reset = '\033[0m'
	print('\nFile: {}'.format(argument))
	features = [' '] + features
	for i, elem in enumerate(features):
		print('{}{:^18.16}{}|'.format(color.format(i % 7), elem, reset), end='')
	print('')
	for row in stats:
		for i, elem in enumerate(row):
			print('\033[1;3{}m'.format(i % 7), end='')
			try:
				float(elem)
			except:
				print('{:^18}'.format(elem), end='')
			else:
				print('{:^18.2f}'.format(elem), end='')
			print('\033[0m|', end='')
		print('')


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