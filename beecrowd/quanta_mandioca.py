# https://www.beecrowd.com.br/judge/pt/problems/view/2936

convidados = {
    'curupira': 300,
    'boitata': 1500,
    'boto': 600,
    'mapinguari': 1000,
    'iara': 150
}
mandioca = 0

for chave, valor in convidados.items():
    entrada = int(input())
    mandioca+= entrada*valor
mandioca+=225
print(mandioca)