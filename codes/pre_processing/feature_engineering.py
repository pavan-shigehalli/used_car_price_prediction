#!/usr/bin/env python3
"""
Contains methods for feature engineering
"""

import csv
import sys
import os
import logging
from logging.handlers import TimedRotatingFileHandler

from .__init__ import Data


class FeatureEllimintation:
    """
    Contains methods to delete the redundant features
    """

    def __init__(self, data_file, batch_size=None, log=True):
        self.logger = log
        self.data_file = data_file
        self.batch_size = batch_size

    @property
    def logger(self):
        """ Set the logger """
        return self._logger

    @logger.setter
    def logger(self, log):
        format = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

        file_handler = TimedRotatingFileHandler(Data.FEATURE_ELLIMINATION_LOG, when='midnight')
        file_handler.setFormatter(format)

        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.DEBUG)
        console_handler.setFormatter(format)

        self._logger = logging.getLogger()
        self._logger.setLevel(logging.DEBUG)
        self._logger.addHandler(console_handler)

        if log:
            self._logger.addHandler(file_handler)

    @property
    def data_file(self):
        """ check if the file exists """
        return self._data_file

    @data_file.setter
    def data_file(self, file):
        if os.path.isfile(file):
            self._data_file = file
        else:
            self.logger.error(f"The file {file} does not exist")
            raise OSError(f"The file {file} does not exist")

    @property
    def batch_size(self):
        """ Sets the batch size """
        return self._batch_size

    @batch_size.setter
    def batch_size(self, size):
        if size :
            self._batch_size = size
        else:
            self._batch_size = self._get_file_length(self.data_file)

        self.logger.info(f"Batch size set to : {self._batch_size}")

    @staticmethod
    def _get_file_length(input_file):
        # Get the number of lines in a file
        with open(input_file, 'r') as file:
            for i, _ in enumerate(file):
                pass

        return i + 1

    def elliminate(self):
        """
        Returns a list of removable columns from the data set
        """

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
