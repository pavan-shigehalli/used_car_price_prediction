#!/usr/bin/env python3
"""
Contains mehthods to randomize the given data
"""

import os
import sys
import random
import linecache
import logging
from logging.handlers import RotatingFileHandler


class Randomize:
    """
    Pre processes the data file
    """

    def __init__(self, log_file=None):
        self.logger = log_file

    @property
    def logger(self):
        """ Sets logger """
        return self._logger

    @logger.setter
    def logger(self,log_file):
        format = logging.Formatter('%(asctime)s:%(levelname)s: %(message)s')

        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.DEBUG)
        console_handler.setFormatter(format)

        self._logger = logging.getLogger()
        self._logger.setLevel(logging.DEBUG)
        self._logger.addHandler(console_handler)

        if log_file:
            file_handler = RotatingFileHandler(log_file, maxBytes=1073741824)
            file_handler.setFormatter(format)
            self._logger.addHandler(file_handler)

    def randomize(self, input_file, output_file):
        """
        Randomly shuffles the input file rows and writes it to the
        specified directory
        """
        if not os.path.exists(input_file):
            self.logger(f"The file {input_file} does not exist")

        input_data_size = self._get_file_length(input_file)
        random_list = random.sample(range(2, input_data_size + 1), input_data_size - 1)

        with open(output_file, 'w') as out_file:
            out_file.write(linecache.getline(input_file, 1))
            for i in random_list:
                out_file.write(linecache.getline(input_file, i))

        # Check the output file integrity
        output_data_size = self._get_file_length(output_file)
        if input_data_size != output_data_size:
            self.logger.warning(f"The {output_file} length:{output_data_size} "
                                f"The {input_file} length:{input_data_size}\n")
        else:
            self.logger.info(f"The file {output_file} is successfully written")

    @staticmethod
    def _get_file_length(input_file):
        # Get the number of lines in a file
        with open(input_file, 'r') as file:
            for i, _ in enumerate(file):
                pass

        return i + 1
