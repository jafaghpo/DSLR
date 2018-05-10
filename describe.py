#!/usr/bin/env python
# coding: utf-8

__author__ = 'John Afaghpour'

import sys
from pandas import read_csv


def main():

	if len(sys.argv) != 2:
		print 'usage: ' + __file__ + ' file.csv'
		sys.exit()
	data = read_csv(sys.argv[1])
	print data

if __name__ == '__main__':
	main()