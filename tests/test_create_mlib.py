import sys
import os
import tempfile
import shutil

project_root = os.path.dirname(os.path.dirname(__file__))
sys.path.append(project_root)

from mlib.create_mlib import new_mlib
from mlib.utils import join_path

import pytest

def test_create_mlib():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        new_mlib(temp_dir)

        mlib_path = join_path(temp_dir, "mlib")

        assert os.path.exists(mlib_path)

        # Cleanup is automatic for TemporaryDirectory
