lista_notas = [100,50,20,10,5,2,1]

def devolve_notas(valor):
    resposta = {}
    for nota in lista_notas:
        if(valor>=nota):
            qtd_notas = 0
            qtd_notas = valor//nota
            restante = valor - (nota*qtd_notas)
            resposta[nota] = qtd_notas
            valor = restante
    print(resposta)

devolve_notas(235)