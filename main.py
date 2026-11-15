import os
os.system("clear")



from utils import (show_logo, show_menu,show_submenu)
from produtos import (criar_produto, listar_todos, palavra_chave, categoria_chave
                      , faixa_preco, faixa_qnt
                      )
from json_stuff import (read_json)
import cores

#1. abre a peneira de erro.
try:

    #2. mostra o menu e as opções.
    show_logo()
    show_menu()

    #3. inicia o loop infinito.
    while True:

        #4. pede a opção para o usuario.
        op = input("Escolha a opção desejada: ")

        #5. abre a checagem da opção
        match op:
            case "1":


                while True:
                    try:
                        cod = int(input("Codigo: "))
                        dict = read_json()
                        for i in dict:
                            if cod == i['codigo']:
                                print(f"{cores.RED}Codigo já ultilizado! {cores.RESET}")
                                continue

                        nome = input("Nome: ")
                        categoria = input("Categoria: ")
                        preco = float(input("Preço: "))
                        qnt = int(input("Quantidade: "))
                        break
                    except ValueError:
                        print(f"{cores.RED}Valor invalido, tente novamente.{cores.RESET}")
                        continue

                criar_produto(cod, nome, categoria, preco, qnt)

            case "2":
                show_submenu()
                while True:

                        op = input(f"{cores.MARGEM}{cores.AZUL}Escolha a opção desejada: {cores.RESET}")

                        match op:
                            case "1":
                                listar_todos()
                            case "2":
                                palavra = input("Digite a palavra chave desejada: ").strip().lower()
                                palavra_chave(palavra)
                            case "3":
                                categoria = input("Digite a categoria desejada: ").strip().lower()
                                categoria_chave(categoria)
                            case "4":
                                min = float(input("Digite o preço minimo: "))
                                max = float(input("Digite o preço maxímo: "))
                                faixa_preco(min, max)
                            case "5":
                                min = int(input("Digite a quantidade minima: "))
                                max = int(input("Digite a quantidade maxíma: "))
                                faixa_qnt(min, max)
                            case "6":
                                print(f"{cores.VERDE}Saindo dos Filtros...{cores.RESET}")
                                break
                            case _:
                                print(f"{cores.RED}Opção inválida. Por favor, escolha uma opção válida.{cores.RESET}", ValueError)

            case "3":
                print(f"{cores.VERDE}Saindo do programa.{cores.RESET}")
                break
            case _:
                print(f"{cores.RED}Opção inválida. Por favor, escolha uma opção válida.{cores.RESET}", ValueError)

# 6. caso de erro a peneira pega o erro e
# devolve para o terminal tratada.

except ValueError:
    print(f"{cores.RED}Erro: Valor inválido. Por favor, insira um número válido. {cores.RESET}", ValueError)
