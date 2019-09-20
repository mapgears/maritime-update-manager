"""Util methos for paths"""

from contextlib import contextmanager
import os


@contextmanager
def chdir(dir):
    old_cwd = os.getcwd()
    os.chdir(dir)
    try:
        yield
    finally:
        os.chdir(old_cwd)
