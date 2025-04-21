# Exercício Programa - Yacht Dice

**Este EP pode ser feito individualmente ou em duplas e deve utilizar o github para registrar o histórico do código e para fazer a entrega (com contribuições de ambos os membros, no caso de duplas).**

**Caso faça em dupla, defina quais exercícios cada integrante ficará responsável.**

**Caso faça individualmente, ainda é necessário utilizar o github e fazer commits ao longo do desenvolvimento do projeto.**

Para exercitar nossas habilidades com programação, vamos desenvolver o jogo *Yacht Dice*.

Nesse jogo, o objetivo do jogador é rolar os dados e tentar obter a maior pontuação possível. O jogador pode escolher quais dados manter e quais rolar novamente, com o objetivo de formar combinações específicas.

## O jogo

O jogo é jogado com 5 dados em rodadas. Em cada rodada o jogador tem 3 chances de rolar os dados. Após cada rolagem, o jogador pode escolher quais dados manter e quais rolar novamente. O jogador pode escolher entre várias combinações de pontuação, como "sequências", "dados iguais" ou "soma de dados". O jogador deve tentar obter a maior pontuação possível em cada rodada. Ao final de cada rodada, o jogador escolhe uma combinação que esteja disponível na cartela de pontos e marca a pontuação correspondente. O jogo termina quando o jogador preenche todas as combinações disponíveis na cartela de pontos. Ao final de cada rodada, o jogador é obrigado a escolher uma das combinações disponíveis, mesmo que não tenha obtido uma boa pontuação.

Veja o exemplo de uma rodada sendo jogada:

<img src="img/exemplo_jogada.gif" alt="Rodada do jogo" width="80%" />

___

Você deve implementar uma versão para terminal (console) do jogo, ou seja, usando `print` e `input` para interagir com o usuário por meio de texto.

Para te auxiliar nessa tarefa, foram criados exercícios no PrairieLearn que te ajudarão a implementar as funções necessárias para o jogo.

Se quiser jogar uma partida para entender melhor o jogo, você pode acessar o site [https://cardgames.io/yahtzee/](https://cardgames.io/yahtzee/).

## Desenvolvimento do projeto

- Crie um repositório **público** no github para o seu projeto e adicione sua dupla caso haja.
- Cada exercício feito com sucesso no PrairieLearn deve ser adicionado ao repositório em um commit separado no mesmo dia. Dica: crie um arquivo para adicionar essas funções. A cada modificação nesse arquivo, faça um novo commit. Assim, a evolução do programa fica registrada.
- As funções enviadas no PrairieLearn devem ser utilizadas pelo seu programa no EP2. Faça um outro arquivo para o programa que será responsável pela impressão em tela e validação de entrada de dados.

Leia também a rubrica atentamente, pois ela irá te ajudar a entender o que precisa ser feito.

## Rubrica

A tabela a seguir apresenta os requisitos esperados e seus respectivos conceitos associados para os objetivos de aprendizagem **desenvolver de programas de computador** e **identificar e desenhar estratégias algorítmicas computacionais**. Esta tabela deve ser considerada em conjunto com a tabela do objetivo **atuar em uma equipe autogerenciada de desenvolvimento**.


### Conceito I
Não entregou

### Conceito D
Não submeteu com sucesso no PrairieLearn ou não fez o commit de alguma das funções a seguir:

- Rolar dados
- Guardar dado
- Remover dado
- Calcula pontos na regra simples
- Calcula pontos na regra avançada - Soma
- Calcula pontos na regra avançada - Sequência baixa
- Calcula pontos na regra avançada - Sequência alta

### Conceito C
Submeteu com sucesso no PrairieLearn **E** fez o commit das funções anteriores e das funções a seguir:

- Calcula pontos na regra avançada - Full House
- Calcula pontos na regra avançada - Quadra

### Conceito B
Atingiu o conceito C
E submeteu com sucesso no PrairieLearn **E** fez o commit das funções a seguir:


- Calcula pontos na regra avançada - Quina
- Calcula pontos na regra avançada
- Faz jogada

### Conceito A
Atingiu o conceito B
E submeteu com sucesso no PrairieLearn **E** fez o commit do exercício a seguir:

- Jogo

### Conceito A+
Atingiu o conceito A e existem exatamente 2 arquivos no repositório (um para as funções e outro para o código do jogo). Além disso, as funções estão sendo importadas do arquivo que contém as definições das funções e não foram copiadas para o arquivo do programa.
___

A tabela a seguir apresenta a rubrica do objetivo **atuar em uma equipe autogerenciada de desenvolvimento**.

| Conceito  |  Descrição |
| --------- | :--------: |
| I        | Não entregou. |
| D        | Não possui nenhum commit próprio e nenhuma evidência de trabalho em grupo. |
| C        | O grupo enviou todo o código de uma vez para o git (em um ou poucos commits enviados em um intervalo curto de tempo). |
| B        | Todos os membros do grupo enviaram commits com partes do código, mas a evolução do código é artificial. |
| A        | O grupo fez bom uso do git, enviando commits a cada funcionalidade implementada ou bug corrigido. Os commits são distribuídos ao longo de alguns dias, mostrando a evolução do trabalho. |



**O conceito final do EP2 será dado pelo menor entre os conceitos obtidos para cada objetivo acima.** Ou seja, se você obtiver conceito C no primeiro objetivo e A no segundo, o conceito final será C. Se você obtiver conceito A+ no primeiro objetivo, mas não possuir nenhum commit e nenhuma outra evidência de trabalho em grupo (conceito D), seu conceito final será D.

## Entrega 06/05 até 23:59
Será considerado o código enviado para o github até a data de entrega.

O endereço do seu repositório deve ser enviado pelo Blackboard. Não façam commits após a data de entrega, pois será considerado como atraso.

**Importante:** Caso algum integrante da dupla esqueça de enviar o endereço do repositório, será descontado conceito da nota final do projeto.
