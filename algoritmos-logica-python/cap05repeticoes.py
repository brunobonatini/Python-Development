'''x = 1
while x <=3:
    print(x)
    x = x + 1
    
# Contadores
fim = int(input('Digite o último valor a ser impresso: '))
x = 1
while x <= fim:
    print(x)
    x += 1'''

fim = int(input('Digite o último valor a ser impresso: '))
x = 0
while x <= fim:
    if x % 2 == 0:
        print(x)
        x += 1

fim = int(input('Digite o último número a ser impresso: '))
x = 0
while x <= fim:
    if x % 2 == 0:
        print(x)
        x += 2  