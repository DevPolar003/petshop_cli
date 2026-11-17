from armazenamento import add_json, read_json
from interface import mostrar_tabela

def criar_produto(
    cod: int, nome: str, categoria: str, preco: float, quantidade: int
) -> None:
    produto = {
        "codigo": cod,
        "nome": nome,
        "categoria": categoria,
        "preco": preco,
        "quantidade": quantidade,
    }
    lista = read_json()
    lista.append(produto)
    add_json(lista)


def checar_id(cod: int) -> bool:
    for item in read_json():
        if item["codigo"] == cod:
            return True
    return False


def listar_todos() -> None:
    mostrar_tabela(read_json(), "Todos os produtos")


### filtros ###


def palavra_chave(palavra: str) -> None:
    palavra = palavra.lower().strip()
    valores = [i for i in read_json() if palavra in i["nome"].lower()]
    mostrar_tabela(valores, "Busca por nome")


def categoria_chave(palavra: str) -> None:
    palavra = palavra.lower().strip()
    valores = [i for i in read_json() if palavra in i["categoria"].lower()]
    mostrar_tabela(valores, "Busca por categoria")


def faixa_qnt(minimo: int, maximo: int) -> None:
    valores = [i for i in read_json() if minimo < i["quantidade"] < maximo]
    mostrar_tabela(valores, "Faixa de quantidade")


def faixa_preco(minimo: float, maximo: float) -> None:
    valores = [i for i in read_json() if minimo < i["preco"] < maximo]
    mostrar_tabela(valores, "Faixa de preço")
