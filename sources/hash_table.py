from collections import defaultdict

INDEX_FILE = "indices/notas_index.txt"

def initiate_dict():

    tabela_hash = defaultdict(list)

    with open(INDEX_FILE, "r", encoding="utf-8") as f:

        while True:

            linha = f.readline()
            if not linha:
                break

            data, offset_str = linha.strip().split(",")
            offset = int(offset_str)

            tabela_hash[data].append(offset)

    for i, (data, lista_offsets) in enumerate(tabela_hash.items()):
        if i >10:
            break
        
        print(f"data: {data} | offsets: {lista_offsets}")