# Guia de Preparação de Semestre

Este guia tem como objetivo auxiliar os professores a preparar o ambiente do Prairie Learn e do GitHub pages para um novo semestre.

## 1. Criando um novo Course.

Para criar um novo Course no Prairie Learn, siga os passos:

1. Acesse o site do Prairie Learn ([https://us.prairielearn.com](https://us.prairielearn.com)).
2. Clique em **Sign in**.
3. Escolha a opção de login com Microsoft e insira suas credenciais Insper.
4. Acesse o Course do semestre anterior de DesSoft.
5. Vá em `Settings` e clique em `Make a copy of this course instance`.
6. Altere o Long Name do curso para o padrão `Design de Software 202X-Y` onde `X` é o ano e `Y` é o semestre (1 ou 2).
7. Altere o CIID para o padrão `202X-Y` onde `X` é o ano e `Y` é o semestre (1 ou 2).
8. O **identificador do curso** está presente no campo `Student Link`. O link tem o formato `https://us.prairielearn.com/pl/course_instance/XXXXX` onde `XXXXX` é o identificador do curso.
9. **Pronto!** Seu novo Course está criado no Prairie Learn.

Para atualizar os links do GitHub Pages, siga os passos:

1. Crie um **token de acesso** no Prairie Learn. Para isso, acesse o site do Prairie Learn ([https://us.prairielearn.com](https://us.prairielearn.com)), e no canto superior direito, clique no seu nome e depois em `Settings`. Vá em `Personal Access Tokens` e clique em `Generate New Token`. Dê um nome ao token e copie o valor gerado.
1. Acesse o repositório do GitHub Pages ([https://github.com/insper/DesignDeSoftware](https://github.com/insper/DesignDeSoftware)).
1. Clone o repositório em sua máquina local.
1. Duplique o arquivo `.env.example` e renomeie para `.env`.
1. Altere o valor da variável `TOKEN` para o **token de acesso** do Prairie Learn.
1. Altere o valor da variável `COURSE_INSTANCE_ID` para o **identificador do curso**.
1. Execute o script `update_assessments.py`.
1. Verifique se os links foram atualizados corretamente.
1. Faça um commit/push das mudanças no branch `main`.
1. Faça o deploy utilizando o comando `mkdocs gh-deploy`.
1. **Pronto!** Seu GitHub Pages está atualizado com os links do novo semestre.
