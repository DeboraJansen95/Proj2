import pandas as pd

 

# Lista de resultados dos candidatos com nomes aleatórios

candidatos = [

    {"nome": "João", "id": 1, "resultados": "e4_t4_p8_s8"},

    {"nome": "Ana", "id": 2, "resultados": "e5_t5_p7_s7"},

    {"nome": "Pedro", "id": 3, "resultados": "e6_t6_p6_s6"},

    {"nome": "Maria", "id": 4, "resultados": "e7_t7_p5_s5"},

    {"nome": "Carlos", "id": 5, "resultados": "e8_t8_p4_s4"}

]

 

# Cria um DataFrame a partir da lista de candidatos

df = pd.DataFrame(candidatos)

 

# Separa a string de resultados em colunas separadas

df[['e', 't', 'p', 's']] = df['resultados'].str.split('_', expand=True)

 

# Remove os caracteres não numéricos das colunas de notas e converte para inteiros

df[['e', 't', 'p', 's']] = df[['e', 't', 'p', 's']].apply(lambda x: x.str[1:].astype(int))

 

# Cria uma nova coluna com a soma total das notas

df['total'] = df[['e', 't', 'p', 's']].sum(axis=1)

 

# Imprime o DataFrame da lista de candidatos e suas notas no formato original

print("Candidatos e resultados:")

print(df[['nome', 'id', 'resultados']].to_string(index=False))

print("\n")  # Espaço de parágrafo

 

# Separa os candidatos que se enquadram nos critérios

df_selecionados = df[(df['e'] >= 5) & (df['t'] >= 5) & (df['p'] >= 5) & (df['s'] >= 5)]

 

# Imprime os candidatos que se enquadram nos critérios

print("Candidatos compatíveis com os parâmetros:")

print(df_selecionados[['nome', 'id', 'resultados']].to_string(index=False))

print("\n")  # Espaço de parágrafo

 

# Cria um novo DataFrame com a somatória das notas dos candidatos compatíveis

df_total_selecionados = df_selecionados[['nome', 'id', 'total']]

 

# Imprime o novo DataFrame com a somatória das notas dos candidatos compatíveis

print("Somatória das notas dos candidatos compatíveis:")

print(df_total_selecionados.to_string(index=False))

print("\n")  # Espaço de parágrafo

 

# Encontra o melhor candidato entre os compatíveis com base na maior somatória das notas

melhor_candidato = df_selecionados[df_selecionados['total'] == df_selecionados['total'].max()]['nome'].values[0]

 

print(f'O melhor candidato entre os compatíveis é {melhor_candidato} com base na maior somatória das notas.')