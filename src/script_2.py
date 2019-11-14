#!/usr/bin/env python3


def main(files):
    div = files.split("/")
    svc_name = div[0]
    if len(div) == 1:
        print(svc_name + " : Arquivo na raiz do projeto.")
        return 1
    if len(div[-1]) > 500:
        print("Erro no servico:" + div[0] + ": Nome muito longo")
        return 1
    return 0
