#!/usr/bin/env python
# coding: utf-8

__author__ = 'John Afaghpour'

import math
import numpy as np
import os


N = 3


def get_path(file, rel_path):

	script_dir = os.path.dirname(file)
	return os.path.join(script_dir, rel_path)


def get_mean(data, i):

	total, count = 0, 0
	for elem in data:
		total += elem[i] if elem[i] else 0
		count += 1
	return total / count


def get_max(data, i):

	maximum = data[0][i]
	for elem in data:
		if elem[i] and elem[i] > maximum:
			maximum = elem[i]
	return maximum


def fill_data(data, mean, maximum):

	for i in range(N):
		if not data[i]:
			data[i] = mean[i]
		data[i] /= maximum[i]
	return data


def organize_data(file):

	first = False
	houses = {'Gryffindor':0, 'Slytherin':1, 'Ravenclaw':2, 'Hufflepuff':3}
	data = []
	house = list()
	count = 0
	for i, row in enumerate(file):
		if i == 0:
			continue
		data.append([])
		if row[1]:
			house.append(houses[row[1]])
		row[7] = float(row[7]) if row[7] else row[7]
		row[8] = float(row[8]) if row[8] else row[8]
		row[12] = float(row[12]) if row[12] else row[12]
		data[i - 1].append(row[7])
		data[i - 1].append(row[8])
		data[i - 1].append(row[12])
		count += 1
	maximum = []
	mean = []
	for i in range(N):
		maximum.append(get_max(data, i))
		mean.append(get_mean(data, i))
	for i in range(count):
		data[i] = fill_data(data[i], mean, maximum)
	return data, house, count


def h(theta, x):

	z = 0
	for i in range(N):
		z += (theta[i] * x[i])
	return 1 / (1 + math.exp(-z))