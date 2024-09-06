import requests
import json
URL ='https://drive.google.com/file/d/1qXvCPjEL4jerElN-hnScoKkEVmSQ8A2L/view'
with open('dados.json') as arquivo_json:

    dados = json.load(arquivo_json)

def menor_faturamento(dados):
    menor= dados[1]['valor']
    for i in range(len(dados)):
       if menor > dados[i]['valor'] and dados[i]['valor'] != 0:
           menor = dados[i]['valor']
    return menor

def maior_faturamento(dados):
    maior= dados[1]['valor']
    for i in range(len(dados)):
       if maior < dados[i]['valor']:
           maior = dados[i]['valor']
    return maior

def dias_maior_faturamento(dados):
    soma = 0
    dias = 0
    faturamento = []
    for i in range(len(dados)):
        if dados[i]['valor'] != 0:
            soma += dados[i]['valor']
            dias += dados[i]['dia']
        media = soma/dias
        if dados[i]['valor'] > media:
            faturamento.append(dados[i]['dia'])
    return faturamento



