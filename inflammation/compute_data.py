"""Module containing mechanism for calculating standard deviation between datasets.
"""

import glob
import os
import numpy as np



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
    
