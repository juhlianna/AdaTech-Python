# funções
# Funções utilizadas anteriormente

"""print() # imprime mensgaens int, float, str no terminal, cmd
input() # retorna um dado informado pelo usuario - entrada padrão - e recebe str
len() # recebe uma lista e retorna o tamanho dela
max() # retorna o maior valor de uma lista"""

# 2. Criação de funções


# Função inicial

def saudação():
    print("Seja bem-vinda")
    print("Olá, é um prazer ter você fazendo esse curso!")
    
saudação() # para chamar a função

# Função com parametros

def saudação(nome, curso): # posso determinar uma variavel para ser chamada dentro de uma função
    print(f"Seja bem-vinda, {nome} <3")
    print(f"É um prazer ter você fazendo parte do curso de {curso}!")

saudação("Juliana", "Cientista de Dados")
saudação("Marcia", " Engenheira de Automação")
saudação("Tais", "Design de moda")

# função com parametro default

def saudação(nome, curso = 'Cientista de Dados'): # posso definir o valor da variavel dentro da função
    print(f"Seja bem-vinda, {nome} <3")
    print(f"É um prazer ter você fazendo parte do curso de {curso}!")

saudação("Juliana", "Python") # o codigo aceita outro valor definido

# Funções com retorno

def soma(n1, n2):
    return n1 + n2

resultado = soma(5,7)
print("O resultado da soma é:", resultado)


def Calculadora(n1, n2, operação="+"):
    if operação == '+':
        return n1 + n2
    elif operação == '-':
        return n1 - n2
    
resultado = Calculadora(10, 20, '-')
print(resultado)