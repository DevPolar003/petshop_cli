import json
import os

import cores

arc = "./data/produtos.json"


def read_json() -> list[dict]:
    if os.path.exists(arc):
        with open(arc, "r", encoding="utf-8") as f:
            return json.load(f)

    with open(arc, "w", encoding="utf-8") as f:
        json.dump([], f, indent=4)
        return []


def add_json(lista_prod: list[dict]) -> None:
    with open(arc, "w", encoding="utf-8") as f:
        json.dump(lista_prod, f, indent=4, ensure_ascii=False)
        print(f"{cores.VERDE}Produto adicionado com sucesso! {cores.RESET}")
