#!/usr/bin/env python

"""Tests for `tictactoe` package."""

import pytest
import builtins
from unittest import mock
from tictactoepy.functions import get_players


def test_get_players():
    """Testing functions.get_players() using mocking"""
    
    with mock.patch.object(builtins, 'input', lambda _: 'Flori'):
        assert get_players() == ['Flori', 'Flori']
