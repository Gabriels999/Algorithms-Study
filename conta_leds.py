entrada = input()

listagem = {
    "0": 6,
    "1": 2,
    "2": 5,
    "3": 5,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 3,
    "8": 7,
    "9": 6,
}

for valores in range(int(entrada)):
    numeros_para_contar = input()
    resposta = 0
    for numero in numeros_para_contar:
        leds = listagem.get(numero)
        resposta+= leds
    print(f"{resposta} leds")