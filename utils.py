import cores
margem = " " * 4

def show_logo() -> None:

    print(f"""{cores.MAGENTA_BRILHANTE}

         /l _/l
        ( -.- )
         > ~ <
        l     l
       (  | |  )
        l_|_|_l
    ╔══════════════╗
    ║   PROD_CLI   ║
    ╚══════════════╝
    {cores.RESET}""")
    print()



def show_submenu() -> None:
    print(f"{margem}{cores.AZUL} =+ Filtros += {cores.RESET}")
    print(f"{margem}{cores.AZUL}[1] Listar todos {cores.RESET}")
    print(f"{margem}{cores.AZUL}[2] Palavra chave {cores.RESET}")
    print(f"{margem}{cores.AZUL}[3] Categoria{cores.RESET}")
    print(f"{margem}{cores.AZUL}[4] Faixa de preco {cores.RESET}")
    print(f"{margem}{cores.AZUL}[5] Faixa de quantidade {cores.RESET}")
    print(f"{margem}{cores.AZUL}[6] Sair dos filtros {cores.RESET}")



def show_menu() -> None:
    print("[1] Adicionar produto")
    print("[2] Pesquisa com filtros")
    print("[3] Sair")


