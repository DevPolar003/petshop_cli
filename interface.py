import utils


def show_logo() -> None:

    print(f"""{utils.MAGENTA_BRILHANTE}

         /l _/l
        ( -.- )
         > ~ <
        l     l
       (  | |  )
        l_|_|_l
    ╔══════════════╗
    ║   PETSHOP    ║
    ╚══════════════╝
    {utils.RESET}""")
    print()

def show_submenu() -> None:
    print(f"{utils.MARGEM}{utils.AZUL} =+ Filtros += {utils.RESET}")
    print(f"{utils.MARGEM}{utils.AZUL}[1] Listar todos {utils.RESET}")
    print(f"{utils.MARGEM}{utils.AZUL}[2] Palavra chave {utils.RESET}")
    print(f"{utils.MARGEM}{utils.AZUL}[3] Categoria{utils.RESET}")
    print(f"{utils.MARGEM}{utils.AZUL}[4] Faixa de preco {utils.RESET}")
    print(f"{utils.MARGEM}{utils.AZUL}[5] Faixa de quantidade {utils.RESET}")
    print(f"{utils.MARGEM}{utils.AZUL}[6] Sair dos filtros {utils.RESET}")


def show_menu() -> None:
    print("[1] Adicionar produto")
    print("[2] Pesquisa com filtros")
    print("[3] Sair")




def mostrar_tabela(produtos: list[dict], titulo: str = "Produtos") -> None:
    """Imprime uma lista de produtos em formato de tabela."""
    if not produtos:
        print(f"{utils.MARGEM}{utils.CINZA}Nenhum item encontrado.{utils.RESET}")
        return

    cabecalho = f"{'Cód':<6}{'Nome':<22}{'Categoria':<16}{'Preço':>10}{'Qtd':>6}"

    print()
    print(f"{utils.MARGEM}{utils.MAGENTA_BRILHANTE}{titulo}: {len(produtos)}{utils.RESET}")
    print(f"{utils.MARGEM}{utils.NEGRITO}{cabecalho}{utils.RESET}")
    print(f"{utils.MARGEM}{utils.CINZA}{'-' * len(cabecalho)}{utils.RESET}")

    for p in produtos:
        print(
            f"{utils.MARGEM}"
            f"{p['codigo']:<6}"
            f"{p['nome'][:20]:<22}"
            f"{p['categoria'][:14]:<16}"
            f"{p['preco']:>10.2f}"
            f"{p['quantidade']:>6}"
        )
    print()
