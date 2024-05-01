import os
import argparse
import sys

def execute(args):
    parser = argparse.ArgumentParser(description="Generate a Python project template.")
    parser.add_argument("-n", "--new", type=str, help="Name of the project.")
    args = parser.parse_args()

    if not args.new:
        print("Project name required. Use -n <name> to specify.")
        return

    create_project(args.new)
    create_mlib(args.new)
    create_main(args.new)

def create_project(project_directory: str):
    project_location = os.path.join(os.getcwd(), project_directory)

    try:
        os.mkdir(project_location)
    except FileExistsError:
        print(f"Directory {project_directory} already exists.")

def create_mlib(project_directory: str):
    mlib_path = os.path.join(project_directory, "mlib")
    try:
        os.mkdir(mlib_path)
    except FileExistsError:
        print("mlib already exists.")

def create_main(project_directory: str):
    main_script = f"""
def main():
    pass

if __name__ == "__main__":
    main()
"""

    main_file_path = os.path.join(project_directory, "main.py")
    if os.path.exists(main_file_path):
        print(f"main.py already exists in {project_directory}.")
    else:
        try:
            with open(main_file_path, "w") as f:
                f.write(main_script)
        except Exception as e:
            print(f"Error writing main.py: {e}")

if __name__ == "__main__":
    sys.path.append(os.path.dirname(__file__))
    execute()
