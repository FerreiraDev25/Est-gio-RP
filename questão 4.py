def proximo_elemento():
    # Sequência a) 1, 3, 5, 7, ___
    def sequencia_a():
        return 7 + 2

    # Sequência b) 2, 4, 8, 16, 32, 64, ____
    def sequencia_b():
        return 64 * 2

    # Sequência c) 0, 1, 4, 9, 16, 25, 36, ____
    def sequencia_c():
        n = 7
        return n * n

    # Sequência d) 4, 16, 36, 64, ____
    def sequencia_d():
        n = 10
        return n * n

    # Sequência e) 1, 1, 2, 3, 5, 8, ____
    def sequencia_e():
        fib = [1, 1, 2, 3, 5, 8]
        return fib[-1] + fib[-2]

    # Sequência f) 2, 10, 12, 16, 17, 18, 19, ____
    def sequencia_f():
        return 19 + 1

    # Calculando e imprimindo o próximo elemento de cada sequência
    print("Sequência a) 1, 3, 5, 7, ___")
    print(f"Próximo elemento: {sequencia_a()}")

    print("\nSequência b) 2, 4, 8, 16, 32, 64, ____")
    print(f"Próximo elemento: {sequencia_b()}")

    print("\nSequência c) 0, 1, 4, 9, 16, 25, 36, ____")
    print(f"Próximo elemento: {sequencia_c()}")

    print("\nSequência d) 4, 16, 36, 64, ____")
    print(f"Próximo elemento: {sequencia_d()}")

    print("\nSequência e) 1, 1, 2, 3, 5, 8, ____")
    print(f"Próximo elemento: {sequencia_e()}")

    print("\nSequência f) 2, 10, 12, 16, 17, 18, 19, ____")
    print(f"Próximo elemento: {sequencia_f()}")


# Executa a função
proximo_elemento()