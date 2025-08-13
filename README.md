# Simulação do Fluxo de Pessoas em uma Praça Pública com Autômatos Celulares

## Descrição
Este projeto implementa uma simulação do fluxo de pessoas em uma praça pública utilizando o **Jogo da Vida de Conway** como base conceitual. A praça é representada como uma grade bidimensional (30x30 células), onde cada célula pode estar vazia, ocupada por uma pessoa ou conter um obstáculo fixo (como árvores ou bancos).  

A simulação demonstra como **comportamentos coletivos complexos** podem emergir a partir de **regras simples de interação local**.

## Regras da Simulação
As regras do autômato celular foram adaptadas do Jogo da Vida para o contexto de pessoas na praça:

- **Isolamento**: uma pessoa sozinha (menos de dois vizinhos) deixa o espaço;  
- **Superlotação**: uma pessoa com mais de três vizinhos também deixa o espaço;  
- **Atração social**: um espaço vazio com exatamente três vizinhos é ocupado por uma nova pessoa;  
- **Obstáculos fixos**: não mudam durante a simulação (representam árvores ou estruturas).  

A vizinhança é do tipo **Moore**, considerando os oito vizinhos ao redor de cada célula.

## Funcionalidades
- Grade 30x30 com densidade inicial de ocupação de 30%;  
- 15 obstáculos posicionados aleatoriamente;  
- Visualização animada com cores diferenciadas:  
  - **Vermelho**: pessoa;  
  - **Branco**: espaço vazio;  
  - **Verde**: obstáculo;  
- Exportação da simulação em **GIF animado**;  
- Parâmetros fáceis de ajustar (densidade, número de obstáculos, tamanho da grade, número de iterações).

## Tecnologias Utilizadas
- Python 3.x  
- Numpy  
- Matplotlib (para visualização e animação)  
- Pillow (para salvar GIFs)

## Como Rodar
1. Clone o repositório:  
```bash
git clone <URL_DO_REPOSITORIO>
Instale as dependências:

bash
Copiar
Editar
pip install numpy matplotlib pillow
Execute o script:

bash
Copiar
Editar
python jogo_da_vida_praca.py
O GIF da simulação será salvo como fluxo_pessoas_praca_obstaculos_aleatorios.gif.

Personalização
Você pode alterar facilmente os parâmetros no início do script:

python
Copiar
Editar
GRID_SIZE = 30           # tamanho da praça (grade)
DENSIDADE_INICIAL = 0.3  # porcentagem inicial de pessoas
NUM_OBSTACULOS = 15      # número de obstáculos (árvores, bancos, etc.)
FRAMES = 100             # número de iterações da simulação
INTERVALO_MS = 300       # intervalo entre frames (ms)
Aplicações
Ferramenta educacional para demonstrar comportamento emergente em sistemas complexos;

Visualização simplificada do fluxo de pessoas em espaços públicos;

Base para estudos mais avançados em planejamento urbano e dinâmica de multidões.

Referências
Conway, J.H. (1970). The Game of Life. Scientific American, 223(4), 4.

Wolfram, S. (2002). A New Kind of Science. Wolfram Media.

Bandini, S., Manzoni, S., & Vizzari, G. (2009). Agent Based Modeling and Simulation: An Informatics Perspective. Journal of Artificial Societies and Social Simulation, 12(4), 4.

Autor
Luis Abreu