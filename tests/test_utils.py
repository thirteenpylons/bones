import pytest
import os
from mlib.utils import create_directory, write_file, get_cwd, join_path

def test_create_directory():
    path = join_path(get_cwd(), "test_dir")
    create_directory(path)

    assert os.path.exists(path)

    # Cleanup
    os.rmdir(path)

def test_write_file():
    path = join_path(get_cwd(), "test_file.txt")
    content = "Hello, world!"
    write_file(path, content)

    with open(path, "r") as f:
        data = f.read()

    assert data == content

    # Cleanup
    os.remove(path)

def test_get_cwd():
    assert get_cwd() == os.getcwd()

def test_join_path():
    path = join_path("folder", "subfolder", "file.txt")
    assert path == os.path.join("folder", "subfolder", "file.txt")
