# criar um sistema em que o usuário irá escolher o tamanho da pizza 
# (G 30 reais; M 20 reais; P 10 reais), informe o sabor (frango, calabresa e missarela), 
# se deseja adicional (se sim, +R$5), se deseja borda (se sim, +R$2) 
# e se deseja por delivery (se sim, +R$8). 
# Ao final, informar o valor total a ser pago

print ('Olá! Sou o atendente virtual da pizzaria e vou te auxiliar!')
s = input("Qual sabor deseja? Temos calabresa, mussarela e frango: ").strip().upper()
while s != "CALABRESA" and s != "MUSSARELA" and s != "FRANGO":
    print ("Não temos este sabor :( pode escolher um dos disponíveis?")
    s = input("Qual sabor deseja? Temos calabresa, mussarela e frango: ").strip().upper()
p = input('Qual tamanho deseja? P, M ou G? ').strip().upper()
while p != "P" and p != "M" and p != "G":
    print ('Não entendi. Digite novamente:')
    p = input('Qual tamanho deseja? P, M ou G? ').strip().upper()

if p == 'P':
    p = 10
elif p == 'M':
    p = 20
elif p == 'G':
    p = 30

ad = int(input("Deseja adicional? 1 para SIM, 2 para NÃO: "))
while ad != 1 and ad != 2:
    print('Não entendi. Digite novamente:')
    ad = int(input("Deseja adicional? 1 para SIM, 2 para NÃO: "))

if ad == 1:
    p = p + 5
elif ad == 2:
    p = p

b = int(input('Deseja borda? 1 para SIM, 2 para NÃO: '))
while b != 1 and b != 2:
    print('Não entendi. Digite novamente:')
    b = int(input('Deseja borda? 1 para SIM, 2 para NÃO: '))
if b == 1:
    p = p + 2
elif b == 2:
    p = p

dl = int(input('Deseja entrega por delivery? 1 para SIM, 2 para NÃO: '))
while dl != 1 and dl != 2:
    print('Não entendi. Digite novamente:')
    dl = int(input('Deseja entrega por delivery? 1 para SIM, 2 para NÃO: '))
if dl == 1:
    p = p + 8
elif dl == 2:
    p = p

print (f'Pizza de {s} é uma delícia! O valor total a ser pago será R${p}')
print ('Obrigado por comprar conosco!')