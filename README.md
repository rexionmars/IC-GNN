<div align=center>
  <h1>IC-GNN Get started</h1>
  <p>Undergraduate Research Project in Generative Neural Networks.</p>
</div>

## Como instalar ?
Passo 1: Clonar o repositório
```sh
git clonehttps://github.com/rexionmars/IC-GNN.git && cd IC-NN
```
Passo 2: Instalar as dependências<br>
_OBS: lembre-se de ativar o seu ambiente virtal_
```sh
pip install -r requirements.txt
```
## Como rodar o programa?
Este script é uma aplicação command-line, logo pode ser fornecido parâmetros em sua chamada.<br>
Para acessar as opções do programa rode:
```sh
python3 resolution.py --help
```
<img src="thumbnail/swappy-20230716_222604.png" alt="Snake logo">

Exibindo as informações referente a questão desejada, usando o parâmetro opcional `--desc`.<br>
```sh
python3 resolution.py --quest NUMERO_DA_QUESTAO_ECOLHIDA --desc
```
<img src="thumbnail/swappy-20230716_222033.png" alt="Snake logo">

Exibindo a solução referente a questão desejada, usando o parâmetro `--quest`.<br>
```sh
python3 resolution.py --quest NUMERO_DA_QUESTAO_ECOLHIDA
```
<img src="thumbnail/swappy-20230716_222057.png" alt="Snake logo">
