# -*- coding: utf-8 -*-

import sys
import re
import warnings
import logging

from . import utility, data
from . import motif_analysis
from .version import __version__

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)

# Notify users this is the lite fork
logger.info(f"Using celloracle-lite v{__version__} (lightweight fork for ReCoN/HuMMuS)")
logger.info("To install the original CellOracle, please check: https://github.com/morris-lab/CellOracle")


# Make sure that DeprecationWarning within this package always gets printed
warnings.filterwarnings('always', category=DeprecationWarning,
                        module=r'^{0}\.'.format(re.escape(__name__)))


logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)


# Make sure that DeprecationWarning within this package always gets printed
warnings.filterwarnings('always', category=DeprecationWarning,
                        module=r'^{0}\.'.format(re.escape(__name__)))

# Original CellOracle metadata
__copyright__    = 'Copyright (C) 2020 Kenji Kamimoto'
__license__      = 'Apache License Version 2.0'
__author__       = 'Kenji Kamimoto'
__author_email__ = 'kamimoto@wustl.edu'
__url__          = 'https://github.com/morris-lab/CellOracle'

# CellOracle-lite fork information
__fork_name__    = 'celloracle-lite'
__fork_maintainer__ = 'cantinilab'
__fork_url__     = 'https://github.com/cantinilab/celloracle'
__fork_purpose__ = 'Lightweight fork for ReCoN/HuMMuS with reduced dependencies'


__all__ = ["utility", "motif_analysis", "data"]
