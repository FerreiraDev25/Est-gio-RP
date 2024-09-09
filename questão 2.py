def contar_letra_a(s):
    # Conta a ocorrência das letras 'a' e 'A' na string
    count = s.lower().count('a')
    return count

def verificar_letra_a(s):
    # Verifica se a letra 'a' está presente e retorna uma mensagem com a contagem
    count = contar_letra_a(s)
    if count > 0:
        return f"A letra 'a' aparece {count} vez(es) na string."
    else:
        return "A letra 'a' não está presente na string."

# Solicita ao usuário que insira uma string
entrada = input("Digite uma string para verificar a letra 'a': ")

# Verifica e exibe o resultado
resultado = verificar_letra_a(entrada)
print(resultado)