#!/usr/bin/env python3
"""
Contains mehthods to randomize the given data
"""

import os
import random
import linecache
import logging

#from .__init__ import Data

#logging.basicConfig(filename=Data.RANDOMIZE_LOG, level=logging.DEBUG,
#                    format='%(asctime)s:%(levelname)s:%(message)s')

class Randomize:
    """
    Pre processes the data file
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
        Randomly shuffles the input file rows and writes it to the
        specified directory
        """
        input_data_size = self._get_file_length(self.input_file)
        random_list = random.sample(range(2, input_data_size + 1), input_data_size - 1)

        with open(self.output_file, 'w') as out_file:
            out_file.write(linecache.getline(self.input_file, 1))
            for i in random_list:
                out_file.write(linecache.getline(self.input_file, i))

        # Check the output file integrity
        output_data_size = self._get_file_length(self.output_file)
        if input_data_size != output_data_size:
            #logging.warning(f"The {self.output_file} length:{output_data_size} "
            #                f"The {self.input_file} length:{input_data_size}\n")
            pass
        else:
            #logging.info(f"The file {self.output_file} is successfully written")
            pass

    @staticmethod
    def _get_file_length(input_file):
        # Get the number of lines in a file
        with open(input_file, 'r') as file:
            for i, _ in enumerate(file):
                pass

        return i + 1
