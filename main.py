"""
Create a python template generator.

This will generate the desired subdirectories and generic source files required.



"""
import os

from mlib import data


def main() -> None:
    """
    TODO:
        bones will need to be called from outside.
        Create flags to use this:
            bones.py -new <name>

    """
    directory = input("Enter the project name: ")
    create_project(directory)

    # create a main.py file

    # do you need an __init__?

def create_project(project_directory: str) -> None:
        project_location = f"../{project_directory}"

        # create the project directory using input
        try:
            os.mkdir(project_location)
        except FileExistsError:
            print("File already exists.")

def create_mlib(project_directory: str) -> None:
    try:
        os.mkdir(f"{project_directory}/mlib")
    except FileExistsError:
        print("mlib already exists.")

def create_main():
    """
    Main should have 
    """
    try:
        with open("main.py", "a") as raw_file:
            raw_file.write(data.main)
    except Exception:
        print("Something went wrong writing main.py")