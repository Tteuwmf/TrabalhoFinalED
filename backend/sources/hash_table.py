from collections import defaultdict

INDEX_FILE = "indices/notas_index.txt"

def initiate_dict():
     
    tabela_hash = defaultdict(list)
    print("Carregando banco de índices para a memória...")

    try:
        with open(INDEX_FILE, "r", encoding="utf-8") as f:
            for linha in f:
                linha = linha.strip()
                if not linha:
                    continue
                
                data, offsets_agrupados = linha.split("|")
                lista_de_inteiros = [int(off) for off in offsets_agrupados.split(",")]
                tabela_hash[data].extend(lista_de_inteiros)

        primeira_data = min(tabela_hash.keys())
        ultima_data = max(tabela_hash.keys())
        print(f"Índice carregado! {len(tabela_hash)} dias diferentes disponíveis para busca.")
        print(f"Período disponível para pesquisa: de {primeira_data} até {ultima_data}.")
        
        return tabela_hash

    except FileNotFoundError:
        print("Arquivo de índice não encontrado.")
        return {}