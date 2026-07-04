import csv
import os

from pathlib import Path

from indexer import create_index_file
from hash_table import initiate_dict
from etl import query_notes

INDEX_FILE = "indices/notas_index.txt"

def rodar_pipeline_completo():

    arquivo_index = Path(INDEX_FILE)

    if not arquivo_index.is_file():
        create_index_file()
    else:
        print("\nProcessamento já realizado;\n")

    tabela_hash = initiate_dict()

    data_requisitada = input("\n Digite a data (YYYY-MM-DD) das notas que você quer localizar:")
    
    lista_notas = query_notes(tabela_hash, data_requisitada)

    #print para verificar 
    print(lista_notas)

if __name__ == "__main__":
    rodar_pipeline_completo()