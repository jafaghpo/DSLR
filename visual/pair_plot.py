#!/usr/bin/env python
# coding: utf-8

__author__ = 'John Afaghpour'

import sys
import pandas as pd
import numpy as np
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt


def main():

	if len(sys.argv) != 2:
		print('usage: {} file.csv'.format(__file__))
		sys.exit()
	data = pd.read_csv(sys.argv[1])
	data['Defense Dark Arts'] = data['Defense Against the Dark Arts']
	data['Magical Creatures'] = data['Care of Magical Creatures']
	ft1 = ['Arithmancy', 'Astronomy', 'Herbology', 'Defense Dark Arts', 'Divination']
	ft2 = ['Muggle Studies', 'Ancient Runes', 'History of Magic', 'Transfiguration']
	ft3 = ['Potions', 'Magical Creatures', 'Charms', 'Flying']
	features = ft1 + ft2 + ft3
	sm = scatter_matrix(data[features], alpha=0.2, figsize=(25, 15), diagonal='hist')
	[s.xaxis.label.set_rotation(45) for s in sm.reshape(-1)]
	[s.yaxis.label.set_rotation(0) for s in sm.reshape(-1)]
	[s.get_yaxis().set_label_coords(-0.5,0.5) for s in sm.reshape(-1)]
	[s.set_xticks(()) for s in sm.reshape(-1)]
	[s.set_yticks(()) for s in sm.reshape(-1)]
	plt.show()

if __name__ == '__main__':
	main()