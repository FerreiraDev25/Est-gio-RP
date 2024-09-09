def pertence_fibonacci(n):
    # Função para verificar se um número pertence à sequência de Fibonacci
    if n < 0:
        return False

    a, b = 0, 1
    while a <= n:
        if a == n:
            return True
        a, b = b, a + b

    return False


# Solicita ao usuário que insira um número
numero = int(input("Digite um número para verificar se ele pertence à sequência de Fibonacci: "))

# Verifica se o número pertence à sequência e exibe a mensagem apropriada
if pertence_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")