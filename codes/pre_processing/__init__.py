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
    RANDOMIZE_LOG = os.path.join(parent_directory, 'codes', 'log',
                                  'RANDOMIZE.log')
