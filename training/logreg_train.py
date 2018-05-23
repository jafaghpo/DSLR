#!/usr/bin/env python
# coding: utf-8

__author__ = 'John Afaghpour'

import csv
import sys
import copy
from tools import *


def write_theta(theta):

	path = get_path(__file__, '../theta.csv')
	fd = open(path, 'w')
	for elem in theta:
		for i, value in enumerate(elem):
			if i != 0:
				fd.write(',')
			fd.write(str(value))
		fd.write('\n')
	fd.close()


def gradient_descent(x, y, m, iteration=100, houses=4):

	theta = [[0. for a in range(N)] for b in range(houses)]
	last = copy.deepcopy(theta)
	lr = 0.7
	sums = [0.] * N
	for _ in range(iteration):
		last = list(sums)
		for house in range(houses):
			for i in range(m):
				yi = 1 if y[i] == house else 0
				for j in range(N):
					sums[j] += (h(theta[house], x[i]) - yi) * x[i][j]
			for idx in range(N):
				theta[house][idx] -= (lr / float(m)) * sums[idx]
	return theta


def main():

	path = get_path(__file__, '../dataset/dataset_train.csv')
	try:
		fd = open(path, 'r')
	except:
	 	exit('error: failed to open {}'.format(path))
	file = csv.reader(fd, delimiter=',')
	try:
		x, y, m = organize_data(file)
	except:
		exit('error: invalid data')
	i = None
	try:
		i = int(sys.argv[1])
	except:
		print('You can pass the number of iteration in argument')
	if i == None:
		theta = gradient_descent(x, y, m)
	else:
		theta = gradient_descent(x, y, m, i)
	write_theta(theta)
	fd.close()

if __name__ == '__main__':
	main()