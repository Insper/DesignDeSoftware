# Design de Software

Boas vindas ao material sobre Design de Software. Aqui você encontrará todo o material de apoio do curso, incluindo links para entrega dos trabalhos.

## Informações Gerais

|  | Turma Férias |
|:--|:--|
| **Professor** | Raul Ikeda |
| **Auxiliar** | Elisa Malzoni |
| **Horário** | 09h30 às 11h30 e 13h00 às 15h00<br>segunda à sexta |
| **Atendimento** | 15h00 às 16h30 todos os dias<br> (exceto dias de AI e AF).|

## Links importantes

* [*Blackboard*]: Principalmente utilizado para avisos.
* [*PrairieLearn*]: Sistema com os exercícios e avaliações da disciplina.
<!-- * [*Blackboard*](https://insper.blackboard.com/ultra/courses/_56034_1/outline){:target="_blank"}: Principalmente utilizado para avisos. -->
<!-- * [*PrairieLearn*](https://us.prairielearn.com/pl/course_instance/219634){:target="_blank"}: Sistema com os exercícios e avaliações da disciplina. -->
<!-- * [*Regras da disciplina*](about.md): Critérios para aprovação. Leia com atenção! -->
<!-- * [*Calendário*](https://www.insper.edu.br/portaldoprofessor/wp-content/uploads/2015/02/CALENDÁRIO-ACADÊMICO-PROFESSOR-ENG-v2-1.pdf){:target="_blank"}: - Calendário do Insper. -->

## Datas importantes

* Quizzes
    * <span class='quiz'>Quiz 1</span>: 08/07 13h00 (Input, Funções e Condicionais)
    * <span class='quiz'>Quiz 2</span>: 14/07 13h00 (Estruturas de Repetição)
    * <span class='quiz'>Quiz 3</span>: 17/07 13h00 (Listas)
    * <span class='quiz'>Quiz 4</span>: 23/07 13h00 (Dicionário)
    * <span class='quiz'>Quiz 5</span>: 27/07 13h00 (Strings)

* Provas
    * <span class='p1'>Avaliação Intermediária</span>: 20/07 09h30
    * <span class='p2'>Avaliação Final</span>: 29/07 09h30
    * <span class='ps'>Avaliação substitutiva</span>: 03/08

* Projetos
    * <span class='ep1'>EP1</span>: 19/07 23h59
    * <span class='ep1'>EP2</span>: 28/07 23h59

## Critérios da Nota

## Composição da Nota

As atividades avaliativas são:

- <span class='quiz'>Quizzes</span>: avaliações rápidas e individuais, com questões objetivas, que ocorrerão ao longo do curso.
- <span class='ep1'>Exercício Programa - EP</span>: pequeno projeto individual no qual será construído um programa mais elaborado, mas com requisitos definidos a priori.
- <span class='p1'>Provas</span>: 2 avaliações individuais cujo conteúdo é acumulativo. As Provas 1 e 2 coincidirão com as datas da Avaliação Intermediária e Avaliação Final do calendário oficial.
<!-- - <span class='epf'>Projeto Final - PF</span>: Projeto aberto proposto por um grupo de 2 a 3 membros, com escopos definidos pelo conteúdo ministrado na disciplina. -->

### Nota de Avaliação (NA):

A Nota de Avaliação (**NA**) é numérica e composta via média ponderada por 2 provas e quizzes:

- <span class='p1'>Prova 1</span> (Avaliação Intermediária), $30\%$;
- <span class='p2'>Prova 2</span> (Avaliação Final), $60\%$;
- <span class='quiz'>Quizzes</span> (média dos quizzes, descartado o de menor valor), $10\%$.

Ou seja:

$$
NA = 0.3 \times Prova_{1} + 0.6 \times Prova_{2} + 0.1 \times Quizzes
$$

### Nota de Projeto (NP):

A Nota de Projeto (**NP**) é numérica e composta via média ponderada dos:

- <span class='ep1'>EP1</span> (Exercicio-Programa), $40\%$;
- <span class='ep1'>EP2</span>, $60\%$.
<!-- - <span class='epf'>Projeto Final - PF</span>, $70\%$. -->

Tanto o **EP1** quanto o **EP2** serão avaliados por conceitos segundo uma determinada rubrica e em seguida convertidos em
nota numérica segundo a tabela oficial da Engenharia.

As entregas do **EP1** e do **EP2** são obrigatórias e o aluno deve obter nota pelo menos **4** em cada um deles. Caso contrário, a *Nota de Projeto será a menor nota entre o EP1 e EP2*. Considere a seguinte fórmula para cálculo da nota de projeto:

$$
\text{NP} = \left\{\begin{array}{lll}
    EP1 \geq 4 \bigwedge EP2 \geq 4 &
    \implies & 0.4 \times EP1 + 0.6 \times EP2
    \displaystyle 
    \\
    \\
    \text{Caso contrário} &
    \implies &
    \min\left(EP1, EP2\right)
    \end{array}\right.
$$

### Nota Final (NF):

A Nota Final (**NF**) é definida por uma média aritmética entre **NA** e **NP** *se e somente se* **NA** e **NP** forem maiores ou iguais a $5$. Caso contrário, *a Nota final será a menor nota ente NA e NP*. Ou seja:

$$
\text{Nota Final} = \left\{\begin{array}{lll}
    \text{NA} \geq 5 \bigwedge \text{NP} \geq 5 &
    \implies &
    \displaystyle \frac{ \text{NA} + \text{NP} } {2}
    \\
    \\
    \text{Caso contrário} &
    \implies &
    \min\left(\text{NA}, \text{NP}\right)
    \end{array}\right.
$$

<!-- - Caso a média individual do aluno (média da avaliação intermediária e avaliação final) fique entre 4 e 5, este deverá realizar a
prova delta. A prova delta não aumenta a NI, somente permite a aprovação no caso em que a média individual ficar entre 4 e 5,
e a média aritmética entre NI e NG for maior que 5. -->
