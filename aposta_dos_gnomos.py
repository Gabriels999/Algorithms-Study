# https://www.beecrowd.com.br/judge/pt/problems/view/3168

entrada = int(input('entrada: '))

for aposta in range(entrada):
    presentes = int(input('qtd presentes: '))
    chute_defeituoso_basy = int(input('qtd defeituosos: '))
    porcentagem = int(input('porcentagem: '))

    chance_do_presente_ser_bom = porcentagem/100
    chance_do_presente_ser_ruim = 1-chance_do_presente_ser_bom

    chance_do_presente_ser_ruim= chance_do_presente_ser_ruim**chute_defeituoso_basy
    aux = presentes-chute_defeituoso_basy
    chance_do_presente_ser_bom= chance_do_presente_ser_bom**(presentes-chute_defeituoso_basy)

    print(chance_do_presente_ser_bom, '|', chance_do_presente_ser_ruim, '|', chance_do_presente_ser_bom/chance_do_presente_ser_ruim)
