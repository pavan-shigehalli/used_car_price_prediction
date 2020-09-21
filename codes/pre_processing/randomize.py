#!/usr/bin/env python3
"""
Contains mehthods to randomize the given data
"""

import os
import csv
import random

class Randomize:
    """
    Performs the following,
    """

    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    @property
    def input_data(self):
        """ check if the file exists """
        return self._input_data

    @input_data.setter
    def input_data(self,file):
        if os.path.isfile(file):
            return file
        else:
            raise OSError(f"The file {file} is not found")

    def randomize(self):
        """
        """
        data_size = self._get_file_length(self.input_file)
        random_list = random.sample(range(0, data_size), data_size)

        with open(self.output_file, 'w') as csvfile:
            csv_writer = csv.writer(csvfile)
            for i in random_list:
                csv_writer.writerow([i])

    @staticmethod
    def _get_file_length(input_file):
        # Get the number of lines in a file
        with open(input_file, 'r') as file:
            for i, _ in enumerate(file):
                pass

        return i + 1
