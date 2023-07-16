# Author: João Leonardi da Silva Melo
# Teacher: Dimmy Magalhães
# License: MIT license
# Copyright (c) 2023 Leonardi Melo
# Github: rexionmars
# E-mail: opensource.leonardi@gmail.com
# Date: <2023-07-16>
# Code Editor: GNU Emacs (Doom Emacs)
# OS: Arch Linux x86_64

import numpy as np
import pandas as pd
import argparse as ap

parser = ap.ArgumentParser()

parser.add_argument("-q", "--quest", metavar="", type=int, required=True, help="Número das questões de 1 a 13")
parser.add_argument("-d", "--desc", action="store_true",
                    help="Mostra o enuciado das questões e a lógica que usei para resolvê-las")

args = parser.parse_args()

class ResolvedQuestions():
    def __init__(self):
        # Iniciando o arr1, que será usada em varias questões
        self.arr1 = np.array([ i for i in range(1, 50000 + 1)])
        # Iniciando a mat1, que será usada em varias questões
        self.mat1 = mat1 = np.random.random_sample((3, 3))

    def question1(self):
        """Questão 1: Crie um array NumPy chamado arr1 de 1D com os números de 1 a 50000
        Solução: usei o List Comprehension para preencher o Array, com os valores
        indicados na questão.
        OBS: o start da função `range` começa do 0, exemplo: 0 a 50000, o maior valor
        será 50000, agora se for iniciado do 1, o maior número será 49999. Logica do
        range: valor_final - valor_inicial
        """
        #self.arr1 = np.array([ i for i in range(1, 50000 + 1)])

        return self.arr1

    def question2(self):
        """Questão 2: Crie uma matriz NumPy 3x3 chamada mat1 com valores aleatórios entre 0 e 1
        IDEIA: penso que os valores entre 0 e 1, sejam referentes aos pesos em uma NN.
        Solução: `RANDOM_SAMPLE`Retorna valores flutuantes aleatórios no intervalo [0,0, 1,0].
        [DOC] Numpy `random_sample`: https://numpy.org/doc/stable/reference/random/generated/numpy.random.random_sample.html
        """

        return self.mat1

    def question3(self):
        """Questão 3: Qual é o valor máximo no array arr1?
        Solução: como na Q1 usamos List Comprehension para preencer a variavel `arr1`,
        logo a senquecia será [1, 2, 3, 4, 5, 6, ..., 49999], então se obtermos o ultimo
        elemento do arry, logo ele será o máximo valor.
        """

        return self.arr1[-1]

    def question4(self):
        """Questão 4: Calcule a média dos valores no array arr1.
        Solução: Essa questão poderia ser resolvida de varias forma, irei usar apenas duas
        para finz de curiosidade.
        [DOC] Numpy `mean`: https://numpy.org/doc/stable/reference/generated/numpy.mean.html
        """

        array_media = np.mean(self.arr1)
        return array_media

    def question5(self):
        """Questão 5: Multiplique todos os elementos do array arr1 por 2.
        OBS: Sei que esse nome da variavel ficou estranho mas, o siginificado
        é: ELEMENTO DO ARRAY VEZES 2, ou seja `para cada elemento do array,
        elemento é igual a elemento * 2`, em resumo, dobra o valor do indice.
        """

        self.array_element_x2 = [ i * 2 for i in self.arr1 ]
        return self.array_element_x2

    def question6(self):
        """Questão 6: Multiplique todos os elementos da matriz mat 1 por 2.
        Solução: Aqui não tem muito segredo, apenas estamos pegando cada elemento da
        matriz e multiplicando por 2.
        Isso me parece pesos de uma NN, com/sem bias.
        OBS: você pode exibir as matrizes antes e depois, para comprar os
        resultados
        """

        self.matriz_x2 = self.mat1 * 2
        return self.matriz_x2

    def question7(self):
        """Questão 7: Calcule o determinante da mat1.
        Solução: aqui usei o metodo linalg.det que vem incluso na lib Pandas, para calcular o determinante
        [DOC] Numpy `linalg`: https://numpy.org/doc/stable/reference/generated/numpy.linalg.det.html
        """

        self.determinant = np.linalg.det(self.mat1)
        return self.determinant

    def question8(self):
        """Questão 8: Crie um DataFrame Pandas chamdo df com as seguintes colunas:
        ‘Nome’, ‘Idade’, ‘Sexo’, ‘Medicamento’.
        Soluçaõ: Aqui também não tem muito segredo, é apenas o uso básico da biblioteca Pandas
        [DOC] Pandas `DataFrame`: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html
        """

        self.df = pd.dataframe(columns=['nome', 'idade', 'sexo', 'medicamento'])
        return self.df

    def question9(self):
        """Questão 9: Preencha o dataframe df com os seguintes dados:
        'Nome': ['Ana', 'Bartolomeu', 'Caio', 'Dora'],
        'Idade': [28, 32, 25, 60],
        'Sexo': ['F', 'M', 'F', 'F'],
        'Medicamento': ['A', 'B', 'A', 'B']

        Solução: Aqui também não tem muito segredo, é só preencher o data frame
        com os dados fornecidos na questão.
        """

        self.data = {
            'Nome': ['Ana', 'Bartolomeu', 'Caio', 'Dora'],
            'Idade': [28, 32, 25, 60],
            'Sexo': ['F', 'M', 'F', 'F'],
            'Medicamento': ['A', 'B', 'A', 'B']
        }

        self.df = pd.DataFrame(self.data)
        return self.df

    def question10(self):
        """Questão 10: Crie uma nova coluna no dataframe df com os seguintes dados:
        curado = [True, True, False, False]
        Solução: a variavel curado é uma lista inicializada com seus valores sendo
        verdadeiro ou falso, para ser utilizados na coluna `curado`.
        OBS: df['curado'], o valor dentro dos colchetes, NÂO É A VARIAVEL `curado`
        declarado logo acima.
        """

        self.question9()
        self.curado = [True, True, False, False]
        self.df['curado'] = self.curado
        return self.df

    def question11(self):
        """Questão 11: Selecione apenas as linhas do DataFrame df em que o sexo seja 'F'.
        Solução: Aqui também é de boa, apenas usei o loc para selecionar a coluna `Sexo` e filtrar
        por sexo feminino `F`.
        [DOC] Pandas `loc`: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html
        """

        self.question10()
        self.filter = self.df.loc[self.df['Sexo'] == 'F']
        return self.filter

    def question12(self):
        """Questão 12: Ordene o DataFrame df por idade em ordem decrescente.
        Solução: usei o metodo `sort_values` do data frame para ordenar
        os valores da coluna `idade` em ordem decrescente.
        [DOC] Pandas `sort_values`: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html
        """

        self.question10()
        self.order_by_age = self.df.sort_values('Idade', ascending=False)
        return self.order_by_age

    def question13(self):
        """Questão 13: Faça o pivoteamento do dataframe df de acordo com a coluna Medicamento
        Solução: Aqui também é bem simples, usei o metodo `pivot_table` pra fazer o pivoteamento do
        data frame.
        [DOC] Pandas `pivot_table`: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pivot_table.html
        """

        self.question10()
        self.df_pivot = self.df.pivot_table(index='Nome', columns='Medicamento', values=['Idade', 'Sexo'], aggfunc='first')
        return self.df_pivot

def match_case(quest_number: int):
    quest = ResolvedQuestions()

    # Preenchendo automaticamente o dicionario com as questões
    #options = {
    #   1: quest.question1,
    #   .....
    #   13: quest.question13
    #}
    options = {
        i: getattr(quest, f"question{i}")
        for i in range(1, 14)
    }

    if quest_number in options:
        # Se na execução do arquivo for informado o argumento --desc, o programa
        # vai mostrar o enuciado da questão, se não, apenas roda a solução da questão
        output = options[quest_number].__doc__ if args.desc else options[quest_number]()
        return output

if __name__ == "__main__":
    output = match_case(args.quest)
    print(output)
