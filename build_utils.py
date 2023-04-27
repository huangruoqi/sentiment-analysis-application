import shutil
import os


def copy_datas_to_dist():
    source_dir = "sentiment_analysis/frontend/build"
    destination_dir = "static/sentiment_analysis/"
    if os.path.isdir(destination_dir):
        shutil.rmtree(destination_dir)
    shutil.copytree(source_dir, destination_dir)

if __name__ == "__main__":
    copy_datas_to_dist()