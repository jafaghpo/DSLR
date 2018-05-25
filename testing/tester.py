#!/usr/bin/env python
# coding: utf-8

__author__ = 'John Afaghpour'

import os
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
import warnings


def get_path(file, rel_path):

   script_dir = os.path.dirname(file)
   return os.path.join(script_dir, rel_path)


def main():

   warnings.simplefilter(action='ignore', category=FutureWarning)
   truths = pd.read_csv(get_path(__file__, '../dataset/dataset_truth.csv'), sep=',', index_col=0)
   predictions = pd.read_csv(get_path(__file__, '../houses.csv'), sep=',', index_col=0)
   houses = {'Gryffindor': 0, 'Hufflepuff': 1, 'Ravenclaw': 2, 'Slytherin': 3}
   y_true = truths.replace(houses).as_matrix()
   y_pred = predictions.replace(houses).as_matrix()
   print("Your score on test set: {}%".format(100 * accuracy_score(y_true.reshape((400, )), y_pred.reshape((400, )))))

if __name__ == '__main__':
   main()