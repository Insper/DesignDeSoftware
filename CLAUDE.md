# DesignDeSoftware

Material do curso (mkdocs em `material/`) + repositório PrairieLearn do curso em `pl-insper-engdessoft/`.

## material/ (site mkdocs)

- **EPs:** o padrão do curso são dois Exercícios Programa, **EP1 e EP2** (as linhas do EP2 ficam
  comentadas em `material/index.md` quando não há EP2). Em **2026-2 houve um único EP**, chamado só
  de **EP** (peso 35% na Nota em Grupo; PF 65%). Em semestres futuros, voltar a EP1/EP2 salvo aviso.

## pl-insper-engdessoft (PrairieLearn)

Repositório git separado (e ignorado pelo `.gitignore` deste projeto) com **todas as provas e quizzes** do curso.
Estrutura padrão do PrairieLearn:

- `questions/` — banco de questões compartilhado entre semestres
- `courseInstances/<semestre>/assessments/` — provas, quizzes, EPs de cada oferta
- Semestres presentes: `2024-2`, `2025-1`, `2025-1-dp-ferias`, `2025-2`, `2025-2-dp-ferias`,
  `2026-1`, `2026-1-dp-ferias`, `2026-2`, `2026-2-dp-ferias`

### Regra: só editar 2026-2

**Só podemos trabalhar (criar/editar/alterar) na versão `2026-2`.**
Todas as outras versões de `courseInstances/` são **somente leitura**: servem apenas como
referência/estudo (ver como provas anteriores foram montadas, reaproveitar ideias de questões,
comparar formato). Nunca modificar, renomear ou apagar arquivos de semestres anteriores.

Se uma mudança parecer necessária fora de `2026-2`, avisar antes em vez de editar.
