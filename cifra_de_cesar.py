entrada = input()
resposta = ''

for numero in range(int(entrada)):
    palavra = input()
    chave = input()
    for letra in palavra:
        codigo_numerico = ord(letra)
        resposta += chr(int(codigo_numerico)-int(chave))
    print(resposta)
    resposta = ''
