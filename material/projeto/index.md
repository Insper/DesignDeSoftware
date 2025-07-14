# Projeto Final

## Objetivo do Projeto

Desenvolvimento de um jogo de computador em Python 3 usando recursos da biblioteca PyGame, dentre outras. O programa deverá ser interativo, permitindo um ou mais jogadores interagirem em um jogo com objetivo bem definido. O desenvolvimento deverá ser feito em grupos de 3 alunos, usando o Git como sistema de versionamento. O tema do jogo é livre, contudo, a proposta deve ser previamente discutida com o professor.

O objetivo é colocar em prática o que você aprendeu sobre programação com Python e desenvolver mais suas habilidade de aprender a aprender e de trabalhar em uma equipe autogerenciada de software. Por esse motivo, será necessário que você utilize funcionalidades que não vimos em nenhuma aula.

!!! info "Projetos de semestres passados"

    Se estiver em busca de inspiração, confira os jogos desenvolvidos em semestres anteriores:

    - 2020-1: https://jogos-digitais.s3.amazonaws.com/2020/0622Projetos-Design-Software.html
    - 2020-2: https://jogos-digitais.s3.amazonaws.com/2020/1204projetosDessoft.html

## Grupos

Grupos: **duplas** ou **trios**.

Acesse o link para criar o grupo https://classroom.github.com/a/eR0h3yEZ

O primeiro membro de cada grupo cria o grupo, enquanto os demais apenas entram no grupo.

## Entrega

O projeto terá duas entregas:

1. Formulário com a proposta inicial do projeto (pode mudar um pouco depois, mas é importante definir uma direção).

Envie no BlackBoard (não perca o prazo).

Data de entrega da proposta inicial do projeto: **17/07/2024**.

2. Entrega final do projeto. Entrega utilizando o repositório do classroom.

Data de entrega: **23/07/2024 12h00 (meio-dia)**

O repositório deverá conter um arquivo `README.md` com, **no mínimo**, o seguinte conteúdo:

1. Título do projeto;
2. Descrição do projeto;
3. Nomes dos membros do seu grupo;
4. Nomes dos membros;
5. Explicação de como rodar o jogo;
6. Endereço de um **vídeo curto** apresentando o seu jogo (você pode colocar o vídeo onde preferir: YouTube, Vimeo, GoogleDrive, etc. mas o professor precisa ter acesso através do link). Esse vídeo (pode ser de um a cinco minutos) deve mostrar o seu projeto funcionando.
7. Preenchimento da rubrica.

Recomendamos que vocês também incluam no `README.md` instruções de como instalar as dependências (se usar alguma biblioteca adicional, como o PyGame). Esses pontos são recomendados em qualquer projeto.

!!! info "Indo além..."

    Se quiser saber mais sobre Markdown, veja este link: https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet

    Confira também estas dicas de como escrever um bom README: https://www.freecodecamp.org/news/how-to-write-a-good-readme-file/

## Aviso

Os projetos serão examinados com fontes da internet e os projetos de outros alunos. Se você se basear em algum código da Internet, **deixe claro de onde pegou e dê os créditos**. É normal você buscar exemplos na internet para entender como funciona uma ferramenta, o que não é aceitável é **copiar longos trechos de código** e não dar crédito. Se forem poucas linhas, 3 ou 4 por exemplo, você não precisa referenciar, se for muito mais que isso, diga de onde pegou. Já usar projetos de colegas é mais crítico, **não copie código de seus colegas**, é sempre saudável conversar para ter e dar ajuda, mas não dar código pronto.

Existe um documento no Blackboard (Orientações sobre integridade intelectual em atividades de programação) com mais detalhes. Se tiver alguma dúvida pergunte para o seu professor.

Caso você utilize um trecho de código da internet, adicione um comentário no seu código: `Código extraído de https://endereco.de.onde.voce.pegou.o.codigo.com.br`.

## Nota

A nota do projeto será dada pelo seguinte critério:

- Se a equipe obteve conceito I ou D em algum objetivo de aprendizado, o conceito final será dado pelo menor conceito obtido. Por exemplo: se todas as features foram implementadas, e o código está impecável, mas um aluno fez tudo (conforme evidenciado no git), a nota será D (ou até mesmo I).
- Se todos os conceitos forem iguais ou superiores a C, o conceito final será obtido pela média ponderada dos conceitos obtidos para os objetivos de aprendizado:

  $$0.25 * Objetivo 1 + 0.5 * Objetivo 2 + 0.25 * Objetivo 3$$

### Rubrica

A tabela a seguir apresenta os requisitos esperados e seus respectivos conceitos associados para os 3 objetivos de aprendizagem.

#### Objetivo 1: Desenvolver programas de computador

| Conceito  |                                                                                   I                                                                                   |                                                                                      D                                                                                       |                                                                                                        C                                                                                                        |                                                                                                                                                                                            B                                                                                                                                                                                             |                                                                                                                                                                      A                                                                                                                                                                       |
| --------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| Descrição | Código não roda, mesmo havendo algumas rotinas sem erros de sintaxe, não é possível uma execução completa. Documentação basicamente nula, nem no código, nem externa. | Código apresenta erros de sintaxe que inviabilizam o uso do programa de forma completa. Embora haja alguns comentários no código, esses não permitem minimamente entendê-lo. | O código é funcional e faz o que se propõe fazer, código não apresenta erros de sintaxe. Existe uma documentação em algumas linhas de código, porém alguns blocos de código não possuem descrição do que fazem. | Código organizado em uma série de funções que permitem uma clara compreensão da estratégia do jogo. Os principais blocos de código estão documentados de forma clara. Rotinas não possuem chamadas inúteis. Disponibilizou um arquivo README contendo as informações básicas solicitadas no enunciado. | Atingiu o conceito B. Código organizado de forma apropriada em orientação a objetos de forma que auxilia a compreensão, reuso e manutenção do código. Separou responsabilidades em arquivos diferentes. Código documentado com [docstrings](https://realpython.com/documenting-python-code/). Rotinas são eficientes e sem chamadas inúteis. |

#### Objetivo 2: Identificar e programar estratégias computacionais de resolução de problemas práticos

| Conceito  |                                                        I                                                         |                                                                    D                                                                    |                                                                                                          C                                                                                                          |                                                                                                                                                                                    B                                                                                                                                                                                     |                                                                                                                                                                                                                    A                                                                                                                                                                                                                     |
| --------- | :--------------------------------------------------------------------------------------------------------------: | :-------------------------------------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| Descrição | Jogo não apresenta uma jogabilidade mínima. Não há interações que funcionem como esperado para um jogo 2D ou 3D. | Possível visualizar uma cena de jogo, porém não possui nenhum recurso de interação incorporado. Basicamente é um passeio em um cenário. | Foi criado um jogo que possui apenas uma ou duas telas. O jogo possui algumas formas de interação, mas não em tempo real (ou seja, não são ações instantâneas com fazer um personagem pular ou clicar em um botão). | O programa desenvolvido permite a interação com vários objetos (gráficos) na cena de forma coerente com a proposta do jogo. Mais de uma tela é apresentada para o usuário, incluindo telas informativas e tela de início e fim). Possui um som ambiente e/ou de efeito sonoro de personagens. Diferentes interações em tempo real são possíveis. Aplicativo está fluido. | Atingiu o conceito B. Cenário elaborado com riqueza de detalhes e objetos do jogo possuem animações. O jogo possui um bom acabamento, se aproximando de um produto. Serão aceitos jogos menos acabados no caso de utilização de algum recurso avançado como comunicação por rede ou outros dispositivos externos (ex: controles, câmeras, etc.). Som presente no jogo de diversas formas. Jogo está fluido e não trava em momento algum. |

#### Objetivo 3: Atuar em uma equipe de desenvolvimento de software

| Conceito  |                                                                                                        I                                                                                                        |                                                                                                                                                                            D                                                                                                                                                                            |                                                                                                                                                C                                                                                                                                                 |                                                                                  B                                                                                  |                                                                                                                                                                                                       A                                                                                                                                                                                                       |
| --------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| Descrição | Grupo não conseguiu entregar código pelo Github. O código foi entregue em arquivos sem sentido, e com pedaços de código inútil e/ou ilegível. Implementação do jogo foi muito limitada para o tamanho do grupo. | Grupo conseguiu entregar código pelo Github, porém possuíam commits só de um usuário e limitado a um número reduzido de commits. Os arquivos entregues não possuíam uma organização básica. Implementação do jogo foi limitada para o tamanho do grupo. **OU** Não existem evidências de que o aluno teve alguma contribuição significativa no projeto. | Código entregue pelo Github, porém se percebe uma contribuição forçada, pois o código relevante foi postado por basicamente um usuário. Implementação do jogo proposto foi mínima para o tamanho do grupo. **OU** O aluno não preencheu mais de um dos formulários de acompanhamento do projeto. | Código entregue pelo Github, onde se percebe uma contribuição balanceada dos membros do grupo. Implementação do jogo proposto foi adequada para o tamanho do grupo. | Código entregue pelo Github, onde se percebe uma contribuição balanceada dos membros do grupo. Além do código se percebe que os membros do grupo trabalharam juntos em outros evidências de discussão do projeto, como o design do jogo (se tiverem rascunhos, coloquem no README), geração e coleta de imagens (sprites), etc. Implementação do jogo proposto foi acima do esperado para o tamanho do grupo. |

## Cronograma sugerido para o conceito B no Objetivo 2

Esta é uma sugestão de organização para o projeto de vocês. Lembrem-se que um dos objetivos é trabalhar em uma equipe autogerenciada de desenvolvimento de software. Assim, vocês devem se organizar da maneira que acharem melhor. A sugestão abaixo é mais um guia para saberem se estão atrasados (será difícil atingir o conceito B fazendo muito menos do que isso), em dia, ou avançados (buscando o conceito A).

- Até 18/07: handout de PyGame concluído, projeto definido e uma primeira tela com interações iniciais funcionando (sem animações, apenas imagens estáticas se movendo pela tela). Por exemplo, em um jogo de plataforma isso significaria mover o personagem com o teclado e fazer ele perder vida/morrer ao encostar em um inimigo;
- Até 19/07: mecânica básica do jogo concluída e início da implementação de outras telas e recursos sonoros;
- Até 20/07: mecânica do jogo concluída (incluindo recursos interativos adicionais, como _power-ups_, vidas, movimentação dos inimigos - caso se aplique) e navegação entre telas funcionando;
- Até 23/07: projeto concluído com os requisitos do conceito B.

## Exemplo

Cada projeto possui um nível diferente de dificuldade. Por exemplo, é esperado que um jogo com implementação mais simples seja mais bem finalizado do que um jogo com uma lógica mais complexa. Por esse motivo, a lista abaixo deve ser considerada apenas como um guia do que é esperado no jogo ao final da disciplina, mas é importante que você converse com os professores para entender melhor as expectativas para o seu projeto:

- Tela de menu/início de jogo e tela de final de jogo;
- Múltiplas fases;
- Contagem de pontuação e/ou vida;
- Algum tipo de animação;
- Algum tipo de efeito sonoro/fundo musical;
- Outros detalhes específicos de cada jogo (exemplos: inimigos que seguem o jogador, power-ups, telas de instrução, telas de história, botão de pause, ...)
