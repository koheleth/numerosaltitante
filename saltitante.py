#!/usr/bin/python
# -*- coding: utf-8 -*
import sys


class Saltitante:
    total_saltitantes: int
    total_no_saltitantes: int
    numero: int = 0

    def __init__(self, inicio: int = 1, fim: int = 9999999, percentual: float = 50.):
        self._inicio = inicio
        self._fim = fim
        self._percentual = percentual
        self.calcula_detalhes()

    def __str__(self):
        return self.numero

    @staticmethod
    def saltitante(numero):
        numero_texto = str(numero)
        maior = False
        menor = False

        for i in range(1, len(numero_texto)):
            antecessor = numero_texto[i - 1:i]
            sucessor = numero_texto[i:i + 1]

            if not(antecessor == '' or sucessor == ''):
                if antecessor > sucessor:
                    maior = True
                if antecessor < sucessor:
                    menor = True

        eh_saltitante = maior and menor
        return eh_saltitante

    def calcula_detalhes(self):
        inicio = self._inicio
        fim = self._fim
        percentual = self._percentual
        total_saltitantes: int = 0
        total_no_saltitante: int = 0
        numero_saltitante: int = 0

        for i in range(inicio, fim + 1):
            if self.saltitante(i):
                total_saltitantes += 1
                if self.calcula_percentual(total_saltitantes, total_no_saltitante) == percentual:
                    numero_saltitante = i
                    break
            else:
                total_no_saltitante += 1

        self.numero = numero_saltitante
        self.total_saltitantes = total_saltitantes
        self.total_no_saltitantes = total_no_saltitante

    @staticmethod
    def calcula_percentual(saltitante, no_saltitante):
        percentual = saltitante / (saltitante + no_saltitante) * 100
        return percentual

    def mostra_detalhes(self):
        numero_saltitante = self.numero
        total_saltitante = self.total_saltitantes
        total_no_saltitante = self.total_no_saltitantes
        sys.stdout.write(f'\n{numero_saltitante} é o número saltitante que deseja.\n\n')
        sys.stdout.write('Resumo:\n')
        sys.stdout.write(f'\tNúmero Saltitante: {numero_saltitante}\n')
        sys.stdout.write(f'\tSaltitantes: {total_saltitante}\n')
        sys.stdout.write(f'\tNão Saltitantes: {total_no_saltitante}\n')

        percentual_saltitante = total_saltitante / (total_saltitante + total_no_saltitante) * 100
        sys.stdout.write(f'\tPercentual de saltitantes {percentual_saltitante:.2f}%\n')

        percentual_nao_saltitante = total_no_saltitante / (total_saltitante + total_no_saltitante) * 100
        sys.stdout.write(f'\tPercentual de não saltitantes {percentual_nao_saltitante:.2f}%\n')

        total = percentual_saltitante + percentual_nao_saltitante
        sys.stdout.write(f'\tTotal {total:.2f}%\n')
