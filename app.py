"""
Create a python template generator.

This will generate the desired subdirectories and generic source files required.



"""
import os
import argparse
import sys


def main() -> None:
    """
    TODO:
        bones will need to be called from outside.
        Create flags to use this:
            bones.py -new <name>

    """
    parser = argparse.ArgumentParser(description="Generate a Python project template.")
    parser.add_argument("-new", type=str, help="Name of the project.")

    args= parser.parse_args()

    if args.new:
        create_project(args.new)
        create_main(args.new)
        create_mlib(args.new)

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

def create_main(project_directory: str):
    """
    Main should have 
    """
    main_script = f"""
    def main():
        pass
        
    
    if __name__ == "__main__":
        main()
    """

    try:
        with open(f"{project_directory}/main.py", "a") as raw_file:
            raw_file.write(main_script)
    except Exception as e:
        print(f"Something went wrong writing main.py: {e}")


if __name__ == "__main__":
    sys.path.append(os.path.dirname(__file__))
    main()