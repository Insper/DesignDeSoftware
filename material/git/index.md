# Controle de versões com Git

## Introdução

Imagine que um grupo de alunos vai desenvolver um projeto de software em grupo para a matéria de Design de Software (por exemplo, um exercício programa? Um projeto final? #ficadica).

O grupo consiste de três alunos: Astrogibalda Afobada, Baracobama Boêmio, e Cacá Confuso. Após dividir as tarefas do sprint entre si, o grupo começa a desenvolver o código. Afobada já começou a escrever um módulo e manda por e-mail para Boêmio e Confuso:

| Computador de A | Computador de B | Computador de C |
| --------------- | --------------- | --------------- |
| `programa.py`   | `programa.py`   | `programa.py`   |

Afobada e Confuso continuam avançando no desenvolvimento, Boêmio vai trabalhar mais tarde. Quando chega a hora de Boêmio trabalhar, ele manda e-mail para Afobada e Confuso para pedir a versão mais atual do programa:

| Computador de A | Computador de B | Computador de C |
| --------------- | --------------- | --------------- |
| `programa.py`   | `programa.py`   | `programa.py`   |
|                 | `programa_A.py` |                 |
|                 | `programa_C.py` |                 |

Boêmio tem que juntar as duas versões. Ele percebe que Afobada e Confuso acabaram desenvolvendo algumas coisas em duplicata (programaram a mesma função, por exemplo, culpa do Confuso!). E agora? Passa da meia noite e seus colegas estão dormindo! Ele emenda os dois códigos da maneira que ele acha melhor e continua trabalhando.

Enquanto isso, Afobada não espera o *merge* do código para continuar desenvolvendo: ela faz uma cópia do código original e continua trabalhando.

| Computador de A  | Computador de B          | Computador de C |
| ---------------- | ------------------------ | --------------- |
| `programa_v1.py` | `programa.py`            | `programa.py`   |
| `programa_v2.py` | `programa_A.py`          |                 |
|                  | `programa_C.py`          |                 |
|                  | `programa_merged_A_C.py` |                 |

Agora, Confuso recebe a cópia v2 de Afobada e percebe a duplicação de código, fica bravo com Afobada, e resolve manter a sua própria versão do código, apenas adicionando a parte nova que Afobada escreveu. Ele manda sua nova versão do programa para Boêmio, que tenta juntar todas as versões.

| Computador de A  | Computador de B          | Computador de C    |
| ---------------- | ------------------------ | ------------------ |
| `programa_v1.py` | `programa.py`            | `programa.py`      |
| `programa_v2.py` | `programa_A.py`          | `programa_v2.py`   |
|                  | `programa_C.py`          | `programa_novo.py` |
|                  | `programa_merged_A_C.py` |                    |
|                  | `programa_novo.py`       |                    |
|                  | `programa_final.py`      |                    |

Porém o grupo desenvolveu todo o trabalho sem testes adequados, e agora foi descoberto um erro. Durante o *debug*, Afobada e Boêmio trabalharam juntos para consertar o erro e acabaram gerando várias versões. Confuso trabalhou num requisito novo do projeto.

| Computador de A  | Computador de B          | Computador de C    |
| ---------------- | ------------------------ | ------------------ |
| `programa_v1.py` | `programa.py`            | `programa.py`      |
| `programa_v2.py` | `programa_A.py`          | `programa_v2.py`   |
| `programa_final_testando.py` | `programa_C.py`          | `programa_novo.py` |
| `programa_final_testando_novo.py` | `programa_merged_A_C.py` | `programa_20211203.py` |
| `etc...` | `programa_novo.py`       |                    |
|                  | `programa_final.py`      | `programa_entrega.py` |

Por fim Afobada e Boêmio mandam a versão corrigida para Confuso, que com muito esforço consegue juntar as versões. Olha a confusão de arquivos!

![](raw/git/noobs.jpg)

Mas no dia de entregar o projeto, o HD de Confuso queimou.

| Computador de A  | Computador de B          | Computador de C    |
| ---------------- | ------------------------ | ------------------ |
| `programa_v1.py` | `programa.py`            | 😵 |
| `programa_v2.py` | `programa_A.py`          |          |
| `programa_final_testando.py` | `programa_C.py`          |          |
| `programa_final_testando_novo.py` | `programa_merged_A_C.py` |          |
| `etc...` | `programa_novo.py`       |                    |
|                  | `programa_final.py`      |          |

![](raw/git/yunogit.jpg)

Muitos dos problemas deste cenário podem ser diminuídos usando um sistema de controle de versão. Tais sistemas facilitam o gerenciamento de documentos (principalmente código-fonte) que são construídos de modo incremental (como uma sequência de pequenas modificações), e muitas vezes em grupo.

## Sistemas de controle de versão

Sistemas de controle de versão podem ser aplicados à gestão de documentos em geral. Você talvez já tenha usado controle de versão: por exemplo, o mecanismo de revisão do Microsoft Word. Podemos usar controle de versão para arquivos de desenho técnico, para documentos legais, para bulas de remédio, para qualquer coisa! Mas é no gerenciamento de código-fonte que o controle de versão se sobressai: é absolutamente impossível conceber o desenvolvimento moderno de software (e tem sido assim desde os anos 80) sem esta ferramenta.

O uso de sistemas de controle de versão é prática bem estabelecida no mercado onde quer que software seja desenvolvido, de start-ups à grandes empresas multinacionais, em todos os setores de tecnologia. Saber os conceitos de controle de versão e ser proficiente em algum sistema de controle de versão moderno é um requerimento básico para todos os engenheiros (seja Mecânico, Mecatrônico, ou de Computação).

Em nosso curso, usaremos o software de controle de versão chamado Git, criado por Linus Torvalds em 2005.

:::admonition{type="info" title="Linus Torvalds" collapse}
Linus é o criador do kernel do sistema operacional aberto Linux, no qual se baseiam as várias distribuições de sistema operacional que emprestam o mesmo nome (como Ubuntu Linux, RedHat Linux, Debian Linux, Linux Mint, etc). O código-fonte do kernel do Linux é extenso, resultado da colaboração de vários indivíduos mundo afora que gostaram do sistema operacional criado por Linus, que na época era um aluno de computação finlandês de 21 anos apenas!
:::

Nesta apostila discutiremos o Git de modo bastante superficial. Para conhecer melhor o Git, veja este tutorial em https://www.atlassian.com/git/tutorials/ ou estes outros recursos https://try.github.io/

:::admonition{type="info" title="Outros sistemas de controle de versão" collapse}
Outros sistemas de controle de versão incluem Subversion, Mercurial, e CVS. Algumas empresas de grande porte, como o Google, desenvolveram seus próprios sistemas de controle de versão. Mas todos estes sistemas compartilham os mesmos princípios básicos de operação, do ponto de vista do desenvolvedor de software.
:::

## Gerenciamento de mudanças (*tracking changes*)

Um *repositório* (*repository)* é um conjunto de arquivos que está sob controle do sistema de controle de versão. Geralmente trata-se de um diretório e de todos os arquivos e subdiretórios abaixo do mesmo. O repositório pode ser local (um diretório no seu computador) ou remoto (o repositório existe em um computador remoto, em um servidor da sua empresa ou no cloud).

Ao começar um projeto devemos criar o repositório. No caso de equipes de desenvolvimento, geralmente cabe ao líder da equipe a criação do repositório e a definição de quais indivíduos terão acesso ao mesmo. Este repositório inicial é criado em um servidor de rede, ou em serviços online de armazenamento de repositórios. Neste curso usaremos o serviço online [GitHub](https://github.com/).

Os membros da equipe então irão **clonar** o repositório em suas respectivas máquinas. Estes repositórios criados por clonagem são tão centrais como o repositório inicial, é por mera convenção que usaremos o repositório inicial como o repositório oficial do grupo de trabalho. Chamaremos o repositório inicial (no servidor do GitHub) de *repositório remoto*, e os repositórios clonados de *repositórios locais* (pois são cópias no computador de cada membro do grupo).

Os vários repositórios agora serão mantidos em sincronia pelo sistema de controle de versão, através de atividades específicas que passarão a fazer parte da rotina dos desenvolvedores. Tais atividades, como *check-out* (ou *pull*, ou *fetch*), *commit*, *check-in* (ou *push*), *branch*, entre outras, serão discutidas mais tarde.

O ciclo regular de trabalho de um membro da equipe (incluindo o líder), após clonar o repositório inicial, será:

- *Fetch*: baixa as últimas mudanças (em jargão da área, os últimos *commits*).
- *Merge*: quando solicitado a fazer o merge, o Git tenta adicionar estas novas mudanças ao estado atual do seu repositório (ou seja, tenta adicionar os novos códigos escritos pelos seus colegas ao código que já está na sua máquina).
  - *Pull*: o Git oferece o comando *pull*, que é equivalente a um *fetch* seguido de um *merge*.
- Resolução de conflitos: o *merge* não será bem-sucedido enquanto houverem *conflitos* entre o seu código e os novos *commits*. Geralmente o Git é bem esperto e consegue integrar o novo código sozinho, mas às vezes ele fica confuso e não sabe como fazer a integração automática. Nestes casos, o Git mostrará onde não foi possível integrar o código automaticamente e pedirá que você conserte manualmente a integração.
  - *Pro-tip*: mesmo que o Git integre o novo código automaticamente, vale a pena rever manualmente todos os arquivos modificados que tenham algo a ver com o código no qual você estava trabalhando logo antes do merge!
- Enquanto você estiver desenvolvendo uma pequena nova funcionalidade:
  - Escrever novo código com uma pequena mudança.
  - *Commit*: Uma vez que tudo esteja funcionando bem, gravar no seu repositório Git local essa sua pequena mudança.
    - *Pro-tip*: Faça vários pequenos commits, é para o seu próprio bem!
  - De tempos em tempos, repita o ciclo "pull"-"resolver conflitos" para garantir que você não está escrevendo código novo em *codebase* desatualizada.
- Se tudo estiver bem, e faça um último ciclo "pull"-"resolver conflitos"
- *Push*: envia seus *commits* para o repositório remoto

Agora é celebrar, vai tomar um café, uma água! É agora que você começa a receber os e-mails dos seus colegas exaltando a beleza e praticidade da feature que você desenvolveu!

Ou então a sua equipe não tem testes automatizados, e a sua feature quebrou o trabalho dos seus colegas! Neste momento você pode reverter as suas mudanças (lembra da dica de fazer pequenos commits? De nada!) e fazer um novo push com essa atividade. (No jargão da área: dar um *revert*).

Vamos recapitular o que temos até o momento:

- O líder criou um repositório novo. Neste curso usaremos o serviço online GitHub para isso. Chamaremos este repositório inicial de repositório remoto.
- Todos clonam o repositório remoto, gerando os vários repositórios locais.
- Estabelece-se o ciclo regular de trabalho: *fetch-merge-resolve-commit-push*.

## Tutorial

1. Crie uma conta no GitHub: https://github.com/ . Com isso você poderá criar seus próprios repositórios Git remotos, acessíveis de qualquer lugar, com backups e disponibilidade garantidos! Nada mal para um serviço gratuito, não?
2. Instale o git no seu computador seguindo os passos disponíveis nesta página: https://git-scm.com/downloads
3. Combine com a sua dupla quem será o desenvolvedor 1 e quem será o desenvolvedor 2. A única diferença é que o desenvolvedor 1 vai criar o repositório no GitHub. Todos os outros comandos serão executados pelos dois membros da dupla. Entre no seu respectivo link a seguir:
   - [Desenvolvedor 1](git/dev1)
   - [Desenvolvedor 2](git/dev2)


:::admonition{type=info title="Vídeo Suporte"}

Para te auxiliar neste exercício, há um vídeo demonstrando alguns dos passos do handout.
[https://www.youtube.com/watch?v=zjyQF8JdTRE](https://www.youtube.com/watch?v=zjyQF8JdTRE)

**Dica:** Caso precise, diminua a velocidade do vídeo!
:::
