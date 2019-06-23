#!/usr/bin/python3.6
# -*- coding: utf-8 -*


def crescente(numero):
    numero_texto = str(numero)
    eh_crescente = True
    for i in range(1, len(numero_texto)):
        antecessor = numero_texto[i - 1:i]
        sucessor = numero_texto[i:i + 1]
        if not(antecessor == '' or sucessor == ''):
            if antecessor > sucessor:
                eh_crescente = False
                break

    return eh_crescente


def decrescente(numero):
    numero_texto = str(numero)
    eh_decrescente = True
    for i in range(1, len(numero_texto)):
        antecessor = numero_texto[i - 1:i]
        sucessor = numero_texto[i:i + 1]
        if not(antecessor == '' or sucessor == ''):
            if antecessor < sucessor:
                eh_decrescente = False
                break

    return eh_decrescente


def saltitante_old(numero):
    if crescente(numero) and decrescente(numero):
        eh_saltitante = True
    else:
        eh_saltitante = False

    return eh_saltitante


def test_verifica(numero, limite_percentual, saltitante, not_saltitante):
    percentual = saltitante / (saltitante + not_saltitante) * 100
    numeros = [538, 21780, 1587000]
    percentuais_corretos = [50., 90., 99.]
    if numero in numeros:
        for i in range(len(numeros)):
            print(f'{numeros[i]} - {percentual:.6f}%')
            if percentuais_corretos[i] == percentual:
                print(' - ok')

    limite_percentual = float(limite_percentual)
    if percentual >= limite_percentual:
        return True
    else:
        return False


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


def calcula_saltitante_percentual(inicio = 1, fim = 999999999, percentual = 50.):

    total_saltitantes = 0
    total_no_saltitante = 0

    for i in range(inicio, fim + 1):
        if saltitante(i):
            total_saltitantes += 1
            if calcula_percentual(total_saltitantes, total_no_saltitante) == percentual:
                numero_saltitante = i
                break
        else:
            total_no_saltitante += 1

    return numero_saltitante, total_saltitantes, total_no_saltitante


def calcula_percentual(saltitante, no_saltitante):
    percentual = saltitante / (saltitante + no_saltitante) * 100
    return percentual


def mostra_resultado(numero_saltitante, total_saltitante, total_no_saltitante):
    print(f'\n{numero_saltitante} é o número saltitante que deseja.\n\n')
    print('Resumo:')
    print(f'Saltitantes: {total_saltitante}')
    print(f'Não Saltitantes: {total_no_saltitante}')

    percentual_saltitante = total_saltitante / (total_saltitante + total_no_saltitante) * 100
    print(f'Percentual de saltitantes {percentual_saltitante:.2f}%')

    percentual_nao_saltitante = total_no_saltitante / (total_saltitante + total_no_saltitante) * 100
    print(f'Percentual de não saltitantes {percentual_nao_saltitante:.2f}%')

    total = percentual_saltitante + percentual_nao_saltitante
    print(f'Total {total:.2f}%')
