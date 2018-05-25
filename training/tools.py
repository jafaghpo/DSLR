#!/usr/bin/env python
# coding: utf-8

__author__ = 'John Afaghpour'

import numpy as np
import os


all_features = ['Arithmancy', 'Astronomy', 'Herbology', 'Defense Against the Dark Arts', 'Divination', 'Muggle Studies', 'Ancient Runes', 'History of Magic', 'Transfiguration', 'Potions', 'Care of Magical Creatures', 'Charms', 'Flying']
ignored_features = ['Arithmancy', 'Astronomy', 'Ancient Runes', 'Transfiguration', 'Potions', 'Care of Magical Creatures']
# selected_features = ['Herbology', 'Defense Against the Dark Arts', 'Divination', 'History of Magic', 'Potions', 'Charms', 'Flying']

def get_path(file, rel_path):

	script_dir = os.path.dirname(file)
	return os.path.join(script_dir, rel_path)


def get_mean(data, i):

	total, count = 0, 0
	for elem in data:
		if elem[i]:
			total += elem[i]
			count += 1
	return total / count


def get_max(data, i):

	maximum = data[0][i]
	for elem in data:
		if elem[i] and elem[i] > maximum:
			maximum = elem[i]
	return maximum


def fill_data(data, n, mean, maximum):

	for i in range(n):
		if not data[i]:
			data[i] = mean[i]
		if maximum[i] != 0:
			data[i] /= maximum[i]
	return data


def get_data(file, ignored=[]):

	ignored_default = ['Index', 'First Name', 'Last Name', 'Birthday', 'Best Hand']
	houses = {'Gryffindor':0, 'Slytherin':1, 'Ravenclaw':2, 'Hufflepuff':3}
	x, y, m = [], [], 0
	for i, line in enumerate(file):
		if i == 0:
			feature = line
			continue
		x.append([])
		x[i - 1].append(1)
		for j, elem in enumerate(line):
			if feature[j] == 'Hogwarts House':
				if line[j]:
					y.append(houses[line[j]])
			elif feature[j] not in ignored and feature[j] not in ignored_default:
				x[i - 1].append(float(elem) if elem else elem)
		m += 1
	maximum, mean, n = [], [], len(x[0])
	for i in range(n):
		maximum.append(get_max(x, i))
		mean.append(get_mean(x, i))
	for i in range(m):
		x[i] = fill_data(x[i], n, mean, maximum)
	return x, y, m, n


def h(theta, x):

	z = sum([theta[i] * x[i] for i in range(len(x))])
	return 1.0 / (1.0 + np.e ** -z)