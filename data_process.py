"""CSC110 Fall 2020 Course Project, Data preprocess

This file contains code that preprocesses the temperature and sea level data sets.

"""

import xlwings as xw
import os
import csv
from typing import Any, Tuple, List
from data_center import DataCenter


def data_process_sealevel(data_center: DataCenter, sealevel_file: str, format: str) -> None:
    """Given a sea level files with its format and save the data into the given data_center"""
    sealevel = process_average_sealevel(sealevel_file, data_center.get_current_year())
    if format == 'noaa.gov':
        for row in sealevel:
            data_center.set_sealevel(row[0], row[1])
    else:
        raise FutureImplementation


def data_process_temperature(data_center: DataCenter, temperature_file: str, format: str) -> None:
    """Given a temperature files with its format and save the data into the given data_center"""
    temperature = read_temperature_file(temperature_file, data_center.get_current_year())
    if format == 'climatedata.ca':
        for row in temperature:
            data_center.set_temperature(row[0], row[1])
    else:
        raise FutureImplementation


def read_sealevel_file(filename: str) -> List[List[Any]]:
    """Return the headers and data stored in a csv file with the given filename.

    The return value is a list consisting of year and temperature:
    """
    data = []
    with open(filename) as file:
        reader = csv.reader(file)
        line_count = 0
        for row in reader:
            if line_count > 6:
                data.append(process_sealevel_row(row))
            line_count += 1
    return data


def process_sealevel_row(row: List[str]) -> list:
    """Convert a row of temperature data to a list with more appropriate data types.
    """
    if row[1] != str():
        sealevel = row[1]
    elif row[2] != str():
        sealevel = row[2]
    elif row[3] != str():
        sealevel = row[3]
    else:
        sealevel = row[4]

    return [
        int(row[0][0:4]),  # year
        float(sealevel),  # sea level
    ]


def read_temperature_file(filename: str, current_year: int) -> List[List[Any]]:
    """Return the headers and data stored in a csv file with the given filename.

        The return value is a list consisting of year and sea level:
    """
    data = []
    with open(filename) as file:
        reader = csv.reader(file)
        line_count = 0
        for i, row in enumerate(reader):
            if i == 1:
                start_year = int(row[0][0:4])
                data.append(process_temperature_row(row))
                break
        for row in reader:
            if line_count >= 0:
                data.append(process_temperature_row(row))
            if line_count == current_year - start_year - 1:
                break
            line_count += 1
    return data


def process_temperature_row(row: List[str]) -> list:
    """Convert a row of sea level data to a list with more appropriate data types.
    """

    temperature = row[4]

    return [
        int(row[0][0:4]),  # year
        float(temperature),  # sea level
    ]


def process_average_sealevel(filename: str, current_year: int) -> List[List[Any]]:
    """Return a sorted data with one year corresponds to exactly one sea level

    A year with more than one sea level data gets average sea level.
    """
    raw = read_sealevel_file(filename)
    start_year = raw[0][0]
    new_data = []
    for year in range(start_year, current_year + 1):
        sealevel = 0
        num = 0
        for row in raw:
            if row[0] == year:
                sealevel = sealevel + row[1]
                num = num + 1
        sealevel = sealevel / num
        new_data.append([year, sealevel])
    return new_data


class FutureImplementation(Exception):
    """Exception raised when calling a year that is not in the center."""

    def __str__(self) -> str:
        """Return a string representation of this error."""
        return 'This format is not supported yet, more format can be support by future implementation'


def get_directory() -> str:
    """Get current python file directory"""
    current_file_path = __file__
    current_file_dir = os.path.dirname(current_file_path)
    return current_file_dir


def generate_report(datacenter: DataCenter) -> Any:
    """Create an excel file containing complied datasets and save in CSC course project folder"""
    app = xw.App(visible=True, add_book=False)
    wb = app.books.add()
    wb.activate()
    # sht = wb.sheets['Report']
    # sht.range('a1').value = ['This excel file contains processed and predicted data generate in year'
    #                          + str(datacenter.get_current_year())]
    # sht.range('a2').value = ['For CSC110 project usage only']
    # sht.range('a3').value = ['Year', 'Temperature', 'Sea Level']
    # temp = []
    # sea = []
    # for year in range(datacenter.get_start_year(), datacenter.get_end_year() + 1):
    #     temp.append(datacenter.get_temperature(year))
    #     sea.append(datacenter.get_temperature(year))
    # sht.range('a4:a'+str(datacenter.get_end_year() - 4)).options(transpose=True).value = temp
    # sht.range('b4:b' + str(datacenter.get_end_year() - 4)).options(transpose=True).value = sea
    wb.save(get_directory() + '/Compiled Datasets.xlsx')




if __name__ == '__main__':

    import python_ta
    #
    # python_ta.check_all(config={
    #     'extra-imports': ['math'],
    #     'max-line-length': 100
    # })
