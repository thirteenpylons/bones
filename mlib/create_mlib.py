from .utils import create_directory, join_path


def new_mlib(project_directory: str):
    mlib_path = join_path(project_directory, "mlib")
    create_directory(mlib_path)
