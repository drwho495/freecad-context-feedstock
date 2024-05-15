import os

def find_file(directory, prefix, suffix):
    for root, dirs, files in os.walk(directory):
        for file in files:
            print(file)
            if file.startswith(prefix) and file.endswith(suffix):
                return os.path.join(root, file)
    return None

directory = "./build_artifacts/linux-64"
prefix = "freecad"
suffix = ".conda"

print(find_file(directory, prefix, suffix))
