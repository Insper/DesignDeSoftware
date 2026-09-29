## Cenário 1

**Importante:**
Para testar esse cenário, será necessário adicionar um comando ao seu código.

Adicione a seguinte linha de código no começo do arquivo e depois dos import:

```python
random.seed(1)
```

Cenário onde o jogador ganha.

```
Insira as informações referentes ao navio porta-aviões que possui tamanho 4
Linha: 1
Coluna: 5
Orientação: [1] Vertical [2] Horizontal 2
Insira as informações referentes ao navio navio-tanque que possui tamanho 3
Linha: 6
Coluna: 1
Orientação: [1] Vertical [2] Horizontal 2
Insira as informações referentes ao navio navio-tanque que possui tamanho 3
Linha: 4
Coluna: 7
Orientação: [1] Vertical [2] Horizontal 1
Insira as informações referentes ao navio contratorpedeiro que possui tamanho 2
Linha: 1
Coluna: 1
Orientação: [1] Vertical [2] Horizontal 1
Insira as informações referentes ao navio contratorpedeiro que possui tamanho 2
Linha: 2
Coluna: 3
Orientação: [1] Vertical [2] Horizontal 1
Insira as informações referentes ao navio contratorpedeiro que possui tamanho 2
Linha: 9
Coluna: 1
Orientação: [1] Vertical [2] Horizontal 2
Insira as informações referentes ao navio submarino que possui tamanho 1
Linha: 0
Coluna: 3
Insira as informações referentes ao navio submarino que possui tamanho 1
Linha: 4
Coluna: 5
Insira as informações referentes ao navio submarino que possui tamanho 1
Linha: 8
Coluna: 9
Insira as informações referentes ao navio submarino que possui tamanho 1
Linha: 8
Coluna: 4
   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9
_______________________________      _______________________________
0| 0  0  0  1  0  0  0  0  0  0|     0| 0  0  0  0  0  0  0  0  0  0|
1| 0  1  0  0  0  1  1  1  1  0|     1| 0  0  0  0  0  0  0  0  0  0|
2| 0  1  0  1  0  0  0  0  0  0|     2| 0  0  0  0  0  0  0  0  0  0|
3| 0  0  0  1  0  0  0  0  0  0|     3| 0  0  0  0  0  0  0  0  0  0|
4| 0  0  0  0  0  1  0  1  0  0|     4| 0  0  0  0  0  0  0  0  0  0|
5| 0  0  0  0  0  0  0  1  0  0|     5| 0  0  0  0  0  0  0  0  0  0|
6| 0  1  1  1  0  0  0  1  0  0|     6| 0  0  0  0  0  0  0  0  0  0|
7| 0  0  0  0  0  0  0  0  0  0|     7| 0  0  0  0  0  0  0  0  0  0|
8| 0  0  0  0  1  0  0  0  0  1|     8| 0  0  0  0  0  0  0  0  0  0|
9| 0  1  1  0  0  0  0  0  0  0|     9| 0  0  0  0  0  0  0  0  0  0|

Jogador, qual linha deseja atacar? 1
Jogador, qual coluna deseja atacar? 6
Seu oponente está atacando na linha 2 e coluna 9
   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9
_______________________________      _______________________________
0| 0  0  0  1  0  0  0  0  0  0|     0| 0  0  0  0  0  0  0  0  0  0|
1| 0  1  0  0  0  1  1  1  1  0|     1| 0  0  0  0  0  0  X  0  0  0|
2| 0  1  0  1  0  0  0  0  0  -|     2| 0  0  0  0  0  0  0  0  0  0|
3| 0  0  0  1  0  0  0  0  0  0|     3| 0  0  0  0  0  0  0  0  0  0|
4| 0  0  0  0  0  1  0  1  0  0|     4| 0  0  0  0  0  0  0  0  0  0|
5| 0  0  0  0  0  0  0  1  0  0|     5| 0  0  0  0  0  0  0  0  0  0|
6| 0  1  1  1  0  0  0  1  0  0|     6| 0  0  0  0  0  0  0  0  0  0|
7| 0  0  0  0  0  0  0  0  0  0|     7| 0  0  0  0  0  0  0  0  0  0|
8| 0  0  0  0  1  0  0  0  0  1|     8| 0  0  0  0  0  0  0  0  0  0|
9| 0  1  1  0  0  0  0  0  0  0|     9| 0  0  0  0  0  0  0  0  0  0|

Jogador, qual linha deseja atacar? 1
Jogador, qual coluna deseja atacar? 7
Seu oponente está atacando na linha 1 e coluna 4
   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9
_______________________________      _______________________________
0| 0  0  0  1  0  0  0  0  0  0|     0| 0  0  0  0  0  0  0  0  0  0|
1| 0  1  0  0  -  1  1  1  1  0|     1| 0  0  0  0  0  0  X  X  0  0|
2| 0  1  0  1  0  0  0  0  0  -|     2| 0  0  0  0  0  0  0  0  0  0|
3| 0  0  0  1  0  0  0  0  0  0|     3| 0  0  0  0  0  0  0  0  0  0|
4| 0  0  0  0  0  1  0  1  0  0|     4| 0  0  0  0  0  0  0  0  0  0|
5| 0  0  0  0  0  0  0  1  0  0|     5| 0  0  0  0  0  0  0  0  0  0|
6| 0  1  1  1  0  0  0  1  0  0|     6| 0  0  0  0  0  0  0  0  0  0|
7| 0  0  0  0  0  0  0  0  0  0|     7| 0  0  0  0  0  0  0  0  0  0|
8| 0  0  0  0  1  0  0  0  0  1|     8| 0  0  0  0  0  0  0  0  0  0|
9| 0  1  1  0  0  0  0  0  0  0|     9| 0  0  0  0  0  0  0  0  0  0|

Jogador, qual linha deseja atacar? 0
Jogador, qual coluna deseja atacar? 5
Seu oponente está atacando na linha 1 e coluna 7
   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9
_______________________________      _______________________________
0| 0  0  0  1  0  0  0  0  0  0|     0| 0  0  0  0  0  X  0  0  0  0|
1| 0  1  0  0  -  1  1  X  1  0|     1| 0  0  0  0  0  0  X  X  0  0|
2| 0  1  0  1  0  0  0  0  0  -|     2| 0  0  0  0  0  0  0  0  0  0|
3| 0  0  0  1  0  0  0  0  0  0|     3| 0  0  0  0  0  0  0  0  0  0|
4| 0  0  0  0  0  1  0  1  0  0|     4| 0  0  0  0  0  0  0  0  0  0|
5| 0  0  0  0  0  0  0  1  0  0|     5| 0  0  0  0  0  0  0  0  0  0|
6| 0  1  1  1  0  0  0  1  0  0|     6| 0  0  0  0  0  0  0  0  0  0|
7| 0  0  0  0  0  0  0  0  0  0|     7| 0  0  0  0  0  0  0  0  0  0|
8| 0  0  0  0  1  0  0  0  0  1|     8| 0  0  0  0  0  0  0  0  0  0|
9| 0  1  1  0  0  0  0  0  0  0|     9| 0  0  0  0  0  0  0  0  0  0|

Jogador, qual linha deseja atacar? 1
Jogador, qual coluna deseja atacar? 5
Seu oponente está atacando na linha 7 e coluna 7
   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9
_______________________________      _______________________________
0| 0  0  0  1  0  0  0  0  0  0|     0| 0  0  0  0  0  X  0  0  0  0|
1| 0  1  0  0  -  1  1  X  1  0|     1| 0  0  0  0  0  X  X  X  0  0|
2| 0  1  0  1  0  0  0  0  0  -|     2| 0  0  0  0  0  0  0  0  0  0|
3| 0  0  0  1  0  0  0  0  0  0|     3| 0  0  0  0  0  0  0  0  0  0|
4| 0  0  0  0  0  1  0  1  0  0|     4| 0  0  0  0  0  0  0  0  0  0|
5| 0  0  0  0  0  0  0  1  0  0|     5| 0  0  0  0  0  0  0  0  0  0|
6| 0  1  1  1  0  0  0  1  0  0|     6| 0  0  0  0  0  0  0  0  0  0|
7| 0  0  0  0  0  0  0  -  0  0|     7| 0  0  0  0  0  0  0  0  0  0|
8| 0  0  0  0  1  0  0  0  0  1|     8| 0  0  0  0  0  0  0  0  0  0|
9| 0  1  1  0  0  0  0  0  0  0|     9| 0  0  0  0  0  0  0  0  0  0|

Jogador, qual linha deseja atacar? 3
Jogador, qual coluna deseja atacar? 6
Seu oponente está atacando na linha 6 e coluna 3
   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9
_______________________________      _______________________________
0| 0  0  0  1  0  0  0  0  0  0|     0| 0  0  0  0  0  X  0  0  0  0|
1| 0  1  0  0  -  1  1  X  1  0|     1| 0  0  0  0  0  X  X  X  0  0|
2| 0  1  0  1  0  0  0  0  0  -|     2| 0  0  0  0  0  0  0  0  0  0|
3| 0  0  0  1  0  0  0  0  0  0|     3| 0  0  0  0  0  0  X  0  0  0|
4| 0  0  0  0  0  1  0  1  0  0|     4| 0  0  0  0  0  0  0  0  0  0|
5| 0  0  0  0  0  0  0  1  0  0|     5| 0  0  0  0  0  0  0  0  0  0|
6| 0  1  1  X  0  0  0  1  0  0|     6| 0  0  0  0  0  0  0  0  0  0|
7| 0  0  0  0  0  0  0  -  0  0|     7| 0  0  0  0  0  0  0  0  0  0|
8| 0  0  0  0  1  0  0  0  0  1|     8| 0  0  0  0  0  0  0  0  0  0|
9| 0  1  1  0  0  0  0  0  0  0|     9| 0  0  0  0  0  0  0  0  0  0|

Jogador, qual linha deseja atacar? 3
Jogador, qual coluna deseja atacar? 7
Seu oponente está atacando na linha 0 e coluna 6
   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9
_______________________________      _______________________________
0| 0  0  0  1  0  0  -  0  0  0|     0| 0  0  0  0  0  X  0  0  0  0|
1| 0  1  0  0  -  1  1  X  1  0|     1| 0  0  0  0  0  X  X  X  0  0|
2| 0  1  0  1  0  0  0  0  0  -|     2| 0  0  0  0  0  0  0  0  0  0|
3| 0  0  0  1  0  0  0  0  0  0|     3| 0  0  0  0  0  0  X  X  0  0|
4| 0  0  0  0  0  1  0  1  0  0|     4| 0  0  0  0  0  0  0  0  0  0|
5| 0  0  0  0  0  0  0  1  0  0|     5| 0  0  0  0  0  0  0  0  0  0|
6| 0  1  1  X  0  0  0  1  0  0|     6| 0  0  0  0  0  0  0  0  0  0|
7| 0  0  0  0  0  0  0  -  0  0|     7| 0  0  0  0  0  0  0  0  0  0|
8| 0  0  0  0  1  0  0  0  0  1|     8| 0  0  0  0  0  0  0  0  0  0|
9| 0  1  1  0  0  0  0  0  0  0|     9| 0  0  0  0  0  0  0  0  0  0|

Jogador, qual linha deseja atacar? 6
Jogador, qual coluna deseja atacar? 0
Seu oponente está atacando na linha 6 e coluna 9
   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9
_______________________________      _______________________________
0| 0  0  0  1  0  0  -  0  0  0|     0| 0  0  0  0  0  X  0  0  0  0|
1| 0  1  0  0  -  1  1  X  1  0|     1| 0  0  0  0  0  X  X  X  0  0|
2| 0  1  0  1  0  0  0  0  0  -|     2| 0  0  0  0  0  0  0  0  0  0|
3| 0  0  0  1  0  0  0  0  0  0|     3| 0  0  0  0  0  0  X  X  0  0|
4| 0  0  0  0  0  1  0  1  0  0|     4| 0  0  0  0  0  0  0  0  0  0|
5| 0  0  0  0  0  0  0  1  0  0|     5| 0  0  0  0  0  0  0  0  0  0|
6| 0  1  1  X  0  0  0  1  0  -|     6| X  0  0  0  0  0  0  0  0  0|
7| 0  0  0  0  0  0  0  -  0  0|     7| 0  0  0  0  0  0  0  0  0  0|
8| 0  0  0  0  1  0  0  0  0  1|     8| 0  0  0  0  0  0  0  0  0  0|
9| 0  1  1  0  0  0  0  0  0  0|     9| 0  0  0  0  0  0  0  0  0  0|

Jogador, qual linha deseja atacar? 6
Jogador, qual coluna deseja atacar? 1
Seu oponente está atacando na linha 0 e coluna 7
   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9
_______________________________      _______________________________
0| 0  0  0  1  0  0  -  -  0  0|     0| 0  0  0  0  0  X  0  0  0  0|
1| 0  1  0  0  -  1  1  X  1  0|     1| 0  0  0  0  0  X  X  X  0  0|
2| 0  1  0  1  0  0  0  0  0  -|     2| 0  0  0  0  0  0  0  0  0  0|
3| 0  0  0  1  0  0  0  0  0  0|     3| 0  0  0  0  0  0  X  X  0  0|
4| 0  0  0  0  0  1  0  1  0  0|     4| 0  0  0  0  0  0  0  0  0  0|
5| 0  0  0  0  0  0  0  1  0  0|     5| 0  0  0  0  0  0  0  0  0  0|
6| 0  1  1  X  0  0  0  1  0  -|     6| X  X  0  0  0  0  0  0  0  0|
7| 0  0  0  0  0  0  0  -  0  0|     7| 0  0  0  0  0  0  0  0  0  0|
8| 0  0  0  0  1  0  0  0  0  1|     8| 0  0  0  0  0  0  0  0  0  0|
9| 0  1  1  0  0  0  0  0  0  0|     9| 0  0  0  0  0  0  0  0  0  0|

Jogador, qual linha deseja atacar? 6
Jogador, qual coluna deseja atacar? 2
Seu oponente está atacando na linha 4 e coluna 3
   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9
_______________________________      _______________________________
0| 0  0  0  1  0  0  -  -  0  0|     0| 0  0  0  0  0  X  0  0  0  0|
1| 0  1  0  0  -  1  1  X  1  0|     1| 0  0  0  0  0  X  X  X  0  0|
2| 0  1  0  1  0  0  0  0  0  -|     2| 0  0  0  0  0  0  0  0  0  0|
3| 0  0  0  1  0  0  0  0  0  0|     3| 0  0  0  0  0  0  X  X  0  0|
4| 0  0  0  -  0  1  0  1  0  0|     4| 0  0  0  0  0  0  0  0  0  0|
5| 0  0  0  0  0  0  0  1  0  0|     5| 0  0  0  0  0  0  0  0  0  0|
6| 0  1  1  X  0  0  0  1  0  -|     6| X  X  X  0  0  0  0  0  0  0|
7| 0  0  0  0  0  0  0  -  0  0|     7| 0  0  0  0  0  0  0  0  0  0|
8| 0  0  0  0  1  0  0  0  0  1|     8| 0  0  0  0  0  0  0  0  0  0|
9| 0  1  1  0  0  0  0  0  0  0|     9| 0  0  0  0  0  0  0  0  0  0|

Jogador, qual linha deseja atacar? 4
Jogador, qual coluna deseja atacar? 3
Seu oponente está atacando na linha 9 e coluna 1
   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9
_______________________________      _______________________________
0| 0  0  0  1  0  0  -  -  0  0|     0| 0  0  0  0  0  X  0  0  0  0|
1| 0  1  0  0  -  1  1  X  1  0|     1| 0  0  0  0  0  X  X  X  0  0|
2| 0  1  0  1  0  0  0  0  0  -|     2| 0  0  0  0  0  0  0  0  0  0|
3| 0  0  0  1  0  0  0  0  0  0|     3| 0  0  0  0  0  0  X  X  0  0|
4| 0  0  0  -  0  1  0  1  0  0|     4| 0  0  0  X  0  0  0  0  0  0|
5| 0  0  0  0  0  0  0  1  0  0|     5| 0  0  0  0  0  0  0  0  0  0|
6| 0  1  1  X  0  0  0  1  0  -|     6| X  X  X  0  0  0  0  0  0  0|
7| 0  0  0  0  0  0  0  -  0  0|     7| 0  0  0  0  0  0  0  0  0  0|
8| 0  0  0  0  1  0  0  0  0  1|     8| 0  0  0  0  0  0  0  0  0  0|
9| 0  X  1  0  0  0  0  0  0  0|     9| 0  0  0  0  0  0  0  0  0  0|

Jogador, qual linha deseja atacar? 5
Jogador, qual coluna deseja atacar? 3
Seu oponente está atacando na linha 5 e coluna 0
   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9
_______________________________      _______________________________
0| 0  0  0  1  0  0  -  -  0  0|     0| 0  0  0  0  0  X  0  0  0  0|
1| 0  1  0  0  -  1  1  X  1  0|     1| 0  0  0  0  0  X  X  X  0  0|
2| 0  1  0  1  0  0  0  0  0  -|     2| 0  0  0  0  0  0  0  0  0  0|
3| 0  0  0  1  0  0  0  0  0  0|     3| 0  0  0  0  0  0  X  X  0  0|
4| 0  0  0  -  0  1  0  1  0  0|     4| 0  0  0  X  0  0  0  0  0  0|
5| -  0  0  0  0  0  0  1  0  0|     5| 0  0  0  X  0  0  0  0  0  0|
6| 0  1  1  X  0  0  0  1  0  -|     6| X  X  X  0  0  0  0  0  0  0|
7| 0  0  0  0  0  0  0  -  0  0|     7| 0  0  0  0  0  0  0  0  0  0|
8| 0  0  0  0  1  0  0  0  0  1|     8| 0  0  0  0  0  0  0  0  0  0|
9| 0  X  1  0  0  0  0  0  0  0|     9| 0  0  0  0  0  0  0  0  0  0|

Jogador, qual linha deseja atacar? 6
Jogador, qual coluna deseja atacar? 3
Seu oponente está atacando na linha 0 e coluna 0
   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9
_______________________________      _______________________________
0| -  0  0  1  0  0  -  -  0  0|     0| 0  0  0  0  0  X  0  0  0  0|
1| 0  1  0  0  -  1  1  X  1  0|     1| 0  0  0  0  0  X  X  X  0  0|
2| 0  1  0  1  0  0  0  0  0  -|     2| 0  0  0  0  0  0  0  0  0  0|
3| 0  0  0  1  0  0  0  0  0  0|     3| 0  0  0  0  0  0  X  X  0  0|
4| 0  0  0  -  0  1  0  1  0  0|     4| 0  0  0  X  0  0  0  0  0  0|
5| -  0  0  0  0  0  0  1  0  0|     5| 0  0  0  X  0  0  0  0  0  0|
6| 0  1  1  X  0  0  0  1  0  -|     6| X  X  X  X  0  0  0  0  0  0|
7| 0  0  0  0  0  0  0  -  0  0|     7| 0  0  0  0  0  0  0  0  0  0|
8| 0  0  0  0  1  0  0  0  0  1|     8| 0  0  0  0  0  0  0  0  0  0|
9| 0  X  1  0  0  0  0  0  0  0|     9| 0  0  0  0  0  0  0  0  0  0|

Jogador, qual linha deseja atacar? 9
Jogador, qual coluna deseja atacar? 1
Seu oponente está atacando na linha 8 e coluna 0
   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9
_______________________________      _______________________________
0| -  0  0  1  0  0  -  -  0  0|     0| 0  0  0  0  0  X  0  0  0  0|
1| 0  1  0  0  -  1  1  X  1  0|     1| 0  0  0  0  0  X  X  X  0  0|
2| 0  1  0  1  0  0  0  0  0  -|     2| 0  0  0  0  0  0  0  0  0  0|
3| 0  0  0  1  0  0  0  0  0  0|     3| 0  0  0  0  0  0  X  X  0  0|
4| 0  0  0  -  0  1  0  1  0  0|     4| 0  0  0  X  0  0  0  0  0  0|
5| -  0  0  0  0  0  0  1  0  0|     5| 0  0  0  X  0  0  0  0  0  0|
6| 0  1  1  X  0  0  0  1  0  -|     6| X  X  X  X  0  0  0  0  0  0|
7| 0  0  0  0  0  0  0  -  0  0|     7| 0  0  0  0  0  0  0  0  0  0|
8| -  0  0  0  1  0  0  0  0  1|     8| 0  0  0  0  0  0  0  0  0  0|
9| 0  X  1  0  0  0  0  0  0  0|     9| 0  X  0  0  0  0  0  0  0  0|

Jogador, qual linha deseja atacar? 9
Jogador, qual coluna deseja atacar? 2
Seu oponente está atacando na linha 6 e coluna 0
   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9
_______________________________      _______________________________
0| -  0  0  1  0  0  -  -  0  0|     0| 0  0  0  0  0  X  0  0  0  0|
1| 0  1  0  0  -  1  1  X  1  0|     1| 0  0  0  0  0  X  X  X  0  0|
2| 0  1  0  1  0  0  0  0  0  -|     2| 0  0  0  0  0  0  0  0  0  0|
3| 0  0  0  1  0  0  0  0  0  0|     3| 0  0  0  0  0  0  X  X  0  0|
4| 0  0  0  -  0  1  0  1  0  0|     4| 0  0  0  X  0  0  0  0  0  0|
5| -  0  0  0  0  0  0  1  0  0|     5| 0  0  0  X  0  0  0  0  0  0|
6| -  1  1  X  0  0  0  1  0  -|     6| X  X  X  X  0  0  0  0  0  0|
7| 0  0  0  0  0  0  0  -  0  0|     7| 0  0  0  0  0  0  0  0  0  0|
8| -  0  0  0  1  0  0  0  0  1|     8| 0  0  0  0  0  0  0  0  0  0|
9| 0  X  1  0  0  0  0  0  0  0|     9| 0  X  X  0  0  0  0  0  0  0|

Jogador, qual linha deseja atacar? 9
Jogador, qual coluna deseja atacar? 3
Seu oponente está atacando na linha 8 e coluna 3
   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9
_______________________________      _______________________________
0| -  0  0  1  0  0  -  -  0  0|     0| 0  0  0  0  0  X  0  0  0  0|
1| 0  1  0  0  -  1  1  X  1  0|     1| 0  0  0  0  0  X  X  X  0  0|
2| 0  1  0  1  0  0  0  0  0  -|     2| 0  0  0  0  0  0  0  0  0  0|
3| 0  0  0  1  0  0  0  0  0  0|     3| 0  0  0  0  0  0  X  X  0  0|
4| 0  0  0  -  0  1  0  1  0  0|     4| 0  0  0  X  0  0  0  0  0  0|
5| -  0  0  0  0  0  0  1  0  0|     5| 0  0  0  X  0  0  0  0  0  0|
6| -  1  1  X  0  0  0  1  0  -|     6| X  X  X  X  0  0  0  0  0  0|
7| 0  0  0  0  0  0  0  -  0  0|     7| 0  0  0  0  0  0  0  0  0  0|
8| -  0  0  -  1  0  0  0  0  1|     8| 0  0  0  0  0  0  0  0  0  0|
9| 0  X  1  0  0  0  0  0  0  0|     9| 0  X  X  X  0  0  0  0  0  0|

Jogador, qual linha deseja atacar? 9
Jogador, qual coluna deseja atacar? 4
Seu oponente está atacando na linha 5 e coluna 3
   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9
_______________________________      _______________________________
0| -  0  0  1  0  0  -  -  0  0|     0| 0  0  0  0  0  X  0  0  0  0|
1| 0  1  0  0  -  1  1  X  1  0|     1| 0  0  0  0  0  X  X  X  0  0|
2| 0  1  0  1  0  0  0  0  0  -|     2| 0  0  0  0  0  0  0  0  0  0|
3| 0  0  0  1  0  0  0  0  0  0|     3| 0  0  0  0  0  0  X  X  0  0|
4| 0  0  0  -  0  1  0  1  0  0|     4| 0  0  0  X  0  0  0  0  0  0|
5| -  0  0  -  0  0  0  1  0  0|     5| 0  0  0  X  0  0  0  0  0  0|
6| -  1  1  X  0  0  0  1  0  -|     6| X  X  X  X  0  0  0  0  0  0|
7| 0  0  0  0  0  0  0  -  0  0|     7| 0  0  0  0  0  0  0  0  0  0|
8| -  0  0  -  1  0  0  0  0  1|     8| 0  0  0  0  0  0  0  0  0  0|
9| 0  X  1  0  0  0  0  0  0  0|     9| 0  X  X  X  X  0  0  0  0  0|

Jogador, qual linha deseja atacar? 2
Jogador, qual coluna deseja atacar? 7
Seu oponente está atacando na linha 3 e coluna 7
   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9
_______________________________      _______________________________
0| -  0  0  1  0  0  -  -  0  0|     0| 0  0  0  0  0  X  0  0  0  0|
1| 0  1  0  0  -  1  1  X  1  0|     1| 0  0  0  0  0  X  X  X  0  0|
2| 0  1  0  1  0  0  0  0  0  -|     2| 0  0  0  0  0  0  0  X  0  0|
3| 0  0  0  1  0  0  0  -  0  0|     3| 0  0  0  0  0  0  X  X  0  0|
4| 0  0  0  -  0  1  0  1  0  0|     4| 0  0  0  X  0  0  0  0  0  0|
5| -  0  0  -  0  0  0  1  0  0|     5| 0  0  0  X  0  0  0  0  0  0|
6| -  1  1  X  0  0  0  1  0  -|     6| X  X  X  X  0  0  0  0  0  0|
7| 0  0  0  0  0  0  0  -  0  0|     7| 0  0  0  0  0  0  0  0  0  0|
8| -  0  0  -  1  0  0  0  0  1|     8| 0  0  0  0  0  0  0  0  0  0|
9| 0  X  1  0  0  0  0  0  0  0|     9| 0  X  X  X  X  0  0  0  0  0|

Jogador, qual linha deseja atacar? 0
Jogador, qual coluna deseja atacar? 6
Seu oponente está atacando na linha 4 e coluna 0
   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9
_______________________________      _______________________________
0| -  0  0  1  0  0  -  -  0  0|     0| 0  0  0  0  0  X  X  0  0  0|
1| 0  1  0  0  -  1  1  X  1  0|     1| 0  0  0  0  0  X  X  X  0  0|
2| 0  1  0  1  0  0  0  0  0  -|     2| 0  0  0  0  0  0  0  X  0  0|
3| 0  0  0  1  0  0  0  -  0  0|     3| 0  0  0  0  0  0  X  X  0  0|
4| -  0  0  -  0  1  0  1  0  0|     4| 0  0  0  X  0  0  0  0  0  0|
5| -  0  0  -  0  0  0  1  0  0|     5| 0  0  0  X  0  0  0  0  0  0|
6| -  1  1  X  0  0  0  1  0  -|     6| X  X  X  X  0  0  0  0  0  0|
7| 0  0  0  0  0  0  0  -  0  0|     7| 0  0  0  0  0  0  0  0  0  0|
8| -  0  0  -  1  0  0  0  0  1|     8| 0  0  0  0  0  0  0  0  0  0|
9| 0  X  1  0  0  0  0  0  0  0|     9| 0  X  X  X  X  0  0  0  0  0|

Jogador, qual linha deseja atacar? 9
Jogador, qual coluna deseja atacar? 7
Seu oponente está atacando na linha 6 e coluna 8
   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9
_______________________________      _______________________________
0| -  0  0  1  0  0  -  -  0  0|     0| 0  0  0  0  0  X  X  0  0  0|
1| 0  1  0  0  -  1  1  X  1  0|     1| 0  0  0  0  0  X  X  X  0  0|
2| 0  1  0  1  0  0  0  0  0  -|     2| 0  0  0  0  0  0  0  X  0  0|
3| 0  0  0  1  0  0  0  -  0  0|     3| 0  0  0  0  0  0  X  X  0  0|
4| -  0  0  -  0  1  0  1  0  0|     4| 0  0  0  X  0  0  0  0  0  0|
5| -  0  0  -  0  0  0  1  0  0|     5| 0  0  0  X  0  0  0  0  0  0|
6| -  1  1  X  0  0  0  1  -  -|     6| X  X  X  X  0  0  0  0  0  0|
7| 0  0  0  0  0  0  0  -  0  0|     7| 0  0  0  0  0  0  0  0  0  0|
8| -  0  0  -  1  0  0  0  0  1|     8| 0  0  0  0  0  0  0  0  0  0|
9| 0  X  1  0  0  0  0  0  0  0|     9| 0  X  X  X  X  0  0  X  0  0|

Jogador, qual linha deseja atacar? 7
Jogador, qual coluna deseja atacar? 6
Parabéns! Você derrubou todos os navios do seu oponente!
```

```
1
5
2
6
1
2
4
7
1
1
1
1
2
3
1
9
1
2
0
3
4
5
8
9
8
4
1
6
1
7
0
5
1
5
3
6
3
7
6
0
6
1
6
2
4
3
5
3
6
3
9
1
9
2
9
3
9
4
2
7
0
6
9
7
7
6

```
