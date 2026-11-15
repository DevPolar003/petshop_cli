import os

import cores

os.system("cls")
from armazenamento import add_json, read_json

json = read_json()
lista_produtos = json


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

    lista_produtos.append(produto)
    print(lista_produtos)
    add_json(lista_produtos)


def checar_id(cod: int) -> bool:
    lista = read_json()
    for item in lista:
        if item["codigo"] == cod:
            return True
    return False


def listar_todos() -> None:
    lista = read_json()

    if not lista:
        print(f"{cores.MARGEM}{cores.CINZA} não há itens na lista.{cores.RESET}")
        return

    cabecalho = f"{'Cód':<6}{'Nome':<20}{'Categoria':<15}{'Preço':>10}{'Qtd':>6}"
    largura = len(cabecalho)

    print()
    print(f"{cores.MARGEM}{cores.NEGRITO}{cores.AZUL}{cabecalho}{cores.RESET}")
    print(f"{cores.MARGEM}{cores.AZUL}{'-' * largura}{cores.RESET}")

    for item in lista:
        print(
            f"{cores.MARGEM}"
            f"{item['codigo']:<6}"
            f"{item['nome']:<20}"
            f"{item['categoria']:<15}"
            f"{item['preco']:>10.2f}"
            f"{item['quantidade']:>6}"
        )
    print()


### filtros ###


def palavra_chave(palavra: str) -> None:
    palavra = palavra.lower().strip()
    lista = read_json()
    valores = []

    for item in lista:
        if palavra in item["nome"].lower():
            valores.append(item)

    if valores:
        cabecalho = f"{'Cód':<6}{'Nome':<22}{'Categoria':<16}{'Preço':>10}{'Qtd':>6}"
        print()
        print(
            f"{cores.MAGENTA_BRILHANTE}{cores.MARGEM}Itens encontrados: {len(valores)}{cores.RESET}"
        )
        print(f"{cores.MARGEM}{cores.NEGRITO}{cabecalho}{cores.RESET}")
        print(f"{cores.MARGEM}{cores.CINZA}{'-' * len(cabecalho)}{cores.RESET}")
        for p in valores:
            print(
                f"{cores.MARGEM}"
                f"{p['codigo']:<6}"
                f"{p['nome'][:20]:<22}"
                f"{p['categoria'][:14]:<16}"
                f"{p['preco']:>10.2f}"
                f"{p['quantidade']:>6}"
            )
        print()
    else:
        print(f"{cores.CINZA}{cores.MARGEM}Nenhum item foi encontrado.{cores.RESET}")


def categoria_chave(palavra: str) -> None:
    palavra = palavra.lower().strip()
    lista = read_json()
    valores = []

    for item in lista:
        if palavra in item["categoria"].lower():
            valores.append(item)

    if valores:
        cabecalho = f"{'Cód':<6}{'Nome':<22}{'Categoria':<16}{'Preço':>10}{'Qtd':>6}"
        print()
        print(
            f"{cores.MAGENTA_BRILHANTE}{cores.MARGEM}Itens encontrados: {len(valores)}{cores.RESET}"
        )
        print(f"{cores.MARGEM}{cores.NEGRITO}{cabecalho}{cores.RESET}")
        print(f"{cores.MARGEM}{cores.CINZA}{'-' * len(cabecalho)}{cores.RESET}")
        for p in valores:
            print(
                f"{cores.MARGEM}"
                f"{p['codigo']:<6}"
                f"{p['nome'][:20]:<22}"
                f"{p['categoria'][:14]:<16}"
                f"{p['preco']:>10.2f}"
                f"{p['quantidade']:>6}"
            )
        print()
    else:
        print(f"{cores.CINZA}{cores.MARGEM}Nenhum item foi encontrado.{cores.RESET}")


def faixa_qnt(min: int, max: int) -> None:

    lista = read_json()
    valores = []

    for item in lista:
        if item["quantidade"] > min and item["quantidade"] < max:
            valores.append(item)

    if valores:
        cabecalho = f"{'Cód':<6}{'Nome':<22}{'Categoria':<16}{'Preço':>10}{'Qtd':>6}"
        print()
        print(
            f"{cores.MAGENTA_BRILHANTE}{cores.MARGEM}Itens encontrados: {len(valores)}{cores.RESET}"
        )
        print(f"{cores.MARGEM}{cores.NEGRITO}{cabecalho}{cores.RESET}")
        print(f"{cores.MARGEM}{cores.CINZA}{'-' * len(cabecalho)}{cores.RESET}")
        for p in valores:
            print(
                f"{cores.MARGEM}"
                f"{p['codigo']:<6}"
                f"{p['nome'][:20]:<22}"
                f"{p['categoria'][:14]:<16}"
                f"{p['preco']:>10.2f}"
                f"{p['quantidade']:>6}"
            )
        print()
    else:
        print(f"{cores.CINZA}{cores.MARGEM}Nenhum item foi encontrado.{cores.RESET}")


def faixa_preco(min: float, max: float) -> None:

    lista = read_json()
    valores = []

    for item in lista:
        if item["preco"] > min and item["preco"] < max:
            valores.append(item)

    if valores:
        cabecalho = f"{'Cód':<6}{'Nome':<22}{'Categoria':<16}{'Preço':>10}{'Qtd':>6}"
        print()
        print(
            f"{cores.MAGENTA_BRILHANTE}{cores.MARGEM}Itens encontrados: {len(valores)}{cores.RESET}"
        )
        print(f"{cores.MARGEM}{cores.NEGRITO}{cabecalho}{cores.RESET}")
        print(f"{cores.MARGEM}{cores.CINZA}{'-' * len(cabecalho)}{cores.RESET}")
        for p in valores:
            print(
                f"{cores.MARGEM}"
                f"{p['codigo']:<6}"
                f"{p['nome'][:20]:<22}"
                f"{p['categoria'][:14]:<16}"
                f"{p['preco']:>10.2f}"
                f"{p['quantidade']:>6}"
            )
        print()
    else:
        print(f"{cores.CINZA}{cores.MARGEM}Nenhum item foi encontrado.{cores.RESET}")
