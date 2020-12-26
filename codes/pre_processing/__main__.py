#!/usr/bin/env python3
"""
User endpoint
"""

import argparse
import os
import json

from .randomize import Randomize
from .feature_engineering import FeatureEllimintation


def randomize_data():
    """
    Passes the parametes to randomize.py
    """
    with open(os.path.join('configuration', 'config.json'), 'r') as file:
        data = json.load(file)

    input_directory = os.sep.join([os.getcwd()] + data['Data']['Raw']['Directory'].split('/'))
    output_directory = os.sep.join([os.getcwd()] + data['Data']['Processed']['Directory'].split('/'))
    log = os.sep.join([os.getcwd()] + data['Logs']['Randomize'].split('/'))

    Rand = Randomize(log_file=log)
    for file in os.listdir(input_directory):
        input_file = os.path.join(input_directory, file)
        output_file = os.path.join(output_directory, file)

        Rand.randomize(input_file, output_file)

def remove_features():
    """
    Passes parameters to feature_engineering.py
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
                        action='store_true', dest='randomize' )

    parser.add_argument('-E','--elliminate',
                        action='store_true', dest='feat_ell')

    args = parser.parse_args()
    if args.randomize:
        randomize_data()
    elif args.feat_ell:
        remove_features()
    else:
        pass
