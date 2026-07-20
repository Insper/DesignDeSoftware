# Exercício Programa - Fortuna DesSoft!

**Este EP deve ser feito individualmente e deve utilizar o github para registrar o histórico do código e para fazer a entrega.**

**É necessário utilizar o github e fazer commits ao longo do desenvolvimento do projeto.**

O objetivo deste exercício programa (EP) é colocar em prática os conceitos intermediários de programação em ```Python``` em um problema um pouco maior do que os exercícios de aula. **Este EP deve ser feito individualmente e utilizar o git para registrar o histórico do código e para fazer a entrega (com contribuições parciais).**

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

<div style="background-color: #fff3cd; color: #856404; padding: 12px; border-left: 5px solid #ffeeba; border-radius: 4px;">
<a href="https://macielcalebe.github.io/dessoft-ferias-exemplo-ep2/">Veja um exemplo do que é esperado no EP2 <strong>neste link</strong></a>
</div>

Você deve implementar uma versão para terminal (console) do jogo, ou seja, usando `#!python print` e `#!python input` para interagir com o usuário por meio de texto. 

Para te auxiliar nessa tarefa, foram criados os seguintes exercícios (o resultado dos exercícios na Academia Python não afetam a nota, mas as funções criadas neles devem ser utilizadas no EP2):

- **EP2 Transforma Base**
- **EP2 Valida Questão**
- **EP2 Valida Lista de Questões**
- **EP2 Sorteia Questão**
- **EP2 Sorteia Questão Inedita**
- **EP2 Questão para String**
- **EP2 Gera Ajuda**

**Atenção**: As funções enviadas para os exercícios acima devem ser utilizadas pelo seu programa no **EP2**. Dica: crie um ou mais arquivos para adicionar essas funções. A cada modificação nesse arquivo, faça um novo commit. Assim, a evolução do programa fica registrada. As função de impressão em tela e validação de entrada de dados podem ficar em arquivos separados.

Ainda, está sendo disponibilizado um arquivo com uma base de perguntas e resposta, que pode ser utilizado no EP. **Sugestão:** incremente a base de dados, criando novas perguntas!

**[Base de Perguntas e Respostas](https://github.com/macielcalebe/dessoft-ferias-exemplo-ep2/blob/main/lib_questoes.py)**

Leia também a rubrica atentamente, pois ela pode te ajudar a entender o que precisa ser feito.

## Rubrica

A tabela a seguir apresenta os requisitos esperados e seus respectivos conceitos associados para os objetivos de aprendizagem **desenvolver de programas de computador** e **identificar e desenhar estratégias algorítmicas computacionais**. 

| Conceito  |       I       |                                                                        D                                                                        |                                      C                                       |                                                                                                                                          B                                                                                                                                           |                                                                                                                                               A                                                                                                                                                |
| --------- | :-----------: | :---------------------------------------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| Descrição | Não entregou. | Não entregou todas as sete funções obrigatórias (você pode, e deve, utilizar mais funções, mas as funções listadas no enunciado são obrigatórias). | Entregou as sete funções obrigatórias funcionando, mas o programa não funciona. | O programa funciona conforme o esperado, o jogo sempre apresenta para o jogador o estado atual do seu prêmio, é apresentada uma mensagem ao final de cada jogo indicando se o jogador ganhou ou perdeu e o jogador pode iniciar um novo jogo sem ter que executar o programa novamente. | Atingiu o conceito B, implementou validações para as entradas do usuário (digitou respostas válidas), adicionou mais perguntas à base e implementou alguma forma de visualização mais avançada (ex: cor diferente conforme o valor do prêmio ou de acordo com a importância de cada mensagem). |

## Entrega

Você irá criar um repositório e entregar o endereço deste repositório no Blackboard.

Além disso, é **obrigatório** o envio via Blackboard de um **vídeo de até 5 minutos** que demonstre seu jogo funcionando.

Não façam commit após a data de entrega, será considerado como atraso.

**O prazo é 28/07 às 23:59**

EPs entregues com atraso terão seu conceito **limitado a D** (sem garantia de que será aceito, caso ocorra atraso, converse com os professores de forma urgente).