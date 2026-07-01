import csv

NOTAS_FILE = "raw_data/202601_NFe_NotaFiscal.csv"

def create_index_file ():
    
    with open(NOTAS_FILE, "r", encoding="iso-8859-1", newline="") as f:
        with open("indices/notas_index.txt", "w", encoding="utf-8") as i:

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

                i.write(f"{data_limpa},{offset}\n")
                 
                # Trava de segurança para não processar o arquivo inteiro agora
                if contador >= 10:
                    break

    print(f"Índice criado com sucesso! {contador} registros indexados.")

