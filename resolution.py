# META INFORMATION
# Author: João Leonardi da Silva Melo
# Teacher: Dimmy Magalhães
# License: MIT license
# Copyright (c) 2023 Leonardi Melo
# Github: rexionmars
# E-mail: opensource.leonardi@gmail.com
# Date: 15/07/2023
# Code Editor: GNU Emacs (Doom Emacs)
# OS: Arch Linux x86_64


# Disclaimer:
# Sei que essa `avalição` há varias formas para responder,
# porém optei por ser o mais claro e direto possível.


# [DOC] https://numpy.org/doc/stable/user/absolute_beginners.html
import numpy as np

# [DOC] https://pandas.pydata.org/docs/getting_started/index.html#getting-started
import pandas as pd




# Questão 1: Crie um array NumPy chamado arr1 de 1D com os números de 1 a 50000
# Solução: usei o List Comprehension para preencher o Array, com os valores
# indicados na questão.
# OBS: o start da função `range` começa do 0, exemplo: 0 a 50000, o maior valor
# será 50000, agora se for iniciado do 1, o maior número será 49999. Logica do
# range: valor_final - valor_inicial
arr1 = np.array([ i for i in range(1, 50000 + 1)])




# Questão 2: Crie uma matriz NumPy 3x3 chamada mat1 com valores aleatórios entre 0 e 1
# IDEIA: penso que os valores entre 0 e 1, sejam referentes aos pesos em uma NN.
# Solução: `RANDOM_SAMPLE`Retorna valores flutuantes aleatórios no intervalo [0,0, 1,0].
# [DOC] Numpy `random_sample`: https://numpy.org/doc/stable/reference/random/generated/numpy.random.random_sample.html
mat1 = np.random.random_sample((3, 3))




# Questão 3: Qual é o valor máximo no array arr1?
# Solução: como na Q1 usamos List Comprehension para preencer a variavel `arr1`,
# logo a senquecia será [1, 2, 3, 4, 5, 6, ..., 49999], então se obtermos o ultimo
# elemento do arry, logo ele será o máximo valor.
max_valor = arr1[-1]




# Questão 4: Calcule a média dos valores no array arr1.
# Solução: Essa questão poderia ser resolvida de varias forma, irei usar apenas duas
# para finz de curiosidade.
# [DOC] Numpy `mean`: https://numpy.org/doc/stable/reference/generated/numpy.mean.html
# 1°. media = soma_dos_valores / total_de_elementos
#     Ex: media = sum(arr1) / len(arr1)
#
# 2°. Numpy mean
#     Ex: mean(arr1)
array_media = np.mean(arr1)



# Questão 5: Multiplique todos os elementos do array arr1 por 2.
# OBS: Sei que esse nome da variavel ficou estranho mas, o siginificado
# é: ELEMENTO DO ARRAY VEZES 2, ou seja `para cada elemento do array,
# elemento é igual a elemento * 2`, em resumo, dobra o valor do indice.
array_element_x2 = [ i * 2 for i in arr1 ]




# Questão 6: Multiplique todos os elementos da matriz mat 1 por 2.
# Aqui não tem muito segredo, apenas estamos pegando cada elemento da
# matriz e multiplicando por 2.
# IDEIA. `exibi as saidas nesse caso, apenas por didatica, porque pode ser
# confuso imaginar os valores de 0 entre 1, multiplicados por 2.`
# Isso me parece pesos de uma NN, com/sem bias.
matriz_x2 = mat1 * 2
#   print("Matriz * 1:\n{}\n".format(mat1))
#   print("Matriz * 2:\n{}\n".format(matriz_x2))




# Questão 7: Calcule o determinante da mat1.
# Solução: aqui usei o metodo linalg.det que vem incluso na lib Pandas, para calcular o determinante 
# [DOC] Numpy `linalg`: https://numpy.org/doc/stable/reference/generated/numpy.linalg.det.html
determinant = np.linalg.det(mat1)




# OBS: a partir desse ponto começam as questões de manipulação de
# data frame


# Questão 8: Crie um DataFrame Pandas chamdo df com as seguintes colunas:
# ‘Nome’, ‘Idade’, ‘Sexo’, ‘Medicamento’.
# Aqui também não tem muito segredo, é apenas o uso básico da biblioteca Pandas
# [DOC] Pandas `DataFrame`: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html
df = pd.DataFrame(columns=['Nome', 'Idade', 'Sexo', 'Medicamento'])




# Questão 9: Preencha o dataframe df com os seguintes dados:
# Aqui também não tem muito segredo, é só preencher o data frame
# com os dados fornecidos na questão.
data = {
    'Nome': ['Ana', 'Bartolomeu', 'Caio', 'Dora'],
    'Idade': [28, 32, 25, 60],
    'Sexo': ['F', 'M', 'F', 'F'],
    'Medicamento': ['A', 'B', 'A', 'B']
}

df = pd.DataFrame(data)




# Questão 10: Crie uma nova coluna no dataframe df com os seguintes dados:
# curado = [True, True, False, False]
# Solução: a variavel curado é uma lista inicializada com seus valores sendo
# verdadeiro ou falso, para ser utilizados na coluna `curado`.
# OBS: df['curado'], o valor dentro dos colchetes, NÂO É A VARIAVEL `curado`
# declarado logo acima.
curado = [True, True, False, False]
df['curado'] = curado




# Questão 11: Selecione apenas as linhas do DataFrame df em que o sexo seja 'F'.
# Aqui também é de boa, apenas usei o loc para selecionar a coluna `Sexo` e filtrar
# por sexo feminino `F`.
# [DOC] Pandas `loc`: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html
filter = df.loc[df['Sexo'] == 'F']




# Questão 12: Ordene o DataFrame df por idade em ordem decrescente.
# Solução: usei o metodo `sort_values` do data frame para ordenar
# os valores da coluna `idade` em ordem decrescente.
# [DOC] Pandas `sort_values`: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html
order_by_age = df.sort_values('Idade', ascending=False)


# Questão 13: Faça o pivoteamento do dataframe df de acordo com a coluna Medicamento
# Aqui também é bem simples, usei o metodo `pivot_table` pra fazer o pivoteamento do
# data frame.
# [DOC] Pandas `pivot_table`: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pivot_table.html
df_pivot = df.pivot_table(index='Nome', columns='Medicamento', values=['Idade', 'Sexo'], aggfunc='first')
