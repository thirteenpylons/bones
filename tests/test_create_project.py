import pytest
import os
import tempfile
from mlib.create_project import new_project
from mlib.utils import join_path

def test_new_project():
    with tempfile.TemporaryDirectory() as temp_dir:
        new_project(temp_dir)

        path = join_path(os.getcwd(), temp_dir)

        assert os.path.exists(path)

        # Cleanup is automatic

if __name__ == "__main__":
    pytest.main()
