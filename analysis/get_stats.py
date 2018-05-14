#!/usr/bin/env python
# coding: utf-8

__author__ = 'John Afaghpour'

from math import sqrt


def get_count(feature):

	count = 0
	for elem in feature:
		count += 1 if elem else 0
	if not count:
		print('error: count cannot be null')
		sys.exit()
	return count


def get_mean(feature):

	total = 0
	for elem in feature:
		total += elem if elem else 0
	return total / get_count(feature)


def get_std(feature):

	std = 0
	mean = get_mean(feature)
	for elem in feature:
		std += (elem - mean) * (elem - mean) if elem else 0
	std = std / get_count(feature)
	return sqrt(std)

def get_min(feature):

	minimum = feature[0]
	for elem in feature:
		if elem and elem < minimum:
			minimum = elem
	return minimum


def get_max(feature):

	maximum = feature[0]
	for elem in feature:
		if elem and elem > maximum:
			maximum = elem
	return maximum


def get_percentile(feature, percent):

	feature.sort()
	n = get_count(feature)
	if n % 2 == 1:
		index = int((n + 1) * percent) - 1
		if feature[index]:
			return feature[index]
	else:
		index = int((n) * percent)
		if feature[index - 1] and feature[index]:
			return (feature[index - 1] + feature[index]) / 2