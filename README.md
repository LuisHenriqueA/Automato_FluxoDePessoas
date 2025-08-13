
# Simulação de Fluxo de Pessoas em Praça Pública com Autômato Celular

Este projeto implementa uma versão adaptada do **Jogo da Vida** de John Conway em Python, simulando o fluxo e a formação de grupos de pessoas em uma praça pública.  
Além disso, obstáculos fixos (representando árvores ou estruturas) são posicionados aleatoriamente no espaço.

## 📝 Contexto

A simulação representa uma praça no centro de uma cidade, onde:
- Cada célula da grade representa um pequeno espaço físico da praça.
- Células **ocupadas** indicam a presença de uma pessoa.
- Células **vazias** indicam espaço livre.
- Células com **obstáculos** representam estruturas fixas (árvores, bancos, postes).

As regras são baseadas no Jogo da Vida:
- Uma pessoa permanece no local se houver exatamente 2 ou 3 pessoas vizinhas.
- Uma pessoa aparece em um espaço vazio se houver exatamente 3 pessoas vizinhas.
- Caso contrário, o espaço fica vazio.
- Obstáculos nunca mudam de estado.

## 🎯 Objetivo

Demonstrar como **autômatos celulares** podem ser aplicados para simular **dinâmicas de ocupação e movimento** em espaços públicos, auxiliando no planejamento urbano, arquitetura e ensino.

## 📦 Requisitos

- Python 3.8+
- Bibliotecas:
  ```bash
  pip install numpy matplotlib pillow
  ```

## ▶️ Como Executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/LuisHenriqueA/Automato_FluxoDePessoas.git
   ```

2. Execute o script principal:
   ```bash
   python main.py
   ```

3. Ao final, será gerado um gif com a animação.

## 📊 Parâmetros do Modelo

- **Tamanho da grade:** 30x30 células
- **Densidade inicial de ocupação:** 30%
- **Número de obstáculos:** 15 (posicionados aleatoriamente)
- **Número de gerações:** 50

## 📌 Exemplo de Uso

Este modelo pode ser usado para:
- Ensino de autômatos celulares.
- Visualização de dinâmicas de grupos.
- Simulação simplificada de fluxo de pessoas em eventos ou espaços abertos.
