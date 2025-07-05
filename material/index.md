# Design de Software

Boas vindas ao material sobre Design de Software. Aqui você encontrará todo o material de apoio do curso, incluindo links para entrega dos trabalhos.

## Informações Gerais

|  | Turma Férias |
|:--|:--|
| **Professor** | Maciel Vidal |
| **Auxiliar** | Elisa Malzoni |
| **Horário** | 08:00 às 10:00 e 10h00 às 12h00<br>segunda à sexta<br>09/07 é feriado (sem aula) |
| **Atendimento** | 12h30 às 14h00 nos dias:<br>01/jul, 02/jul, 03/jul,<br>07/jul, 08/jul, 10/jul,<br>14/jul, 15/jul, 16/jul, 17/jul,<br>21/jul.|

## Links importantes

* [*Blackboard*](https://insper.blackboard.com/){:target="_blank"}: Principalmente utilizado para avisos.
* [*PrairieLearn*]({{pl_root}}){:target="_blank"}: Sistema com os exercícios e avaliações da disciplina.
<!-- * [*Regras da disciplina*](about.md): Critérios para aprovação. Leia com atenção! -->
<!-- * [*Calendário*](https://www.insper.edu.br/portaldoprofessor/wp-content/uploads/2015/02/CALENDÁRIO-ACADÊMICO-PROFESSOR-ENG-v2-1.pdf){:target="_blank"}: - Calendário do Insper. -->

## Datas importantes

* Quizzes
    * <span class='quiz'>Quiz 1</span>: 03/07 (Input, Funções e Condicionais)
    * <span class='quiz'>Quiz 2</span>: 07/07 (Estruturas de Repetição)
    * <span class='quiz'>Quiz 3</span>: 10/07 (Listas)
    * <span class='quiz'>Quiz 4</span>: 16/07 (Dicionário)
    * <span class='quiz'>Quiz 5</span>: 18/07 (Strings)

* Provas
    * <span class='p1'>Avaliação Intermediária</span>: 11/07
    * <span class='p2'>Avaliação Final</span>: 22/07
    * <span class='ps'>Avaliação substitutiva</span>: 25/07

* Projetos
    * <span class='ep1'>EP1</span>: 08/07 23h59
    * <span class='ep2'>EP2</span>: 14/07 23h59
    * <span class='epf'>Final</span>: 23/07 12h00

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
- <span class='ep2'>EP2</span> (Exercicios Programa 2), $30\%$;
- <span class='epf'>Projeto Final - PF</span>, $60\%$.

Tanto os **EPs** quanto o **PF** serão avaliados por conceitos segundo uma determinada rubrica e em seguida convertidos em
nota numérica segundo a tabela oficial da Engenharia.

A entrega dos **EPs** e do **PF** é obrigatória e o aluno deve obter nota pelo menos **4** em cada um deles. Caso contrário, a *Nota em Grupo será a menor nota entre os EPs e PF*. Considere a seguinte fórmula para cálculo da nota em grupo:

$$
\text{NG} = \left\{\begin{array}{lll}
    EP_1 \geq 4 \bigwedge EP_2 \geq 4 \bigwedge PF \geq 4 &
    \implies & 0.1 \times EP_1 + 0.3 \times EP_2 + 0.6 \times PF
    \displaystyle 
    \\
    \\
    \text{Caso contrário} &
    \implies &
    \min\left(EP_1, EP_2, PF\right)
    \end{array}\right.
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

