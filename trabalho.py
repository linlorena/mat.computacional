import pandas as pd

# Lê o arquivo Excel usando pd.read_excel()
educacao = pd.read_excel('educacao.xlsx')
mobilidade = pd.read_excel('mobilidade.xlsx')
saude = pd.read_excel('saude.xlsx')

# Agora você pode trabalhar com os dados lidos do arquivo educacao.xlsx
#print(educacao)
#print(mobilidade)
#print(saude)

import datetime


arquivo_excel = 'educacao.xlsx'
df = pd.read_excel(arquivo_excel)

formatos_esperados = ['%d/%m/%Y', '%m/%d/%Y']

# Converte a coluna de datas para datetime
coluna_data = 'Data de Nascimento'  # Substitua pelo nome correto da coluna
datas_convertidas = pd.to_datetime(df[coluna_data], errors='coerce')

# Verifica datas inconsistentes
datas_inconsistentes = df[~datas_convertidas.dt.strftime(formatos_esperados[0]).isin(df[coluna_data]) & 
                         ~datas_convertidas.dt.strftime(formatos_esperados[1]).isin(df[coluna_data])]

# Exibe as datas inconsistentes
print(datas_inconsistentes)

# Cria uma nova coluna para armazenar as datas corrigidas
df['coluna_data_corrigida'] = datas_convertidas

# Loop para corrigir as datas inconsistentes
for idx, row in datas_inconsistentes.iterrows():
    for formato in formatos_esperados:
        try:
            data_corrigida = pd.to_datetime(row[coluna_data], format=formato)
            df.at[idx, 'coluna_data_corrigida'] = data_corrigida
            break
        except:
            pass

# Exibe o DataFrame com as datas corrigidas
print(df)

# Organiza a coluna ID por ordem crescente
df_ordenado = df.sort_values(by='ID', ascending=True)

# Encontrar os cidadãos do arquivo Saúde que tiveram dengue
cidadaos_com_dengue = saude['Nome'][saude['Data da Dengue'].notnull()]

# Filtrar os cidadãos do arquivo Educação que não tiveram dengue
educacao_sem_dengue = educacao[~educacao['Nome'].isin(cidadaos_com_dengue)]

# Selecionar as colunas desejadas
colunas_desejadas = ['Nome', 'Data de Nascimento', 'ID']
relatorio_educacao = educacao_sem_dengue[colunas_desejadas]

# Salvar o DataFrame em um novo arquivo Excel
relatorio_educacao.to_excel('Relatório_Educação.xlsx', index=False)



# Filtrar os cidadãos do arquivo Saude que não estão no arquivo Mobilidade
saude_sem_mobilidade = saude[~saude['Nome'].isin(mobilidade['Nome'])]

# Criar um DataFrame com as colunas desejadas
relatorio_saude = saude_sem_mobilidade[['Nome', 'Data de Nascimento', 'Data da Dengue']]

# Salvar o DataFrame em um novo arquivo Excel
relatorio_saude.to_excel('Relatorio_Saude.xlsx', index=False)



# Encontrar os cidadãos do arquivo Saúde que tiveram dengue
cidadaos_com_dengue = saude['Nome'][saude['Data da Dengue'].notnull()]

# Filtrar os cidadãos do arquivo Mobilidade que não tiveram dengue
mobilidade_sem_dengue = mobilidade[~mobilidade['Nome'].isin(cidadaos_com_dengue)]

# Selecionar as colunas desejadas
colunas_desejadas = ['Nome', 'Data de Nascimento', 'Ônibus']
relatorio_mobilidade = mobilidade_sem_dengue[colunas_desejadas]

# Salvar o DataFrame em um novo arquivo Excel
relatorio_mobilidade.to_excel('Relatório_Mobilidade.xlsx', index=False)


# Juntar os dados dos arquivos Educação e Saude pelo nome
relatorio_educacao_saude = pd.merge(educacao, saude, on='Nome', how='inner')

# Selecionar as colunas desejadas
colunas_desejadas = ['Nome', 'Data de Nascimento_x', 'ID', 'Data da Dengue']
relatorio_educacao_saude = relatorio_educacao_saude[colunas_desejadas]

# Renomear as colunas
relatorio_educacao_saude.rename(columns={'Data de Nascimento_x': 'Data de Nascimento'}, inplace=True)

# Salvar o DataFrame em um novo arquivo Excel
relatorio_educacao_saude.to_excel('Relatório_Educacao_Saude.xlsx', index=False)


# Juntar os dados dos arquivos Educacao e Mobilidade pelo nome
relatorio_educacao_mobilidade = pd.merge(educacao, mobilidade, on='Nome', how='inner')

# Selecionar as colunas desejadas
colunas_desejadas = ['Nome', 'Data de Nascimento_x', 'ID', 'Ônibus']
relatorio_educacao_mobilidade = relatorio_educacao_mobilidade[colunas_desejadas]

# Renomear as colunas
relatorio_educacao_mobilidade.rename(columns={'Data de Nascimento_x': 'Data de Nascimento'}, inplace=True)

# Salvar o DataFrame em um novo arquivo Excel
relatorio_educacao_mobilidade.to_excel('Relatório_Educacao_Mobilidade.xlsx', index=False)



# Juntar os dados dos arquivos Saude e Mobilidade pelo nome
relatorio_saude_mobilidade = pd.merge(saude, mobilidade, on='Nome', how='inner')

# Renomear as colunas para que sejam únicas e distinguíveis
relatorio_saude_mobilidade = relatorio_saude_mobilidade.rename(columns={'Data de Nascimento_x': 'Data de Nascimento Saude', 
                                                                      'Data de Nascimento_y': 'Data de Nascimento Mobilidade'})

# Selecionar as colunas desejadas
colunas_desejadas = ['Nome', 'Data de Nascimento Saude', 'Data da Dengue', 'Ônibus']
relatorio_saude_mobilidade = relatorio_saude_mobilidade[colunas_desejadas]

# Salvar o DataFrame em um novo arquivo Excel
relatorio_saude_mobilidade.to_excel('Relatório_Saude_Mobilidade.xlsx', index=False)



# Juntar os dados dos arquivos Saude, Mobilidade e Educação pelo nome
relatorio_completo = pd.merge(saude, mobilidade, on='Nome', how='inner')
relatorio_completo = pd.merge(relatorio_completo, educacao, on='Nome', how='inner')

# Selecionar as colunas desejadas
colunas_desejadas = ['Nome', 'Data de Nascimento_x', 'Data da Dengue', 'Ônibus']
relatorio_completo = relatorio_completo[colunas_desejadas]

# Renomear as colunas para que sejam únicas e distinguíveis
relatorio_completo = relatorio_completo.rename(columns={'Data de Nascimento_x': 'Data de Nascimento Saude'})

# Salvar o DataFrame em um novo arquivo Excel
relatorio_completo.to_excel('Relatório_Saude_Mobilidade_Educacao.xlsx', index=False)



# Encontrar os cidadãos do arquivo Saúde que não estão no arquivo Educação
cidadaos_sem_educacao = saude[~saude['Nome'].isin(educacao['Nome'])]

# Selecionar as colunas desejadas
colunas_desejadas = ['Nome', 'Data de Nascimento', 'Data da Dengue']
relatorio_saude_sem_educacao = cidadaos_sem_educacao[colunas_desejadas]

# Salvar o DataFrame em um novo arquivo Excel
relatorio_saude_sem_educacao.to_excel('Relatório_Saude_Sem_Educacao.xlsx', index=False)



# Encontrar os cidadãos do arquivo Saúde que não estão no arquivo Educação nem no arquivo Mobilidade
cidadaos_sem_educacao_mobilidade = saude[~saude['Nome'].isin(educacao['Nome']) & ~saude['Nome'].isin(mobilidade['Nome'])]

# Selecionar as colunas desejadas
colunas_desejadas = ['Nome', 'Data de Nascimento', 'Data da Dengue']
relatorio_saude_sem_educacao_mobilidade = cidadaos_sem_educacao_mobilidade[colunas_desejadas]

# Salvar o DataFrame em um novo arquivo Excel
relatorio_saude_sem_educacao_mobilidade.to_excel('Relatório_Saude_Sem_Educacao_Mobilidade.xlsx', index=False)
