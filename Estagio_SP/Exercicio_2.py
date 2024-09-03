numero_informado = (int(input('Escreva um número: ')))
Lista = [0,1]
i = 0

while Lista[i+1] < numero_informado:
    Fibonacci = Lista[i] + Lista[i+1]
    Lista.append(Fibonacci)
    i+= 1
if numero_informado in Lista:
    print('Esse número pertence a sequencia de Fibonacci')
else:
    print('Esse número não pertence a sequencia de Fibonacci')
print(Lista)