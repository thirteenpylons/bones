"""
TODO:
    -h --help needs fixed
    display functionality. User doesn't know that it completed successfully.
    expand with __main__.py and __init__.py and .gitignore

Author: Christian M. Fulton
Date: 01.May.24
"""


import os
import argparse
import sys

def execute(args):
    if args is None:
        args = sys.argv[1:]

    parser = argparse.ArgumentParser(description="Generate a Python project template.")
    parser.add_argument("-n", "--new", type=str, help="Create a new python template for your project.")
    parsed_args = parser.parse_args()

    if not parsed_args.new:
        print("Project name required. Use -n <name> to specify.")
        return

    create_project(parsed_args.new)
    create_mlib(parsed_args.new)
    create_main(parsed_args.new)
    create_init(parsed_args.new)
    create_gitignore(parsed_args.new)

    print("Project created successfully with all components.")

def create_project(project_directory: str):
    project_location = os.path.join(os.getcwd(), project_directory)

    try:
        os.mkdir(project_location)
        print(f"Project directory '{project_directory}' created successfully.")
    except FileExistsError:
        print(f"Directory {project_directory} already exists.")

def create_mlib(project_directory: str):
    mlib_path = os.path.join(project_directory, "mlib")
    try:
        os.mkdir(mlib_path)
        print("mlib directory created successfully.")
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
            print("main.py created successfully.")
        except Exception as e:
            print(f"Error writing main.py: {e}")

def create_init(project_directory: str):
    init_file_path = os.path.join(f"{project_directory}/mlib", "__init__.py")
    try:
        with open(init_file_path, "w") as f:
            f.write("# Init file for python package.\n")
        print(f"__init__.py created successfully in '{project_directory}'.")
    except Exception  as e:
        print(f"Error writing __init__.py: {e}")

def create_gitignore(project_directory: str):
    gitignore_content = """
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
pip-wheel-metadata/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
.python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
#Pipfile.lock

# PEP 582; used by e.g. github.com/David-OConnor/pyflow
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# os stuff
.DS_Store"""

    gitignore_path = os.path.join(project_directory, ".gitignore")
    try:
        with open(gitignore_path, "w") as f:
            f.write(gitignore_content)
        print(".gitignore created successfully.")
    except Exception as e:
        print(f"Error writing .gitignore: {e}")


if __name__ == "__main__":
    sys.path.append(os.path.dirname(__file__))
    execute()
