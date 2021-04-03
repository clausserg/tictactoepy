"""
Unit and regression test for the tictactoepy package.
"""

# Import package, test suite, and other packages as needed
import tictactoepy
import pytest
import sys

def test_tictactoepy_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "tictactoepy" in sys.modules
