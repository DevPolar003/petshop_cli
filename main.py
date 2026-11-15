import cores  # noqa: I001
from armazenamento import read_json
from validacao import tem_texto
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

try:
    show_logo()
    show_menu()

    while True:
        op = input("Escolha a opção desejada: ")

        match op:
            case "1":
                while True:
                    try:
                        dict = read_json()
                        cod = int(input("Codigo: "))
                        if checar_id(cod):
                            print(f"{cores.RED}Código já utilizado!{cores.RESET}")
                            continue

                        nome = input("Nome: ").strip()
                        if not tem_texto(nome):
                            print(
                                f"{cores.RED}Nome inválido. Por favor, insira um nome válido.{cores.RESET}"
                            )
                            continue

                        categoria = input("Categoria: ").strip()
                        if not tem_texto(categoria):
                            print(
                                f"{cores.RED}Categoria inválida. Por favor, insira uma categoria válida.{cores.RESET}"
                            )
                            continue

                        preco = float(input("Preço: "))
                        qnt = int(input("Quantidade: "))
                        break
                    except ValueError:
                        print(
                            f"{cores.RED}Valor invalido, tente novamente.{cores.RESET}"
                        )
                        continue

                criar_produto(cod, nome, categoria, preco, qnt)

            case "2":
                show_submenu()
                while True:
                    op = input(
                        f"{cores.MARGEM}{cores.AZUL}Escolha a opção desejada: {cores.RESET}"
                    )

                    match op:
                        case "1":
                            listar_todos()
                        case "2":
                            try:
                                palavra = (
                                    input(f"{cores.MARGEM}{cores.AZUL}Digite a palavra chave desejada: {cores.RESET}")
                                    .strip()
                                    .lower()
                                )
                            except ValueError:
                                print(
                                    f"{cores.RED}Valor inválido. Por favor, insira uma palavra válida.{cores.RESET}"
                                )
                                continue
                            palavra_chave(palavra)
                        case "3":
                            try:
                                categoria = (
                                    input(f"{cores.MARGEM}{cores.AZUL}Digite a categoria desejada: {cores.RESET}")
                                    .strip()
                                    .lower()
                                )
                            except ValueError:
                                print(
                                    f"{cores.RED}Valor inválido. Por favor, insira uma categoria válida.{cores.RESET}"
                                )
                                continue
                            categoria_chave(categoria)
                        case "4":
                            try:
                                min = float(input("Digite o preço minimo: "))
                                max = float(input("Digite o preço maxímo: "))
                            except ValueError:
                                print(
                                    f"{cores.RED}Valor inválido. Por favor, insira um preço válido.{cores.RESET}"
                                )
                                continue
                            faixa_preco(min, max)
                        case "5":
                            try:
                                min = int(input("Digite a quantidade minima: "))
                                max = int(input("Digite a quantidade maxíma: "))
                            except ValueError:
                                print(
                                    f"{cores.RED}Valor inválido. Por favor, insira uma quantidade válida.{cores.RESET}"
                                )
                                continue
                            faixa_qnt(min, max)
                        case "6":
                            print(f"{cores.VERDE}Saindo dos Filtros...{cores.RESET}")
                            break
                        case _:
                            print(
                                f"{cores.RED}Opção inválida. Por favor, escolha uma opção válida.{cores.RESET}",
                                ValueError,
                            )

            case "3":
                print(f"{cores.VERDE}Saindo do programa.{cores.RESET}")
                break
            case _:
                print(
                    f"{cores.RED}Opção inválida. Por favor, escolha uma opção válida.{cores.RESET}",
                    ValueError,
                )

# 6. caso de erro a peneira pega o erro e
# devolve para o terminal tratada.

except ValueError:
    print(
        f"{cores.RED}Erro: Valor inválido. Por favor, insira um número válido. {cores.RESET}",
        ValueError,
    )
