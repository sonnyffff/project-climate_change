"""CSC110 Fall 2020 Course Project, Data center

This file contains code that creates a dataclass that keeps track of all the data.

"""
from typing import Dict, List, Tuple


class DataCenter:
    """A center that maintains all data.
    """
    # Private Instance Attributes:
    #   - _processed_data: a mapping from year to a list
    #   [temperature, sea level, predicted temperature, predicted sea level].
    #       This represents all the processed data in the system.
    #   - _predicted_data: a mapping from year to a list[temperature, sea level].
    #       This represents all the predicted data in the system.
    _processed_data: Dict[int, List[float]]
    # _predicted_data: Dict[int, List[float]]
    _current_year: int

    def __init__(self) -> None:
        """Initialize a new data center.

        The center starts with no data.
        """
        self._processed_data = {}
        # self._predicted_data = {}
        self._current_year = 2020  # Set to current year

    def get_temperature(self, year: int) -> float:
        """Return the temperature of the given year.
        """
        if year <= self._current_year:
            if year in self._processed_data:
                return self._processed_data[year][0]
            else:
                raise YearNotFoundError

    def get_predict_temperature(self, year: int) -> float:
        if year in self._processed_data:
            return self._processed_data[year][2]
        else:
            raise YearNotFoundError

    def get_sealevel(self, year: int) -> float:
        """"Return the temperature of the given year."""
        if year <= self._current_year:
            if year in self._processed_data:
                return self._processed_data[year][1]
        else:
            raise YearNotFoundError

    def get_predict_sealevel(self, year: int) -> float:
        """

        """
        if year in self._processed_data:
            return self._processed_data[year][3]
        else:
            raise YearNotFoundError

    def set_temperature(self, year: int, temperature: float) -> None:
        """Add the given year corresponds to its temperature to the center.

        Overwrite the data of a year if this year already exist in the center.
        """
        if year not in self._processed_data:
            self._processed_data[year] = [temperature, 'NaN', 'NaN', 'NaN']
        else:
            self._processed_data[year][0] = temperature

    def set_predict_temperature(self, year: int, temperature: float) -> None:
        """

        """
        if year not in self._processed_data:
            self._processed_data[year] = ['NaN', 'NaN', temperature, 'NaN']
        else:
            self._processed_data[year][2] = temperature


    def set_sealevel(self, year: int, sealevel: float) -> None:
        """Add the given year corresponds to its sealevel to the center.

        Overwrite the data of a year if this year already exist in the center.
        """
        if year not in self._processed_data:
            self._processed_data[year] = ['NaN', sealevel, 'NaN', 'NaN']
        else:
            self._processed_data[year][1] = sealevel

    def set_predict_sealevel(self, year: int, sealevel: float) -> None:
        if year not in self._processed_data:
            self._processed_data[year] = ['NaN', 'NaN', 'NaN', sealevel]
        else:
            self._processed_data[year][3] = sealevel

    def get_start_year(self) -> Tuple[int, int]:
        """Return the start year of the data in a tuple (temperature, sea level)"""
        temp = 0
        sea = 0
        for year in self._processed_data:
            if self._processed_data[year][0] != 'NaN':
                temp = year
                break
        for year in self._processed_data:
            if self._processed_data[year][1] != 'NaN':
                sea = year
                break
        return(temp, sea)
        # if self._processed_data != {}:
        #     return (min([year for year in self._processed_data])
        #
        # else:
        #     raise EmptyCenterError

    def get_current_year(self) -> int:
        """Return"""
        return self._current_year

    def get_end_year(self) -> int:
        """Return the end year of the data"""
        if self._processed_data != {}:
            return max([year for year in self._processed_data])
        else:
            raise EmptyCenterError


class YearNotFoundError(Exception):
    """Exception raised when calling a year that is not in the center."""

    def __str__(self) -> str:
        """Return a string representation of this error."""
        return 'year may not be found in this center'


class EmptyCenterError(Exception):
    """Exception raised when calling a year that is not in the center."""

    def __str__(self) -> str:
        """Return a string representation of this error."""
        return 'you may not found year in this center'
