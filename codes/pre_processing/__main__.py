#!/usr/bin/env python3
"""
User endpoint
"""

import argparse
import os

from .randomize import Randomize
from .feature_engineering import FeatureEllimintation


def randomize_data(input_directory, output_directory):
    """
    Passes the parametes to randomize.py
    """
    for file in os.listdir(input_directory):
        input_file = os.path.join(input_directory, file)
        output_file = os.path.join(output_directory, file)

        Rand = Randomize(input_file, output_file)
        Rand.randomize()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-R','--randomize',
                        metavar=('input_directory', 'output_directory'),
                        nargs=2, type=str, dest='data_directory' )

    parser.add_argument('-e','--elliminate',
                        action='store_true', dest='feat_ell')

    args = parser.parse_args()
    if args.data_directory:
        randomize_data(args.data_directory[0], args.data_directory[1])
    elif args.feat_ell:
        FE = FeatureEllimintation(data_file='data/processed_data/audi.csv')
