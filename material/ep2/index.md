# Exercício Programa 2

O objetivo deste exercício programa (EP) é colocar em prática os conceitos intermediários de programação em ```Python``` em um problema um pouco maior do que os exercícios de aula. **Este EP deve ser feito em duplas e utilizar o git para registrar o histórico do código e para fazer a entrega (com contribuições de ambos os membros).**

Neste EP você vai implementar o jogo de **Fortuna DesSoft**, descrito a seguir.

## Regras do jogo

Você irá implementar um jogo de perguntas e respostas. Cada pergunta tem quatro alternativas e, conforme o jogador responde as perguntas corretamente, tem seu prêmio aumentado. Caso o jogador erre alguma resposta, perde o prêmio e sai sem nada! O jogo acaba quando o jogador atingir o prêmio de **1 milhão** ou escolher parar!

### Descrição geral dos passos do jogo:
1. O jogador deve informar seu nome;
2. O computador exibe um pequeno manual do jogo;
3. Inicia-se o jogo de perguntas e respostas;
4. O computador sorteia uma pergunta aleatória inédita, exibindo a questão e as opções de resposta;
5. O usuário escolhe entre as opções: `A`, `B`, `C`, `D`, `pula` ou `ajuda`;
6. Caso o jogador opte por `ajuda`, sorteie aleatoriamente uma ou duas (quantidade aleatória) respostas sabidamente incorretas e dê a dica de que estas são sabidamente erradas!
7. Caso o jogador opte por `pula`, se o jogador ainda tiver pulos disponíveis, volte ao passo **4**, senão informe que não tem mais pulos e exiba a pergunta novamente
8. Caso o jogador escolha uma resposta correta, o seu prêmio aumenta. Considere que o usuário inicia com zero reais e que sua premiação aumenta conforme a lista:
    ```python
    1000
    5000
    10000
    30000
    50000
    100000
    300000
    500000
    1000000
    ```
9. Caso o jogador escolha uma resposta errada, o jogo acaba e ele sai sem nenhum prêmio!
10. Pergunte se o jogador quer parar ou continuar. 

### Observações:
- Inicialmente, o jogador tem direito a `3` pulos e `2` ajudas;
- O jogo deve validar se a base de dados está consistente;
- O jogo não deve sortear perguntas repetidas;
- no passo **5**, valide se o usuário escolheu alguma opção inexistente;
- no passo **6**, não é possível pedir ajuda mais de uma vez. Valide e exiba mensagem adequada;

### Da vitória:

1. O jogo acaba quando o jogador atingir o prêmio de 1 milhão. Após cada pergunta correta, o jogador tem a opção de parar e sair com o prêmio já conquistado.

## O que você precisa fazer

:::admonition{type=info title="Exemplo do Jogo"}
[Veja um exemplo do que é esperado no EP2 neste link.](https://macielcalebe.github.io/dessoft-23-2-ferias-exemplo-ep2/)
:::

Você deve implementar uma versão para terminal (console) do jogo, ou seja, usando `#!python print` e `#!python input` para interagir com o usuário por meio de texto. 

Para te auxiliar nessa tarefa, foram criados os seguintes exercícios (o resultado dos exercícios na Academia Python não afetam a nota, mas as funções criadas neles devem ser utilizadas no EP2):

- :challenge{type=code slug=222-dp-ep2-transforma-base}
- :challenge{type=code slug=222-dp-ep2-valida-questao}
- :challenge{type=code slug=222-dp-ep2-valida-lista-questoes}
- :challenge{type=code slug=222-dp-ep2-sorteia-questao}
- :challenge{type=code slug=222-dp-ep2-sorteia-questao-inedita}
- :challenge{type=code slug=222-dp-ep2-questao-para-string}
- :challenge{type=code slug=222-dp-ep2-gera-ajuda}

:::admonition{type=danger title="Importante"}
As funções enviadas para os exercícios acima devem ser utilizadas pelo seu programa no EP2. Dica: crie um arquivo para adicionar essas funções. A cada modificação nesse arquivo, faça um novo commit. Assim, a evolução do programa fica registrada. Faça também um outro arquivo para as função de impressão em tela e validação de entrada de dados.
:::

Ainda, está sendo disponibilizado um arquivo com uma base de perguntas e resposta, que pode ser utilizado no EP. **Sugestão:** incremente a base de dados, criando novas perguntas!

**[Base de Perguntas e Respostas](https://github.com/macielcalebe/dessoft-23-2-ferias-exemplo-ep2)**

Leia também a rubrica atentamente, pois ela pode te ajudar a entender o que precisa ser feito.

## Rubrica

A tabela a seguir apresenta os requisitos esperados e seus respectivos conceitos associados para os objetivos de aprendizagem **desenvolver de programas de computador** e **identificar e desenhar estratégias algorítmicas computacionais**. Esta tabela deve ser considerada em conjunto com a tabela do objetivo **atuar em uma equipe autogerenciada de desenvolvimento**.

| Conceito  |       I       |                                                                        D                                                                        |                                      C                                       |                                                                                                                                          B                                                                                                                                           |                                                                                                                                               A                                                                                                                                                |
| --------- | :-----------: | :---------------------------------------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| Descrição | Não entregou. | Não entregou todas as sete funções obrigatórias (você pode, e deve, utilizar mais funções, mas as funções listadas no enunciado são obrigatórias). | Entregou as sete funções obrigatórias funcionando, mas o programa não funciona. | O programa funciona conforme o esperado, o jogo sempre apresenta para o jogador o estado atual do seu prêmio, é apresentada uma mensagem ao final de cada jogo indicando se o jogador ganhou ou perdeu e o jogador pode iniciar um novo jogo sem ter que executar o programa novamente. | Atingiu o conceito B, implementou validações para as entradas do usuário (digitou respostas válidas), adicionou mais perguntas à base e implementou alguma forma de visualização mais avançada (ex: cor diferente conforme o valor do prêmio ou de acordo com a importância de cada mensagem). |

A tabela a seguir apresenta a rubrica do objetivo **atuar em uma equipe autogerenciada de desenvolvimento**.

| Conceito  |       I       |                                     D                                      |                                                           C                                                           |                                                    B                                                    |                                                                                            A                                                                                             |
| --------- | :-----------: | :------------------------------------------------------------------------: | :-------------------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| Descrição | Não entregou. | Não possui nenhum commit próprio e nenhuma evidência de trabalho em grupo. | O grupo enviou todo o código de uma vez para o git (em um ou poucos commits enviados em um intervalo curto de tempo). | Todos os membros do grupo enviaram commits com partes do código, mas a evolução do código é artificial. | O grupo fez bom uso do git, enviando commits a cada funcionalidade implementada ou bug corrigido. Os commits são distribuídos ao longo de alguns dias, mostrando a evolução do trabalho. |

**O conceito final do EP2 será dado pelo menor entre os conceitos obtidos para cada objetivo acima.** Ou seja, se você obtiver conceito C no primeiro objetivo e A no segundo, o conceito final será C. Se você obtiver conceito A+ no primeiro objetivo, mas não possuir nenhum commit e nenhuma outra evidência de trabalho em grupo (conceito D), seu conceito final será D.

## Grupos

É obrigatório fazer em **Dupla**. Caso não tenha time, entre em contato com o professor por email até o dia 04/07.

Utilize o link https://classroom.github.com/a/Bq8-prUt para criar o grupo e informe seu colega o nome do grupo. Apenas o primeiro membro cria o grupo, o segundo (caso exista) apenas entra no grupo já criado.


## Entrega

**Todos os membros** do grupo devem responder ao questionário https://forms.gle/BoqVJCUwvtabR82p8. Além disso, é obrigatório o envio de um vídeo de até 5 minutos que demonstre seu jogo funcionando (pode ser o mesmo vídeo para a dupla, mas ambos devem enviar o link e responder o formulário).

Não façam commit após a data de entrega, será considerado como atraso.

**O prazo é 18/07 às 23:59**

EPs entregues com atraso terão seu conceito **limitado a D**.
