#!/usr/bin/env python
# coding: utf-8

__author__ = 'John Afaghpour'

import sys
import csv
import warnings
import matplotlib.pyplot as plt


def check_empty(row):

	for elem in row:
		if not elem:
			return True
	return False


def organize_data(file):

	data = {'Astronomy':[], 'Defense Against the Dark Arts': []}
	first = False
	for row in file:
		if first == False:
			features = row
			first = True
			continue
		if check_empty(row):
			continue
		for i, elem in enumerate(row):
			if features[i] == 'Astronomy' or features[i] == 'Defense Against the Dark Arts':
				elem = float(elem)
				data[features[i]].append(elem)
	return data


def display(data):

	fig = plt.figure(figsize=(25, 15), facecolor='beige')
	fig.canvas.set_window_title('[Scatter Plot] Quelles sont les deux features qui sont semblables ?')
	plt.grid(True)
	plt.ylabel('Astronomy', color='purple')
	plt.xlabel('Defense Against the Dark Arts', color='teal')
	plt.scatter(data['Astronomy'], data['Defense Against the Dark Arts'], color=['purple', 'teal'], alpha=0.5)
	plt.show()


def main():

	warnings.simplefilter(action='ignore', category=FutureWarning)
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
		data = organize_data(file)
	except:
		print('error: invalid data')
		sys.exit()
	display(data)

if __name__ == '__main__':
	main()