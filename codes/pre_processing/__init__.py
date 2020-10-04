#!/usr/bin/env python3
"""
Contains configuration used by other scripts
"""

import os
import json

class Data:
    """
    Contains relavent data file paths
    """

    with open(os.path.join('configuration', 'config.json'), 'r') as file:
        data = json.load(file)

    RANDOMIZE_LOG = os.sep.join([os.getcwd()]
                                + (data['Logs']['Randomize'].split('/')))

    FEATURE_ELLIMINATION_LOG = os.sep.join([os.getcwd()]
                                           + data['Logs']['Feature Ellimination'].split('/'))
