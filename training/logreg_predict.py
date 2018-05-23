#!/usr/bin/env python
# coding: utf-8

__author__ = 'John Afaghpour'

import csv
from tools import *


def get_dataset():

	path = get_path(__file__, '../dataset/dataset_test.csv')
	try:
		fd = open(path, 'r')
	except:
	 	exit('error: failed to open {}'.format(path))
	file = csv.reader(fd, delimiter=',')
	#try:
	x, _, size = organize_data(file)
	# except:
	# 	exit('error: invalid data')
	fd.close()
	return x, size


def get_theta():

	path = get_path(__file__, '../theta.csv')
	try:
		fd = open(path, 'r')
	except:
	 	exit('error: failed to open {}'.format(path))
	file = csv.reader(fd, delimiter=',')
	theta = [[] * 3] * 4
	try:
		for i, line in enumerate(file):
			theta[i] = [float(x) for x in line]
	except:
		exit('error: invalid theta values')
	fd.close()
	return theta


def predict(theta, x):

	houses = ['Gryffindor', 'Slytherin', 'Ravenclaw', 'Hufflepuff']
	val = [h(t, x) for t in theta]
	i = val.index(max(val))
	return houses[i]


def write_predictions(theta, x, size):

	path = get_path(__file__, '../houses.csv')
	fd = open(path, 'w')
	fd.write('Index,Hogwarts House\n')
	for i in range(size):
		fd.write(str(i) + ',' + predict(theta, x[i]) + '\n')
	fd.close()


def main():

	x, size = get_dataset()
	theta = get_theta()
	write_predictions(theta, x, size)

if __name__ == '__main__':
	main()