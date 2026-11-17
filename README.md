# PETSHOP_CLI

Um aplicativo de linha de comando simples para cadastrar e pesquisar produtos, desenvolvido em Python puro. Os dados são armazenados em um arquivo JSON local, e a interface utiliza códigos de cores ANSI, sem a necessidade de bibliotecas externas.

## Funcionalidades

- Cadastro de produtos (código, nome, categoria, preço, quantidade)
- Prevenção contra códigos de produto duplicados
- Validação de entradas (campos vazios, números inválidos)
- Listagem de todos os produtos em uma tabela formatada
- Pesquisa com filtros:
- Por nome (palavra-chave)
- Por categoria
- Por faixa de preço
- Por faixa de quantidade

## Requisitos

- Python 3.10 ou superior (utiliza a estrutura `match`/`case`)
- Um terminal que suporte cores ANSI (a maioria dos terminais Linux/Mac, Windows Terminal)

## Como executar

```bash
git clone <url-do-seu-repositorio>
cd prod_cadastro
python main.py
```

## Uso

Ao iniciar o programa, o menu principal é exibido:

```
1 > Adicionar produto
2 > Pesquisar com filtros
3 > Sair
```

Digite o número da opção desejada e pressione Enter. A opção 2 abre o submenu de filtros, onde é possível listar todos os produtos ou filtrar por nome, categoria, faixa de preço ou faixa de quantidade.

## Estrutura do projeto

```
prod_cadastro/
├── main.py            # ponto de entrada e loops de menu
├── cores.py           # constantes de cores ANSI
├── armazenamento.py   # leitura/escrita do arquivo JSON
├── produtos.py        # regras de negócio: criação, verificação de ID, filtros
├── interface.py       # logotipo, menus e exibição de tabelas
├── validacao.py       # funções auxiliares para validação de entradas
└── produtos.json      # dados salvos
```

O código está organizado por responsabilidades: **dados** (`armazenamento.py`), **regras de negócio** (`produtos.py`) e **interface** (`interface.py`). ## Formato dos dados

Os produtos são armazenados como uma lista de objetos:

```json
[
{
"codigo": 1,
"nome": "Guitarra Fender",
"categoria": "Cordas",
"preco": 4500.0,
"quantidade": 3
}
]
```

## Possíveis melhorias

- Editar e remover produtos (CRUD completo)
- Substituir a saída ANSI manual pela biblioteca [`rich`](https://github.com/Textualize/rich)
- Testes automatizados com `pytest`
- Substituir o JSON por SQLite

## Autor

Criado por Morgan como um projeto de aprendizado de Python.
