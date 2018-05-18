#!/usr/bin/env python
# coding: utf-8

__author__ = 'John Afaghpour'

import sys
import csv
import numpy as np
import pandas as pd


def get_mean(data):

	total, count = 0, 0
	for elem in data:
		total += elem if elem else 0
		count += 1
	return total / count


def get_max(data):

	maximum = data[0]
	for elem in data:
		if elem and elem > maximum:
			maximum = elem
	return maximum


def fill_data(data, mean):

	size = len(data)
	for i in range(size):
		pass

def organize_data(file):

	first = False
	houses = {'Gryffindor':0, 'Slytherin':1, 'Ravenclaw':2, 'Hufflepuff':3}
	data = [[] for x in range(4)]
	for i, row in enumerate(file):
		if i == 0:
			continue
		data[0].append(houses[row[1]])
		data[1].append(float(row[7])) if row[7] else data[1].append(row[7])
		data[2].append(float(row[8])) if row[8] else data[1].append(row[8])
		data[3].append(float(row[12])) if row[12] else data[1].append(row[12])
	maximum = []
	mean = []
	for i, feature in enumerate(data):
		if i == 0:
			continue
		maximum.append(get_max(feature))
		mean.append(get_mean(feature))
	for i in range(4):
		if i == 0:
			continue
		fill_data(data[i], mean[i - 1])
	return data


def main():

	path = 'dataset/dataset_train.csv'
	try:
		fd = open(path, 'r')
	except:
	 	print('error: failed to open {}'.format(path))
	 	sys.exit()
	file = csv.reader(fd, delimiter=',')
	try:
		data = organize_data(file)
	except:
		print('error: invalid data')
		sys.exit()

if __name__ == '__main__':
	main()