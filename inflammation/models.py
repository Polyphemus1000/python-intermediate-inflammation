"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2D array) where each row contains 
inflammation data for a single patient taken over a number of days 
and each column represents a single day across all patients.
"""

import numpy as np


def load_csv(filename):
    """Load a Numpy array from a CSV
    :param filename: Filename of CSV to load
    """
    return np.loadtxt(fname=filename, delimiter=',')

def load_json(filename):
    """Load a numpy array from a JSON document.
    
    Expected format:
    [
      {
        "observations": [0, 1]
      },
      {
        "observations": [0, 2]
      }    
    ]
    :param filename: Filename of CSV to load
    """
    with open(filename, 'r', encoding='utf-8') as file:
        data_as_json = json.load(file)
        return [np.array(entry['observations']) for entry in data_as_json]


def daily_mean(data):
    """Calculate the daily mean of a 2d inflammation data array."""
    return np.mean(data, axis=0)


def daily_max(data):
    """Calculate the daily max of a 2d inflammation data array."""
    return np.max(data, axis=0)


def daily_min(data):
    """Calculate the daily min of a 2d inflammation data array."""
    return np.min(data, axis=0)

def patient_normalise(data):
    """Normalise patient data from a 2D inflammation data array."""
    if not isinstance (data,np.ndarray):
        raise TypeError('Data is expected to be of type ndarray')
    #if data.shape != (30,60):
    is_zero = data < 0
    if is_zero.any():
        raise ValueError(np.where(is_zero))
    maxvalue = np.max(data, axis=0)
    return data / maxvalue[:, np.newaxis]


def pure_daily_standard_deviation(data):
    
    means_by_day = map(daily_mean, data)
    means_by_day_matrix = np.stack(list(means_by_day))

    daily_standard_deviation = np.std(means_by_day_matrix, axis=0)

    return daily_standard_deviation


def analyse_data(DataSource):
    """Calculates the standard deviation by day between datasets.

    Gets all the inflammation data from CSV files within a directory,
    works out the mean inflammation value for each day across all datasets,
    then plots the graphs of standard deviation of these means."""
    
    data = DataSource.load_information_data()

    std = pure_daily_standard_deviation(data)

    return std
