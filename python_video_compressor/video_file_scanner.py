from pathlib import Path

EXCLUDED_DIR = 'compressed'

class VideoFileScanner:

    def scan(self, path):
        directory_files_list = [str(filename) for filename in Path(path).glob('**/*')]
        return list(filter(lambda path: path.lower().endswith(".mp4") and EXCLUDED_DIR not in path, directory_files_list))
