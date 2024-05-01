from .utils import join_path


def new_init(project_directory: str):
    init_file_path = join_path(f"{project_directory}/mlib", "__init__.py")
    try:
        with open(init_file_path, "w") as f:
            f.write("# Init file for python package.\n")
        print(f"__init__.py created successfully in '{project_directory}'.")
    except Exception  as e:
        print(f"Error writing __init__.py: {e}")
