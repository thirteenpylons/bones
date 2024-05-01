"""
Parse flag args

Author: Christian M. Fulton
Date: 01.May.24
"""
import configparser
import os


APP_LOCATION = os.path.abspath("bones")

def flags(args):
    """
    When the program is executed, any flags/args will be pushed into here.
    Parse flags and slice args pointing them to the right method.

    List all of the options and usage:
        Usage:
            python3 bones <OPTION> [args]
        Options:
            [-n] [--new]    :: Create a new template for a project
    """
    err = "Usage: python3 bones <OPTION> [args]"

    if len(args) > 1:
        if "-n" in args[:1] or "--new" in args[:1]:
            pass
    else:
        print(err)