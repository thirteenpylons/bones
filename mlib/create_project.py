from .utils import join_path, create_directory, get_cwd

def new_project(project_directory: str):
    project_location = join_path(get_cwd(), project_directory)
    try:
        create_directory(project_location)
        print(f"Project directory '{project_directory}' created successfully.")
    except FileExistsError:
        print(f"Directory {project_directory} already exists.")
