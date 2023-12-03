def read_file(file_path: str) -> list:
    with open(file_path, 'r') as f:
        return f.read().splitlines()
