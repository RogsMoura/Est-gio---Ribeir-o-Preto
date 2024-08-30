#1 =============================================================================
def pertence_fibonacci(numero):

    if numero < 0:
        return False

    a, b = 0, 1

    if numero == a or numero == b:
        return True
    
    while b < numero:
        a, b = b, a + b
        if b == numero:
            return True
    return False

def main1():
    try:
        numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
        
        if pertence_fibonacci(numero):
            print(f"O número {numero} pertence à sequência de Fibonacci.")
        else:
            print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")
    
    except ValueError:
        print("Por favor, insira um número válido.")

if __name__ == "__main__":
    main1()


#2 =============================================================================

def contar_letra_a(s):

    quantidade = s.lower().count('a')
    existe = quantidade > 0
    return existe, quantidade

def main2():
    
    string = input("Digite uma string para verificar a ocorrência da letra 'a': ")
    
    existe, quantidade = contar_letra_a(string)
    
    if existe:
        print(f"A letra 'a' (maiúscula ou minúscula) ocorre {quantidade} vez(es) na string.")
    else:
        print("A letra 'a' (maiúscula ou minúscula) não ocorre na string.")

if __name__ == "__main__":
    main2()


#3 =============================================================================
INDICE = 12
SOMA = 0
K = 1

while K < INDICE:
    K = K + 1 
    SOMA = SOMA + K  

print(SOMA)


#4 =============================================================================
"""
a) 9
b) 128
c) 49
d) 100
e) 13
f) 200
"""


#5 =============================================================================
"""
Ligue o interruptor A de 10~15 minutos, depois desligue
Ligue o interruptor B, deixe ligada
Vá na sala das lampadas
A lampada que tiver ligada, é do do interruptor B
A lampada que tiver quente, é do interruptor A
A lampada que tiver fria, é do interruptor C
"""