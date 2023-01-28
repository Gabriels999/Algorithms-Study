# https://www.beecrowd.com.br/judge/pt/problems/view/1253

qtd_casos = input()
codigo_asc_transformado = ''
resposta = ''

for numero in range(int(qtd_casos)):
    palavra = input()
    chave = int(input())
    for letra in palavra:
        codigo_asc = ord(letra)
        codigo_asc_transformado = codigo_asc - chave
        if codigo_asc_transformado < 65:
            codigo_asc_transformado+=26
        resposta += chr(codigo_asc_transformado)
    print(resposta)
    resposta = ''

