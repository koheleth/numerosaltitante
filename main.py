#!/usr/bin/python
# -*- coding: utf-8 -*
from saltitante import Saltitante
from time import time


def main():
    inicio = time()

    saltitante = Saltitante(percentual=99.)
    saltitante.mostra_detalhes()

    fim = time()
    diferenca = fim - inicio
    print(f'\ntempo {diferenca:.3f}s')


if __name__ == '__main__':
    main()
