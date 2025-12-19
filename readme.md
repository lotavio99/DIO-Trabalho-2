## 📌 Descrição do Projeto

Este projeto foi desenvolvido como parte de um desafio da Digital Innovation One (DIO), com o objetivo de aplicar conceitos básicos de Processamento Digital de Imagens.

A proposta consiste em implementar, utilizando Python, um algoritmo capaz de:

Converter uma imagem colorida (RGB) para níveis de cinza (valores de 0 a 255)

Converter a imagem em níveis de cinza para uma imagem binarizada, contendo apenas pixels pretos (0) e brancos (255)

Como referência visual, o resultado esperado inclui a imagem original colorida, sua versão em tons de cinza e a versão final em preto e branco.

## 🧠 Conceitos Aplicados
Conversão para Tons de Cinza

A conversão da imagem colorida para tons de cinza foi realizada a partir de uma combinação ponderada dos canais R (vermelho), G (verde) e B (azul), utilizando a seguinte fórmula:

Cinza = 0.299 × R + 0.587 × G + 0.114 × B


Essa abordagem leva em consideração a sensibilidade do olho humano às diferentes cores.

## Binarização da Imagem

Após a conversão para níveis de cinza, foi aplicada a técnica de binarização, que consiste em definir um valor de limiar (threshold).
Pixels com valor maior ou igual ao limiar são convertidos para branco (255) e os demais para preto (0).

## 🛠️ Tecnologias Utilizadas

Python 3

Pillow (PIL) – para leitura e manipulação de imagens

NumPy – para operações matemáticas e manipulação de arrays

📂 Estrutura do Projeto
📁 desafio-binarizacao-dio
 ├── lena.png
 ├── lena_cinza.png
 ├── lena_binaria.png
 ├── main.py
 └── README.md


lena.png: imagem original colorida

lena_cinza.png: imagem convertida para tons de cinza

lena_binaria.png: imagem binarizada (preto e branco)

main.py: script principal do projeto

README.md: documentação do projeto

## ▶️ Como Executar o Projeto

Certifique-se de ter o Python instalado (versão 3 ou superior)

Instale as dependências necessárias:

pip install pillow numpy


Coloque a imagem de entrada (lena.png) na pasta do projeto

Execute o script:

python main.py


As imagens processadas serão geradas automaticamente na mesma pasta

## ✅ Resultado Esperado

Ao final da execução, o projeto gera:

Uma imagem em tons de cinza

Uma imagem binarizada, contendo apenas pixels pretos e brancos

Esses resultados demonstram, de forma prática, a aplicação dos conceitos estudados durante o módulo.

## 📚 Considerações Finais

Este desafio foi fundamental para reforçar o entendimento sobre manipulação de imagens digitais, além de proporcionar uma experiência prática com bibliotecas amplamente utilizadas no ecossistema Python.