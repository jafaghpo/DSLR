#!/usr/bin/env python
# coding: utf-8

__author__ = 'John Afaghpour'

import sys
from pandas import read_csv
import csv


def organize_data(file, table=[]):
	
	column = {}
	first = False

	for row in file:
		if not first:
			fields = row
			first = True
			continue
		for i, elem in enumerate(row):
			column[fields[i]] = elem
		table.append(column.copy())
	return table, fields


def valid(column):

	for elem in column:
		try:
			pass


def parse_table(table, fields, stats=[]):

	for category in fields:
		if valid(table[category])
			pass


def main():

	if len(sys.argv) != 2:
		print('usage: {} file.csv'.format(__file__))
		sys.exit()

	try:
		fd = open(sys.argv[1], 'r')
	except:
	 	print('error: failed to open {}'.format(sys.argv[1]))
	 	sys.exit()

	file = csv.reader(fd, delimiter=',')
	table, fields = organize_data(file)
	for elem in table:
		print elem
		break
	fd.close()

if __name__ == '__main__':
	main()