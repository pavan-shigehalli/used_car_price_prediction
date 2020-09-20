#!/usr/bin/env python3
"""
Contains configuration used by other scripts
"""

import os


class Data:
    """
    Contains relavaent data file paths
    """

    parent_directory = os.getcwd()
    data_directory = os.path.join(parent_directory, 'codes', 'data',
                                  'used_car_data')
