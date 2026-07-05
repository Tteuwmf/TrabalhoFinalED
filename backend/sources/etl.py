import csv
from datetime import datetime

NOTAS_FILE = "raw_data/202601_NFe_NotaFiscal.csv"


def query_notes(hash_table, data_requisitada):

    notas = []

    if data_requisitada not in hash_table:
        print("Nenhuma nota encontrada para esta data.")
        return notas # Retorna a lista vazia

    with open(NOTAS_FILE, "r", encoding="iso-8859-1", newline="") as f:

        cabecalho = next(csv.reader([f.readline()], delimiter=";"))

        lista_offsets = hash_table[data_requisitada]

        for offset in lista_offsets:
            f.seek(offset)
            linha_crua = f.readline()

            #CORREÇÃO = trecho feito pelo gemini: transforma a linha lida em um dict
            campos = next(csv.reader([linha_crua], delimiter=";"))
            linha = dict(zip(cabecalho, campos)) #zip agrupa em pares usando o cabeçalho

            notas.append(limpar_e_transformar_nota(linha))

    return notas
                




def limpar_e_transformar_nota(registro_bruto):
    """
    Recebe um dicionário bruto do CSV do governo e retorna um dicionário tipado e limpo.
    """
    chave = registro_bruto.get("CHAVE DE ACESSO", "").strip()
    data_bruta = registro_bruto.get("DATA EMISSÃO", "").strip()
    cnpj_bruto = registro_bruto.get("CPF/CNPJ Emitente", "").strip()
    nome = registro_bruto.get("RAZÃO SOCIAL EMITENTE", "").strip()
    orgao = registro_bruto.get("ÓRGÃO DESTINATÁRIO", "").strip()
    valor_bruto = registro_bruto.get("VALOR NOTA FISCAL", "").strip()

    try:
        valor_float = float(valor_bruto.replace(".", "").replace(",", "."))
    except ValueError:
        valor_float = 0.0

    try:
        data_dt = datetime.strptime(data_bruta, "%d/%m/%Y %H:%M:%S")
        data_iso = data_dt.strftime("%Y-%m-%d")
        mes_ref = data_dt.strftime("%Y-%m")
    except ValueError:
        data_iso = "1900-01-01"
        mes_ref = "1900-01"

    return {
        "chave_nota": chave,
        "data_emissao": data_iso,
        "mes_referencia": mes_ref,
        "cnpj_fornecedor": cnpj_bruto,
        "nome_fornecedor": nome,
        "orgao_destinatario": orgao,
        "valor_nota": valor_float
    }