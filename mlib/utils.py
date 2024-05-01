import os

def create_directory(path: str):
    """Create a directory if it doesn't exist."""
    try:
        os.mkdir(path)
        print(f"Directory '{path}' created successfully.")
    except FileExistsError:
        print(f"Directory '{path}' already exists.")

def write_file(path: str, content: str):
    """Write content to a file, creating it if it doesn't exist."""
    if os.path.exists(path):
        print(f"File '{path}' already exists.")
    else:
        try:
            with open(path, "w") as f:
                f.write(content)
            print(f"File '{path}' created successfully.")
        except Exception as e:
            print(f"Error writing '{path}': {e}")

def get_cwd():
    return os.getcwd()

def join_path(*args):
    """Join path components."""
    return os.path.join(*args)
