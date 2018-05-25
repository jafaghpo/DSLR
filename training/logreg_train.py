#!/usr/bin/env python
# coding: utf-8

__author__ = 'John Afaghpour'

import csv
import sys
from tools import *


def write_theta(theta):

	path = get_path(__file__, 'theta.csv')
	fd = open(path, 'w')
	for elem in theta:
		for i, value in enumerate(elem):
			if i != 0:
				fd.write(',')
			fd.write(str(value))
		fd.write('\n')
	fd.close()


def gradient_descent(x, y, m, n, iteration=3):

	theta = [[0.0 for a in range(n)] for b in range(4)]
	lr = 3.0
	for _ in range(iteration):
		for house in range(4):
			sums = [0.] * n
			for i in range(m):
				for j in range(n):
					sums[j] += (h(theta[house], x[i]) - (y[i] == house)) * x[i][j]
			for k in range(n):
				theta[house][k] -= (lr / m) * sums[k]
	return theta


def main():

	path = get_path(__file__, '../dataset/dataset_train.csv')
	try:
		fd = open(path, 'r')
	except:
	 	exit('error: failed to open {}'.format(path))
	file = csv.reader(fd, delimiter=',')
	try:
		x, y, m, n = get_data(file, [f for f in all_features if f in ignored_features])
	except:
		exit('error: invalid data')
	theta = gradient_descent(x, y, m, n)
	write_theta(theta)
	fd.close()

if __name__ == '__main__':
	main()