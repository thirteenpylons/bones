import pytest
import os
from mlib.create_main import new_main
from mlib.utils import join_path

def test_new_main():
    project_directory = os.getcwd()
    new_main(project_directory)

    main_file_path = join_path(project_directory, "main.py")

    assert os.path.exists(main_file_path)

    # Cleanup
    os.remove(main_file_path)

if __name__ == "__main__":
    pytest.main()
