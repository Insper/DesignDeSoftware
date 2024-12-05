# 02. Chamando e criando funções

## Chamando (ou executando) funções

Já vimos como podemos criar valores numéricos e realizar as operações aritméticas básicas (adição, subtração, divisão, multiplicação e potenciação) em Python. Sabemos que além dessas operações básicas existem diversas outras operações matemáticas úteis. Por exemplo: funções trigonométricas (seno, cosseno, tangente), logaritmo, fatorial, etc.

Em Python não existem operadores para seno, logaritmo, etc., mas temos pacotes que estendem a linguagem com essas funcionalidades. Para este exemplo específico, nós temos o pacote `math`, um pacote do Python com diversas funções matemáticas úteis.

!!! info "Se estiver preocupada/preocupado com a matemática"
    Não se preocupe, nesse começo nós utilizamos exemplos matemáticos por serem mais diretos, mas em breve começaremos a apresentar outros exemplos não relacionados à matemática.

Para dizer ao Python que queremos utilizar esse pacote nós devemos utilizar o comando `#!python import`. Veja a seguir um exemplo de cálculo do cosseno de zero:

```python linenums="1"
--8<-- "funcao/raw/funcao/usando_cosseno.py"
```

Na linha 1 estamos dizendo para o Python que queremos utilizar o pacote de funções matemáticas `math`. Antes de entendermos a linha 2, vamos relembrar o que a linha 3 está fazendo: estamos pedindo para o Python executar (através dos parênteses) a função `#!python print` (que mostra um texto no terminal) utilizando como argumento o conteúdo da variável `#!python resultado`.

Agora que revisamos o uso da função `#!python print`, podemos voltar para a linha 2 do nosso código. Nessa linha nós estamos utilizando a função que calcula o cosseno (`cos`) do pacote `math`, ou seja, `math.cos`. Lembrando que os parênteses são a nossa forma de pedir para o Python **executar** uma função, o que essa linha faz é pedir para o Python executar a função `math.cos` com o argumento `0` (zero). Essa função vai devolver um resultado e nós queremos que o Python guarde esse resultado na variável `resultado`.

!!! Danger "Antes de prosseguir"
    Recomendamos que você sempre teste os códigos apresentados no seu próprio computador. Para isso, procure sempre digitar o código ao invés de copiar e colar.

!!! exercise "EXERCÍCIO"

    Teste o código acima com valores diferentes, que você saiba o resultado esperado, e veja o que acontece.

    !!! info "Deu diferente, e agora?"
        Provavelmente o resultado não é o que você esperava. Se tiver curiosidade, leia a [documentação da função `cos`](https://docs.python.org/3/library/math.html#math.cos) para tentar entender o problema.

## Estendendo o Python com as suas próprias funções

Vimos que as funções no Python nos permitem estender as suas funcionalidades. Você pode pensar na função como uma parte reaproveitável de um programa. Como assim? Considere a função `math.cos` que acabamos de testar. Nós pedimos para o Python executar essa função passando um ângulo. Não sabemos (e nem precisamos saber, por enquanto) como ela faz isso, mas ela calcula o cosseno desse ângulo e devolve o resultado. Pensando no nosso programa, o que aconteceu foi que plugamos uma caixa preta na qual entram números representando ângulos e saem números representando o seu cosseno e é isso o que precisamos saber.

Nós poderíamos inclusive chamar essa função várias vezes no mesmo programa, calculando o cosseno de vários ângulos. A cada vez o Python executaria esse código desconhecido/escondido e devolveria o resultado para guardarmos na nossa variável. Por isso dizemos que estamos **reaproveitando código** com a função. O código do nosso programa fica bastante sucinto, apesar de ele pode estar fazendo várias coisas por baixo dos panos sem que saibamos.

Agora veremos que podemos inclusive criar as nossas próprias funções para estender o Python com a funcionalidade que quisermos!

Vamos começar com um exemplo de uma função que converte valores de milhas para quilômetros:

```python linenums="1"
--8<-- "funcao/raw/funcao/conversoes.py"
```

Vamos entender o que está acontecendo, começando pelos nomes:

- O `#!python distancia_mi` na linha 1 é chamado de **argumento** da função.
- O `#!python distancia_km` na linha 3 é chamado de **retorno** ou **resultado** da função.
- As linhas 2 e 3 são chamadas de **corpo** ou **bloco** da função.
- O corpo da função é identificado com os 4 espaços no começo da linha. Esses 4 espaços são chamados de **indentação**.

!!! info "Indentação"
    A indentação é crucial e Python e tem um significado especial. Ela é utilizada para indicar blocos de código. Portanto não se deve utilizar indentações a mais ou a menos, pois isso causará um erro na execução do programa.

    O uso de 4 espaços é outra padronização da comunidade Python. Se você usar 2, 3 ou qualquer outra quantidade de espaços (ou até mesmo o caractere `tab`) o código funcionará da mesma forma. Desde que seja consistente, ou seja, escolha um formato e utilize-o em todo o seu programa. Recomendamos que você utilize 4 espaços para seguir o padrão da comunidade.

Se você executar o código acima não vai acontecer nada. Nesse código nós estamos apenas **definindo** a função `#!python converte_milhas_para_km` (por isso a palavra `#!python def`). Podemos entender a linha 1 como: "Python, **quando** eu pedir para você executar a função `#!python converte_milhas_para_km`, passando um valor para `#!python distancia_mi`, o que você deve fazer é: multiplicar o valor armazenado na variável `#!python distancia_mi` por 1.60934 e guardar o resultado na variável `#!python distancia_km` e depois devolver o valor armazenado na variável `#!python distancia_km` como o resultado". Em outras palavras, é como se estivéssemos **criando um novo comando do Python** (assim como já temos o `#!python print` ou o `#!python math.cos`, por exemplo).

## Chamando a nossa função em Python

Vamos refletir brevemente sobre a função que acabamos de criar. Qual é o valor esperado para o resultado da chamada da função `#!python converte_milhas_para_km(distancia_mi)`? A resposta é: depende! Depende do valor de `distancia_mi`. A função `converte_milhas_para_km` só vai devolver um valor se definirmos um valor para `distancia_mi`.

Essa ideia é a mesma que apresentamos sobre a função `#!python print`, ou seja, precisamos de uma informação adicional. Uma vez que definimos uma função é como se ela se tornasse parte da linguagem Python. Assim, para esse contexto introdutório, não existe nenhuma diferença entre a função `#!python print` e a função `#!python converte_milhas_para_km(distancia_mi)` em termos de importância. Ambas são comandos disponíveis no Python para o programador utilizar em seu código.

Vamos então ver um exemplo de uso da nossa função `#!python converte_milhas_para_km(distancia_mi)`. Suponha que o código que define a função `#!python converte_milhas_para_km(distancia_mi)` esteja em um arquivo chamado `conversoes.py`. Considere o código a seguir em outro arquivo (por exemplo, `teste.py`, que deve estar na mesma pasta que o arquivo `conversoes.py`):

```python linenums="1"
--8<-- "funcao/raw/funcao/funcoes.py"
```

Na linha 1 nós falamos para o Python que queremos utilizar as funções disponíveis no arquivo `conversoes.py`. Na linha 3, armazenamos o número 10 na variável `#!python a`. Na linha 4 ocorre a chamada da função. Vamos detalhar o que ocorre nessa linha:

- O valor da variável `#!python a` é utilizado, o Python consulta esse valor na memória e substitui na chamada da função. Agora a linha é equivalente a `#!python b = conversoes.converte_milhas_para_km(10)`.
- A função `#!python conversoes.converte_milhas_para_km()` é executada com o argumento `#!python 10`.
- A função `#!python conversoes.converte_milhas_para_km()` devolve o valor `#!python 16.0934` (não importa como foi calculado, apesar de nós sabermos).
- Agora que temos o resultado da função, a linha 4 é equivalente a `#!python b = 16.0934`.
- O valor `#!python 16.0934` é armazenado na variável `#!python b`

Por fim, na linha 5, o valor armazenado na variável `#!python b` é utilizado como argumento da função `#!python print()` e o valor `#!python 16.0934` é mostrado no terminal.

!!! info "Dica Pro: use bons nomes!"
    No dia seguinte você abre o programa mostrado acima. O que faz mesmo esse código? Acredite, é mais comum do que você imagina. Enquanto estamos desenvolvendo o programa temos muito claro para quê cada variável serve, mas não precisamos de muito tempo para olhar o mesmo código e não ter ideia do que está acontecendo.

    Por isso, use nomes que façam sentido para as suas variáveis e funções. Quando não estiver claro o suficiente, adicione comentários, mas as vezes boas escolhas de nomes dispensam comentários no código.

## Outros exercícios

Você só vai aprender a programar programando muito. O servidor possui diversos exercícios disponíveis com correção automática. Aproveite esse recurso para praticar bastante.

!!! exercise "EXERCÍCIO"
    Faça o exercício [Celsius para Fahrenheit]({{pl_funcao}}){:target="_blank"}
    
!!! exercise "EXERCÍCIO"
    Faça o exercício [Área do triângulo]({{pl_funcao}}){:target="_blank"}

    Dica: uma função em Python, assim como uma função matemática multivariada, pode receber vários argumentos separados por vírgula.

    Não esqueça de escrever código de teste também. Pense em valores de teste que sejam interessantes. Por exemplo: e se a base for zero? E se a altura for zero? E se forem iguais?

Faça todos os outros exercícios disponíveis sobre funções. Quanto mais, melhor!