import csv
import os

from pathlib import Path

from backend.sources.indexer import create_index_file
from backend.sources.hash_table import initiate_dict
from backend.sources.etl import query_notes
from backend.sources.sort import mergesort_notas

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

    notas_ordenadas = mergesort_notas(lista_notas)

    #print para verificar 
    print(notas_ordenadas)

if __name__ == "__main__":
    rodar_pipeline_completo()