# Análise de Dados Sociais

Este projeto realiza uma análise de dados sociais a partir de três arquivos Excel: `educacao.xlsx`, `mobilidade.xlsx` e `saude.xlsx`. O objetivo é combinar e filtrar informações para gerar relatórios específicos, utilizando a técnica do diagrama de Venn para visualização e interpretação dos dados.

## Uso

1. Coloque os arquivos `educacao.xlsx`, `mobilidade.xlsx` e `saude.xlsx` no diretório do projeto.

2. Execute o script Python para gerar os relatórios:

    ```bash
    python script.py
    ```

## Script Python

O script realiza as seguintes operações:

1. Lê os dados dos arquivos Excel.
2. Converte e corrige datas inconsistentes.
3. Organiza os dados em ordem crescente por ID.
4. Gera relatórios específicos conforme as necessidades.

## Relatórios Gerados

### Relatório Completo

Este relatório combina dados de `saude.xlsx`, `mobilidade.xlsx` e `educacao.xlsx`.

`Relatório_Saude_Mobilidade_Educacao.xlsx`

### Relatório de Educação

Este relatório contém cidadãos do arquivo `educacao.xlsx` que não tiveram dengue.

`Relatório_Educação.xlsx`

### Relatório de Saúde

Este relatório contém cidadãos do arquivo `saude.xlsx` que não estão no arquivo `mobilidade.xlsx`.

`Relatório_Saude.xlsx`

### Relatório de Mobilidade

Este relatório contém cidadãos do arquivo `mobilidade.xlsx` que não tiveram dengue.

`Relatório_Mobilidade.xlsx`


### Relatório de Educação e Saúde

Este relatório combina dados de `educacao.xlsx` e `saude.xlsx`.

`Relatório_Educacao_Saude.xlsx`

### Relatório de Educação e Mobilidade

Este relatório combina dados de `educacao.xlsx` e `mobilidade.xlsx`.

`Relatório_Educacao_Mobilidade.xlsx`

### Relatório de Saúde e Mobilidade

Este relatório combina dados de `saude.xlsx` e `mobilidade.xlsx`.

`Relatório_Saude_Mobilidade.xlsx`

### Relatório de Saúde sem Educação

Este relatório contém cidadãos do arquivo `saude.xlsx que não estão no arquivo `educacao.xlsx`.

`Relatório_Saude_Sem_Educacao.xlsx`

### Relatório de Saúde sem Educação e Mobilidade

Este relatório contém cidadãos do arquivo `saude.xlsx` que não estão nos arquivos `educacao.xlsx` nem `mobilidade.xlsx`.

`Relatório_Saude_Sem_Educacao_Mobilidade.xlsx`






