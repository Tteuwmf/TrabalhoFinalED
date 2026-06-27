
import zipfile
import csv
import os

from etl import limpar_e_transformar_nota
from processar_itens import processar_arquivo_itens

PASTA_BRUTA = "dados_brutos"
ARQUIVO_NOTAS = "202601_NFe_NotaFiscal.csv"
ARQUIVO_ITENS = "202601_NFe_NotaFiscalItem.csv"

def rodar_pipeline_completo():
    
    arquivos = [f for f in os.listdir(PASTA_BRUTA) if f.endswith('.zip')]
    if not arquivos:
        print(" Arquivo ZIP não encontrado.")
        return
        
    caminho_zip = os.path.join(PASTA_BRUTA, arquivos[0])
    
    contador = 0
    
    with zipfile.ZipFile(caminho_zip, 'r') as z:
        # --- PASSO 1: Processar Notas (Cabeçalhos) ---
        print("\n🚀 Iniciando Processamento de Notas...")
        with z.open(ARQUIVO_NOTAS, 'r') as f:
            linhas_decodificadas = (linha.decode('iso-8859-1') for linha in f)
            leitor = csv.DictReader(linhas_decodificadas, delimiter=';')
            
            for linha_bruta in leitor:
                contador += 1
                
                nota_limpa = limpar_e_transformar_nota(linha_bruta)
                
                #SALVAR A NOTA
                print(nota_limpa.get("chave_nota"))
                
                # Trava de segurança para não processar o arquivo inteiro agora
                if contador >= 10:
                    break
        
        # --- PASSO 2: Processar Itens (Produtos) e linkar --- #
        processar_arquivo_itens(caminho_zip, ARQUIVO_ITENS)
                    
    print(f"\nRESUMO FINAL: {contador} notas processadas ")

if __name__ == "__main__":
    rodar_pipeline_completo()