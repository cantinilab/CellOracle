# -*- coding: utf-8 -*-

import sys
import re
import warnings
import logging

from . import utility, data

from . import motif_analysis

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)


# Make sure that DeprecationWarning within this package always gets printed
warnings.filterwarnings('always', category=DeprecationWarning,
                        module=r'^{0}\.'.format(re.escape(__name__)))


logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)


# Make sure that DeprecationWarning within this package always gets printed
warnings.filterwarnings('always', category=DeprecationWarning,
                        module=r'^{0}\.'.format(re.escape(__name__)))

__copyright__    = 'Copyright (C) 2020 Kenji Kamimoto'
__license__      = 'Apache License Version 2.0'
__author__       = 'Kenji Kamimoto'
__author_email__ = 'kamimoto@wustl.edu'
__url__          = 'https://github.com/morris-lab/CellOracle'


__all__ = ["utility", "motif_analysis", "data"]
