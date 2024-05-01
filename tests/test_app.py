import sys
import os

# Add the project root to sys.path
project_root = os.path.dirname(os.path.dirname(__file__))
sys.path.append(project_root)

from app import execute

import pytest
import shutil

def test_execute():
    args = ["-n", "TestAppProject"]
    execute(args)

    assert os.path.exists("TestAppProject")

    # Cleanup
    shutil.rmtree("TestAppProject")

if __name__ == "__main__":
    pytest.main()
