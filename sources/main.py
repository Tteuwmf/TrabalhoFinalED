import csv
import os

from pathlib import Path

from indexer import create_index_file
from hash_table import initiate_dict

INDEX_FILE = "indices/notas_index.txt"

def rodar_pipeline_completo():

    arquivo_index = Path(INDEX_FILE)

    if not arquivo_index.is_file():
        create_index_file()
    else:
        print("\nProcessamento já realizado;\n")

    initiate_dict()


if __name__ == "__main__":
    rodar_pipeline_completo()