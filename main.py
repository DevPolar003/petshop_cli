import utils  # noqa: I001

from interface import show_logo, show_menu, show_submenu
from produtos import (
    categoria_chave,
    checar_id,
    criar_produto,
    faixa_preco,
    faixa_qnt,
    listar_todos,
    palavra_chave,
)


def erro(mensagem: str) -> None:
    print(f"{utils.RED}{mensagem}{utils.RESET}")

def tem_texto(string: str) -> bool:
    return bool(string)


def cadastrar_produto() -> None:
    while True:
        try:
            cod = int(input("Codigo: "))
            if checar_id(cod):
                erro("Código já utilizado!")
                continue

            nome = input("Nome: ").strip()
            if not tem_texto(nome):
                erro("Nome inválido. Por favor, insira um nome válido.")
                continue

            categoria = input("Categoria: ").strip()
            if not tem_texto(categoria):
                erro("Categoria inválida. Por favor, insira uma categoria válida.")
                continue

            preco = float(input("Preço: "))
            qnt = int(input("Quantidade: "))
            break
        except ValueError:
            erro("Valor inválido, tente novamente.")

    criar_produto(cod, nome, categoria, preco, qnt)


def pedir_palavra() -> None:
    prompt = f"{utils.MARGEM}{utils.AZUL}Digite a palavra chave desejada: {utils.RESET}"
    palavra = input(prompt).strip().lower()
    if not tem_texto(palavra):
        erro("Valor inválido. Por favor, insira uma palavra válida.")
        return
    palavra_chave(palavra)


def pedir_categoria() -> None:
    prompt = f"{utils.MARGEM}{utils.AZUL}Digite a categoria desejada: {utils.RESET}"
    categoria = input(prompt).strip().lower()
    if not tem_texto(categoria):
        erro("Valor inválido. Por favor, insira uma categoria válida.")
        return
    categoria_chave(categoria)


def pedir_faixa_preco() -> None:
    try:
        preco_min = float(input("Digite o preço mínimo: "))
        preco_max = float(input("Digite o preço máximo: "))
    except ValueError:
        erro("Valor inválido. Por favor, insira um preço válido.")
        return
    faixa_preco(preco_min, preco_max)


def pedir_faixa_qnt() -> None:
    try:
        qnt_min = int(input("Digite a quantidade mínima: "))
        qnt_max = int(input("Digite a quantidade máxima: "))
    except ValueError:
        erro("Valor inválido. Por favor, insira uma quantidade válida.")
        return
    faixa_qnt(qnt_min, qnt_max)


def menu_filtros() -> None:
    show_submenu()
    while True:
        op = input(f"{utils.MARGEM}{utils.AZUL}Escolha a opção desejada: {utils.RESET}")

        match op:
            case "1":
                listar_todos()
            case "2":
                pedir_palavra()
            case "3":
                pedir_categoria()
            case "4":
                pedir_faixa_preco()
            case "5":
                pedir_faixa_qnt()
            case "6":
                print(f"{utils.VERDE}Saindo dos Filtros...{utils.RESET}")
                return
            case _:
                erro("Opção inválida. Por favor, escolha uma opção válida.")


def menu_principal() -> None:
    show_logo()
    show_menu()
    while True:
        op = input("Escolha a opção desejada: ")

        match op:
            case "1":
                cadastrar_produto()
            case "2":
                menu_filtros()
            case "3":
                print(f"{utils.VERDE}Saindo do programa.{utils.RESET}")
                return
            case _:
                erro("Opção inválida. Por favor, escolha uma opção válida.")


if __name__ == "__main__":
    try:
        menu_principal()
    except KeyboardInterrupt:
        print(f"\n{utils.VERDE}Programa encerrado.{utils.RESET}")
