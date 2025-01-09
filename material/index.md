# Design de Software

Boas vindas ao material sobre Design de Software. Aqui você encontrará todo o material de apoio do curso, incluindo links para entrega dos trabalhos.

| Informações Gerais | |
|:--|:--|
| **Turma** | 2025/1 DP-Férias |
| **Professor** | [Humberto Sandmann](https://hsandmann.github.io){:target="_blank"} |
| **Professora Auxiliar** | [Licia Salles](https://github.com/liciascl){:target="_blank"} |
| **Horário** | das 08h às 12h<br>seg-sex |
| **Atendimento** | das 13h30 às 15h<br>ter |

## Links importantes

* [*Blackboard*](https://insper.blackboard.com/){:target="_blank"}: Principalmente utilizado para avisos.
* [*PrairieLearn*](https://us.prairielearn.com/pl/course_instance/168880){:target="_blank"}: Sistema com os exercícios e avaliações da disciplina.
* [*Atendimento Remoto*](https://teams.microsoft.com/l/meetup-join/19%3ameeting_M2ZkN2ZhOTEtOTM4OS00MzEwLThlOTYtNjQwMzRlOGU2YmU5%40thread.v2/0?context=%7b%22Tid%22%3a%226370a6c0-7b90-4709-bd6e-59c28ede833b%22%2c%22Oid%22%3a%225d87fcea-f08e-4d66-8277-5a3d97d593dc%22%7d){:target="_blank"}: Link para atendimento remoto.
<!-- * [*Regras da disciplina*](about.md): Critérios para aprovação. Leia com atenção! -->
<!-- * [*Calendário*](https://www.insper.edu.br/portaldoprofessor/wp-content/uploads/2015/02/CALENDÁRIO-ACADÊMICO-PROFESSOR-ENG-v2-1.pdf){:target="_blank"}: - Calendário do Insper. -->

## Datas importantes

#### Janeiro - DP Férias
| D  | S  | T  | Q  | Q  | S  | S  |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|    |    | 07 | 08 | <span class='quiz'>09</span> | 10 |    |
|    | <span class='quiz'>13</span> | <span class='ep1'>14</span> | <span class='quiz'>15</span> | <span class='p1'>16</span> |  17  |
|    | <span class='ep2'>20</span> | <span class='quiz'>21</span> | 22 | 23 | <span class='quiz'>24</span> |    |
|    | 27 | <span class='epf'>28</span>| <span class='p2'>29</span> |    | <span class='ps'>31</span> |    |

* Quizzes
    * <span class='quiz'>Quiz 1</span>: 09/01
    * <span class='quiz'>Quiz 2</span>: 13/01
    * <span class='quiz'>Quiz 3</span>: 16/01
    * <span class='quiz'>Quiz 4</span>: 21/01
    * <span class='quiz'>Quiz 5</span>: 24/01

* Provas
    * <span class='p1'>Prova 1</span>: 16/01
    * <span class='p2'>Prova 2</span>: 29/01
    * <span class='ps'>Prova substitutiva</span>: 31/01
    <!-- * Prova delta: 28/11 ou 29/11 -->

* Projetos
    * <span class='ep1'>EP1</span>: 08/01 ~ 14/01
    * <span class='ep2'>EP2</span>: 15/01 ~ 20/01
    * <span class='epf'>Final</span>: 21/01 ~ 28/01

**Atendimento:** os atendimentos, a priori, serão feitos remotamente, através do link disponível acima. Os atendimentos ocorrerão nas **terças-feiras**, das **13h30 às 15h**.

## Critérios da Nota

## Composição da Nota

As atividades avaliativas são:

- <span class='quiz'>Quizzes</span>: avaliações rápidas e individuais, com questões objetivas, que ocorrerão ao longo do curso.
- <span class='ep1'>Exercícios Programa - EP</span>: pequenos projetos nos quais serão construídos programas mais elaborados, mas com requisitos
definidos a priori.
- <span class='p1'>Provas</span>: 2 avaliações individuais cujo conteúdo é acumulativo. As Provas 1 e 2 coincidirão com as datas da Avaliação Intermediária
e Avaliação Final do calendário oficial.
- <span class='epf'>Projeto Final - PF</span>: Projeto aberto proposto por um grupo de 2 a 3 membros, com escopos definidos pelo conteúdo ministrado na
disciplina.

### Nota Individual (NI):

A Nota Individual (**NI**) é numérica e composta via média ponderada por 2 provas e quizzes:

- <span class='p1'>Prova 1</span> (Avaliação Intermediária), $30\%$;
- <span class='p2'>Prova 2</span> (Avaliação Final), $60\%$;
- <span class='quiz'>Quizzes</span> (média dos quizzes, descartado o de menor valor), $10\%$.

Ou seja:

$$
NI = 0.3 \times Prova_{1} + 0.6 \times Prova_{2} + 0.1 \times Quizzes
$$

### Nota em Grupo (NG):

A Nota em Grupo (**NG**) é numérica e composta via média ponderada dos:

- <span class='ep1'>EP1</span> (Exercicios Programa 1), $10\%$;
- <span class='ep2'>EP2</span> (Exercicios Programa 2), $20\%$;
- <span class='epf'>Projeto Final - PF</span>, $70\%$.

Tanto os **EPs** quanto o **PF** serão avaliados por conceitos segundo uma determinada rubrica e em seguida convertidos em
nota numérica segundo a tabela oficial da Engenharia.

$$
NG = 0.1 \times EP_1 + 0.2 \times EP_2 + 0.7 \times PF
$$

### Nota Final (NF):

A Nota Final (**NF**) é definida por uma média aritmética entre **NI** e **NG** *se e somente se* **NI** e **NG** forem maiores ou iguais a $5$. Caso
contrário, *a Nota final será a menor nota ente NI e NG*. Ou seja:

$$
\text{Nota Final} = \left\{\begin{array}{lll}
    \text{NI} \geq 5 \bigwedge \text{NG} \geq 5 &
    \implies &
    \displaystyle \frac{ \text{NI} + \text{NG} } {2}
    \\
    \\
    \text{Caso contrário} &
    \implies &
    \min\left(\text{NI}, \text{NG}\right)
    \end{array}\right.
$$

<!-- - Caso a média individual do aluno (média da avaliação intermediária e avaliação final) fique entre 4 e 5, este deverá realizar a
prova delta. A prova delta não aumenta a NI, somente permite a aprovação no caso em que a média individual ficar entre 4 e 5,
e a média aritmética entre NI e NG for maior que 5. -->

