
import streamlit as st
from pathlib import Path
import os

from backend.sources.indexer import create_index_file
from backend.sources.hash_table import initiate_dict
from backend.sources.etl import query_notes

st.set_page_config(page_title="Ordenador de Notas Fiscais", layout="wide")

# -------------------------------------------------------------------------
# MECANISMO DE CACHE: Garante que a Tabela Hash só seja montada UMA VEZ na RAM
# -------------------------------------------------------------------------
@st.cache_resource
def carregar_sistema_de_indices():
    """
    Esta função roda apenas UMA vez. Ela verifica o índice físico e
    carrega a Tabela Hash para a memória RAM de forma persistente.
    """
    INDEX_FILE = "indices/notas_index.txt"
    arquivo_index = Path(INDEX_FILE)

    # Se o índice não existir na pasta, o back-end cria ele
    if not arquivo_index.is_file():
        create_index_file()
        
    # Carrega o dicionário (defaultdict) na memória
    tabela_hash = initiate_dict()
    return tabela_hash

# -------------------------------------------------------------------------
# INTERFACE VISUAL (FRONT-END)
# -------------------------------------------------------------------------

st.title("Painel de Consulta de Notas Fiscais")
st.markdown("Busca ultra-rápida em arquivos massivos utilizando **Índice Invertido** e **Tabela Hash**.")

# Inicializamos o nosso back-end de forma silenciosa e otimizada
with st.spinner("Carregando tabelas de índices na memória RAM..."):
    tabela_hash_persistente = carregar_sistema_de_indices()

# Criamos uma barra lateral para os filtros de busca
st.sidebar.header("Filtros de Busca")

# Input de texto onde o usuário vai digitar a data
data_digitada = st.sidebar.text_input(
    label="Digite uma data (Formato: YYYY-MM-DD):",
    value="2026-01-01",
    help="Exemplo: 2026-01-01"
)

# Botão para disparar a busca mecânica no disco
botao_buscar = st.sidebar.button("Localizar Notas no Disco")

# Se o usuário clicar no botão...
if botao_buscar:
    st.subheader(f"Resultados para o dia: {data_digitada}")
    
    # Executa a sua função do back-end que usa f.seek()
    with st.spinner("Saltando ponteiros no disco e recuperando registros..."):
        lista_de_notas = query_notes(tabela_hash_persistente, data_digitada)
    
    # Validação se encontrou algo
    if len(lista_de_notas) == 0:
        st.warning("Nenhuma nota fiscal encontrada para esta data ou chave não indexada.")
    else:
        # Exibe métricas rápidas na tela
        col1, col2 = st.columns(2)
        col1.metric("Total de Notas Encontradas", len(lista_de_notas))
        
        # Como o algoritmo de ordenação ainda não está pronto, 
        # vamos avisar que os dados estão em ordem bruta do arquivo
        st.info("Nota: Os dados abaixo estão na ordem original de leitura do disco. A ordenação por valor será implementada na próxima fase.")
        
        # O Streamlit recebe a sua lista de dicionários do Python 
        # e transforma magicamente em uma tabela interativa rica!
        st.dataframe(
            lista_de_notas, 
            use_container_width=True,
            column_config={
                "chave_nota": "Chave de Acesso",
                "data_emissao": "Data de Emissão",
                "cnpj_emitente": "CNPJ Emitente",
                "razao_social": "Razão Social",
                "orgao_destinatario": "Órgão Destinatário",
                "valor_nota": st.column_config.NumberColumn("Valor (R$)", format="%.2f")
            }
        )