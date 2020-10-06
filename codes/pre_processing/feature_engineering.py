#!/usr/bin/env python3
"""
Contains methods for feature engineering
"""

import csv
import sys
import os
import logging
from logging.handlers import RotatingFileHandler


class FeatureEllimintation:
    """
    Contains methods to delete the redundant features
    """

    def __init__(self, batch_size=None, log_file=None):
        self.logger = log_file
        self.batch_size = batch_size, None

    @property
    def logger(self):
        """ Set the logger """
        return self._logger

    @logger.setter
    def logger(self, log_file):
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

    @property
    def batch_size(self):
        """ Sets the batch size """
        return self._batch_size

    @batch_size.setter
    def batch_size(self, args):
        size, data_file = args
        if data_file:
            if size :
                self._batch_size = size
            else:
                self._batch_size = self._get_file_length(data_file)
        else:
            self._batch_size = None

        self.logger.info(f"Batch size set to : {self._batch_size}")

    @staticmethod
    def _get_file_length(input_file):
        # Get the number of lines in a file
        with open(input_file, 'r') as file:
            for i, _ in enumerate(file):
                pass

        return i + 1

    def elliminate(self, data_file):
        """
        Returns a list of removable columns from the data set
        """
        if not os.path.isfile(data_file):
            self.logger.error(f"The file {data_file} does not exist")
            raise OSError(f"The file {data_file} does not exist")

        self.batch_size = None, data_file


    def t_test(self):
        """
        Statistical T test
        """

    def p_test(self):
        """
        Statistical P test
        """

    def anova_test(self):
        """
        Statistical ANOVA test
        """

    def correlation(self):
        """
        Cross correlation test
        """


class DimensionalityReduction:
    """
    Contains the methods to reduce the input data dimension
    """

    def __init__(self):
        pass

    def pca(self):
        """
        Principal Component analysis
        """

    def lda(self):
        """
        Linear Discriminant Analysis
        """

    def svd(self):
        """
        Singular Value Decomposition
        """
