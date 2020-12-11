"""CSC110 Fall 2020 Course Project, Data Modeling

This file contains code that generate a math model that show the trend of
temperature and sea level data and makes prediction of future data.

"""
from data_center import DataCenter
import math
from typing import Tuple, List, Dict, Any

possible_as = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]  # smooth constant


def exponential_smoothing_training(y_prime, y, a) -> float:
    """
    Use existing value to predict
    - y: current actual value
    - y_prime: current predict value
    """
    new_y_prime = a * y + (1 - a) * y_prime
    return new_y_prime


def prediction_temperature(datacenter: DataCenter, initial_tries: int) -> Any:
    """ Choose a proper a value from possible as and give out the prediction.
    """
    start = datacenter.get_start_year()[0]
    end = datacenter.get_end_year()
    y_prime = 0
    prediction = {}
    mse = 0
    dict_mse = {}
    total_years = start - end
    prediction[start] = y_prime

    for a in possible_as:
        for year in range(start, end):
            y = datacenter.get_temperature(year)
            prediction[year + 1] = exponential_smoothing_training(y_prime, y, a)
        for year in range(start, end + 1):
            actual = datacenter.get_temperature(year)
            pre = prediction[year]
            mse = mse + (actual - pre) ** 2
        dict_mse[a] = mse / total_years
    return dict_mse


def initialize_y_prime(datacenter: DataCenter, initial_tries: int) -> float:
    start = datacenter.get_start_year()[0]
    sum = 0
    for year in range(start, start + initial_tries):
        sum = sum + datacenter.get_temperature(year)  # Determine starting value for predict value
    y_prime = sum / initial_tries
    return y_prime


def initialize_alpha(datacenter: DataCenter) -> float:
    mse_dict = {}
    pre_dict = {}
    y_prime = initialize_y_prime(datacenter, 3)
    start = datacenter.get_start_year()[0]
    end = datacenter.get_end_year()
    pre_dict[start] = y_prime  # First prediction
    for a in possible_as:
        mse = 0
        for year in range(start, end):
            pre = exponential_smoothing_training(y_prime, y, a)
        y = datacenter.get_temperature(year)

        mse_dict[a] = mse

