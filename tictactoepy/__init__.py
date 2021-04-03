"""
tictactoepy
A tictactoe program written for fun while following the '2021 Complete Python Bootcamp From Zero to Hero in Python' by Jose Portilla, on Udemy
"""

# Add imports here
# from .tictactoepy import *

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
