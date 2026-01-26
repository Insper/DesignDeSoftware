# Exercício Programa

O objetivo deste exercício programa (EP) é colocar em prática os conceitos intermediários de programação em ```Python``` em um problema um pouco maior do que os exercícios de aula. **Este EP pode ser feito individualmente ou em duplas e deve utilizar o git para registrar o histórico do código e para fazer a entrega (com contribuições de ambos os membros, no caso de duplas).**

Neste EP você vai implementar o jogo de [dominó](https://pt.wikipedia.org/wiki/Domin%C3%B3), descrito a seguir.

## Regras do jogo

O jogo pode ser jogado por $2$, $3$ ou $4$ participantes. No início do jogo, cada participante recebe $7$ peças de dominó para iniciar o jogo. No total são $28$ peças, onde cada peça é uma combinação de dois números entre $0$ a $6$, sem repetições. São peças:

```python
[0|0], [0|1], [0|2], [0|3], [0|4], [0|5], [0|6],
[1|1], [1|2], [1|3], [1|4], [1|5], [1|6], [2|2],
[2|3], [2|4], [2|5], [2|6], [3|3], [3|4], [3|5],
[3|6], [4|4], [4|5], [4|6], [5|5], [5|6], [6|6]
```

### Início do jogo:
1. Todas as peças são misturadas, ou seja, assumem posições aleatórias;
2. Define-se o número de jogadores: $2$, $3$ ou $4$;
3. Cada jogador recebe $7$ peças; se houver menos de $4$ jogadores, então, as peças remanecentes devem ir para o **monte**;
4. Aleatoriamente um dos jogadores inicia o jogo, colocando uma peça sobre a mesa;
5. Vez do próximo jogador.

### Movimentos possíveis:

1. Na vez de um jogador, esse deve observar as peças posicionadas nas pontas da montagem sobre a mesa e seus valores;
2. O jogador deve escolher uma peça de sua posse que tenha um dos números de alguma das pontas das peças da mesa;
3. Se tiver uma peça possível, então, o jogador deve colocar a peça na mesa e está encerrada sua jogada nessa rodada;
4. Caso o jogador não tenha peças possíveis para a mesa, então, se houver **monte**, deve pegar uma do monte. 
5. O passo $4$ deve ser repetido até que o jogador tenha uma peça que cumpra o passo $2$.
6. Caso o jogador não tenha peça possível e também esteja esgotado o **monte**, então, esse deve passar sua vez para o próximo jogador.

### Da vitória:

1. O jogador vitorioso é aquele que conseguir colocar todas suas peças na mesa, respeitando as regras dos valores das pontas, antes dos demais jogadores;
2. Quanto algum jogador ganhar, o jogo deve parar e o vencedor deve ser anunciado.

### Do empate:

1. Existe a possibilidade de nenhum jogador colocar peças em toda uma rodada, isso porque o jogo pode estar fechado e sem **monte**. Nesse caso, o jogo está encerrado;
2. Para efeito de vitória, os participantes devem contar os valores das faces das peças em sua posse;
3. Ganha o jogador que tiver a menor contagem de pontos, sendo possível empate.

### Da automação de jogadores:

1. O jogador **humano** deve escolher as peças que irá colocar sobre a mesa, ou seja, a cada jogada esse jogador deve escolher as peças e, se for o caso, ser informado do **monte** ou **pulo** da vez;
2. Todo os demais jogadores devem ser automatizados, ou seja, o computador deve jogar por eles. A estratégia de escolha de peças para um jogador automatizado pode ser qualquer uma desde que respeite as regras do jogo, destacadas em [**movimentos possíveis**](#movimentos-possíveis) (dica: utilize estratégia aleatória dos possíveis inicialmente).

## O que você precisa fazer

:::admonition{type=info title="Exemplo Jogável"}
[Veja um exemplo do que é esperado no EP2 neste link.](https://hsandmann.github.io/domino/)
:::

Você deve implementar uma versão para terminal (console) do jogo de dominó, ou seja, usando `#!python print` e `#!python input` para interagir com o usuário por meio de texto. 

Para te auxiliar nessa tarefa, nós criamos os seguintes exercícios (o resultado dos exercícios na Academia Python não afetam a nota, mas as funções criadas neles devem ser utilizadas no EP2):

- :challenge{type=code slug=212-ep2-cria-pecas}
- :challenge{type=code slug=212-ep2-inicia-jogo}
- :challenge{type=code slug=212-ep2-verifica-ganhador}
- :challenge{type=code slug=212-ep2-conta-pontos}
- :challenge{type=code slug=212-ep2-posicoes-possiveis}
- :challenge{type=code slug=212-ep2-adiciona-na-mesa}

:::admonition{type=danger title="Importante"}
As funções enviadas para os exercícios acima devem ser utilizadas pelo seu programa no EP. Crie um arquivo para adicionar essas funções. A cada modificação nesse arquivo, faça um novo commit. Assim, a evolução do programa fica registrada.
:::

Leia também a rubrica atentamente, pois ela pode te ajudar a entender o que precisa ser feito.

## Rubrica

A tabela a seguir apresenta os requisitos esperados e seus respectivos conceitos associados para os objetivos de aprendizagem **desenvolver de programas de computador** e **identificar e desenhar estratégias algorítmicas computacionais**. Esta tabela deve ser considerada em conjunto com a tabela do objetivo **atuar em uma equipe autogerenciada de desenvolvimento**.

| Conceito  |       I                                                |                                                                        D                                                                                                        |                                      C                                            |                                                                                                                                          B                                                                                                                                                                        |                                                                                                                                               A                                                                                                                                                |
| --------- | :----------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :-------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| Descrição | Não entregou ou não entregou as 6 funções funcionando. | Entregou todas as 6 funções obrigatórias (você pode, e deve, utilizar mais funções, mas as funções listadas no enunciado são obrigatórias) mas não há programa ou não funciona. | Entregou as 6 funções obrigatórias funcionando e o programa funciona minimamente. | O programa funciona conforme o esperado, o jogo sempre apresenta para o jogador o estado atual das suas peças e das peças sobre a mesa, é apresentada uma mensagem ao final de cada jogo indicando se o jogador ganhou ou perdeu e o jogador pode iniciar um novo jogo sem ter que executar o programa novamente. | Atingiu o conceito B, implementou validações para as entradas do usuário (digitou posições válidas, verifica se o movimento pode ser realizado, etc.) e implementou alguma forma de visualização mais avançada (ex: cores diferentes para cada naipe, desenhou as cartas com ASCII art, etc.). |

A tabela a seguir apresenta a rubrica do objetivo **atuar em uma equipe autogerenciada de desenvolvimento**.

| Conceito  |       I       |                                     D                                      |                                                           C                                                           |                                                    B                                                    |                                                                                            A                                                                                             |
| --------- | :-----------: | :------------------------------------------------------------------------: | :-------------------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| Descrição | Não entregou. | Não possui nenhum commit próprio e nenhuma evidência de trabalho em grupo. | O grupo enviou todo o código de uma vez para o git (em um ou poucos commits enviados em um intervalo curto de tempo). | Todos os membros do grupo enviaram commits com partes do código, mas a evolução do código é artificial. | O grupo fez bom uso do git, enviando commits a cada funcionalidade implementada ou bug corrigido. Os commits são distribuídos ao longo de alguns dias, mostrando a evolução do trabalho. |

**O conceito final do EP será dado pelo menor entre os conceitos obtidos para cada objetivo acima.** Ou seja, se você obtiver conceito C no primeiro objetivo e A no segundo, o conceito final será C. Se você obtiver conceito A+ no primeiro objetivo, mas não possuir nenhum commit e nenhuma outra evidência de trabalho em grupo (conceito D), seu conceito final será D.

## Entrega

O endereço do seu repositório deve ser enviado pelo Blackboard. Será considerado o último commit antes do horário de entrega. **Em caso de duplas, ambos devem enviar o mesmo endereço no Blackboard.**

**O prazo é 31/01 às 23:59**
