"""CSC110 Fall 2020 Course Project, Main

This file contains code that runs the whole project.

"""
from data_center import DataCenter
from data_process import data_process_sealevel, data_process_temperature, generate_report

datacenter = DataCenter()
data_process_temperature(datacenter, 'Vancouver.csv', 'climatedata.ca')
data_process_sealevel(datacenter, 'Pacific Ocean.csv', 'noaa.gov')
generate_report(datacenter)
