# mlib/create_main.py
from mlib.utils import write_file, join_path
from mlib.templates import main_script_template

def new_main(project_directory: str):
    main_file_path = join_path(project_directory, "main.py")
    write_file(main_file_path, main_script_template)
