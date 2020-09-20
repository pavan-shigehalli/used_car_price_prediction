#!/usr/bin/env python3
"""
User endpoint
"""

import argparse
import os

from .randomize import Randomize


def randomize_data(input_directory, output_directory):
    """
    Passes the parametes to randomize.py
    """
    for input_file in os.listdir(input_directory):
        output_file, _ = os.path.splitext(input_file)
        output_file += '_rand.csv'
        output_file = os.path.join(output_directory, output_file)

        Rand = Randomize(input_file, output_file)
        Rand.randomize()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-R','--randomize',
                        metavar=('input_directory', 'output_directory'),
                        nargs=2, type=str, dest='data_directory' )

    args = parser.parse_args()
    if args.data_directory:
        randomize_data(args.data_directory[0], args.data_directory[1])
