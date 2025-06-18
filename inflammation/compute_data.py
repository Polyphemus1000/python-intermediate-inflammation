"""Module containing mechanism for calculating standard deviation between datasets.
"""

import glob
import os
import numpy as np

import sys
sys.path.append('/home/livphd1/python-intermediate-inflammation')

dir_path = '/home/livphd1/python-intermediate-inflammation/data'

from inflammation import models, views

class CSVDataSource:
    def __init__(self, dir_path):
        self.dir_path = dir_path
    
    def load_information_data(self):
        data_file_paths = glob.glob(os.path.join(self.dir_path, 'inflammation*.csv'))
        if len(data_file_paths) == 0:
            raise ValueError(f"No inflammation data CSV files found in path {self.dir_path}")
        data = map(models.load_csv, data_file_paths)
        print('hello')
        
        return list(data)
    
class JsonSource:
    def __init__(self, dir_path):
        self.dir_path = dir_path
    
    def load_information_data(self):
        data_file_paths = glob.glob(os.path.join(self.dir_path, 'inflammation*.json'))
        if len(data_file_paths) == 0:
            raise ValueError(f"No inflammation data JSON files found in path {self.dir_path}")
        data = map(models.load_json, data_file_paths)
        print('hello')
        
        return list(data)


def analyse_data(DataSource):
    """Calculates the standard deviation by day between datasets.

    Gets all the inflammation data from CSV files within a directory,
    works out the mean inflammation value for each day across all datasets,
    then plots the graphs of standard deviation of these means."""
    
   
    data = DataSource.load_information_data()

    means_by_day = map(models.daily_mean, data)
    means_by_day_matrix = np.stack(list(means_by_day))

    daily_standard_deviation = np.std(means_by_day_matrix, axis=0)

    return daily_standard_deviation