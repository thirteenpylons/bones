"""

TODO:
    modularize this project
    expand with __main__.py
    extend with an option to --append and add missing to a new project that was already created
        and cloned from github.
    

Author: Christian M. Fulton
Date: 01.May.24
"""
import sys
import os
import argparse

from mlib import create_project, create_mlib, create_main, create_gitignore, create_init, templates, utils


def execute(args=None):
    if args is None:
        args = sys.argv[1:]

    parser = argparse.ArgumentParser(description="Generate a Python project template.")
    parser.add_argument("-n", "--new", type=str, help="Create a new python template for your project.")
    parsed_args, unknown_args = parser.parse_known_args(args)

    if not parsed_args.new:
        print("Project name required. Use -n <name> to specify.")
        return

    create_project.new_project(parsed_args.new)
    create_mlib.new_mlib(parsed_args.new)
    create_main.new_main(parsed_args.new)
    create_init.new_init(parsed_args.new)
    create_gitignore.new_gitignore(parsed_args.new)

    print("Project created successfully with all components.")

if __name__ == "__main__":
    sys.path.append(os.path.dirname(__file__))
    execute()
