# Sistema de Indexação e Consulta de Notas Fiscais

Trabalho final desenvolvido para a disciplina de **Estruturas de Dados** do curso de Ciência da Computação da **UFRGS**.

O projeto implementa uma solução para consulta eficiente de notas fiscais armazenadas em arquivos CSV, sem utilizar um sistema gerenciador de banco de dados.

A aplicação utiliza **indexação por offsets físicos de arquivo**, **Tabela Hash** para localizar registros por data e uma implementação própria de **Merge Sort** para ordenar os resultados pelo valor das notas.

## Tecnologias e conceitos utilizados

- Python
- Estruturas de Dados
- Tabela Hash
- Merge Sort
- Indexação de arquivos
- Manipulação de CSV
- Acesso direto a arquivos com `seek()`
- Streamlit

## Como funciona

1. O arquivo CSV é processado para gerar um índice que associa cada data de emissão aos offsets dos respectivos registros.
2. Esse índice é carregado em memória utilizando uma tabela hash.
3. A aplicação usa os offsets encontrados para acessar diretamente as notas no arquivo CSV.
4. As notas recuperadas são ordenadas por valor com Merge Sort.
5. Os resultados podem ser consultados por meio de uma interface em Streamlit.

## Interface

A interface permite pesquisar notas fiscais por data e visualizar os resultados encontrados em ordem decrescente de valor.

## Objetivo acadêmico

O objetivo do projeto foi aplicar na prática conceitos estudados em **Estruturas de Dados e Algoritmos**, principalmente:

- tabelas hash;
- indexação de arquivos;
- acesso a registros por posição;
- algoritmos de ordenação;
- organização modular do código.

## Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/Tteuwmf/TrabalhoFinalED.git
cd TrabalhoFinalED
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Prepare os dados

Crie as pastas:

```text
raw_data/
indices/
```

Coloque o arquivo de notas fiscais utilizado pela aplicação dentro de `raw_data/` com o nome:

```text
202601_NFe_NotaFiscal.csv
```

O arquivo de índice será gerado pela aplicação e armazenado na pasta `indices/`.

### 4. Execute a interface

```bash
streamlit run app.py
```

Após a inicialização, o Streamlit abrirá a aplicação no navegador.

## Autor

**Matheus Dagostini Faccini**  
Ciência da Computação — UFRGS
