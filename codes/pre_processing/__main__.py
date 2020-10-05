#!/usr/bin/env python3
"""
User endpoint
"""

import argparse
import os
import json

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

def remove_features():
    """
    Passes paramerts to feature_engineering.py
    """
    with open(os.path.join('configuration', 'config.json'), 'r') as file:
        data = json.load(file)

    log = os.sep.join([os.getcwd()] + data['Logs']['Feature Ellimination'].split('/'))
    data_dir = os.sep.join([os.getcwd()] + data['Data']['Processed']['Directory'].split('/')) + os.sep

    FE = FeatureEllimintation(log_file=log)

    for file in os.listdir(data_dir):
        FE.elliminate(data_dir + file)


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
        remove_features()
    else:
        pass
