import pathlib
import zipfile


def make_archive(filepaths, destination_dir):
    destination_path = pathlib.Path(destination_dir, "compressed.zip")
    with zipfile.ZipFile(destination_path, "w") as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)
