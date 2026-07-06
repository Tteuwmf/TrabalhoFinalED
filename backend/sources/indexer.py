import csv

NOTAS_FILE = "raw_data/202601_NFe_NotaFiscal.csv"

def create_index_file():
    # Dicionário temporário na memória para agrupar as datas
    indice_temporario = {}

    with open(NOTAS_FILE, "r", encoding="iso-8859-1", newline="") as f:
        cabecalho = next(csv.reader([f.readline()], delimiter=";"))
        idx_data = cabecalho.index("DATA EMISSÃO")

        print("\n Iniciando Processamento de Notas...")
        contador = 0

        while True:
            contador += 1
            offset = f.tell()
            
            linha = f.readline()
            if not linha:
                break

            campos = next(csv.reader([linha], delimiter=";"))
            data_emissao = campos[idx_data]

            if len(data_emissao) >= 10:
                dia, mes, ano = data_emissao[:2], data_emissao[3:5], data_emissao[6:10]
                data_limpa = f"{ano}-{mes}-{dia}"
            else:
                data_limpa = "1900-01-01"

            # EM VEZ DE ESCREVER NO ARQUIVO AQUI, AGRUPAMOS NO DICIONÁRIO:
            if data_limpa not in indice_temporario:
                indice_temporario[data_limpa] = []
            
            # Adicionamos o offset convertido em string para facilitar depois
            indice_temporario[data_limpa].append(str(offset))

    # --- FIM DO LOOP DO CSV ---
    
    # Agora que lemos todo o CSV, abrimos o txt e escrevemos agrupado
    with open("indices/notas_index.txt", "w", encoding="utf-8") as i:
        for data, lista_offsets in indice_temporario.items():
            # Junta todos os offsets com vírgula e separa da data com "|"
            offsets_agrupados = ",".join(lista_offsets)
            i.write(f"{data}|{offsets_agrupados}\n")

    print(f"Índice criado com sucesso! {contador} registros processados e agrupados em {len(indice_temporario)} dias.")