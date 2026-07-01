import csv
import os

from indexer import create_index_file

def rodar_pipeline_completo():

    create_index_file()

if __name__ == "__main__":
    rodar_pipeline_completo()