import time


def identificar_interruptores():
    # Simula a lógica das lâmpadas
    # 0 - Apagada, 1 - Acesa, 2 - Quente (mas não acesa)

    # Estado dos interruptores:
    interruptores = {
        "Interruptor 1": 0,
        "Interruptor 2": 0,
        "Interruptor 3": 0
    }

    # Estado das lâmpadas (inicialmente todas apagadas e frias)
    lampadas = {
        "Lâmpada 1": 0,
        "Lâmpada 2": 0,
        "Lâmpada 3": 0
    }

    # Passo 1: Ligue o Interruptor 1 por 10 minutos
    interruptores["Interruptor 1"] = 1
    print("Liguei o Interruptor 1")
    time.sleep(10)  # Simula o tempo de espera de 10 minutos

    # Passo 2: Desligue o Interruptor 1 e ligue o Interruptor 2
    interruptores["Interruptor 1"] = 0
    interruptores["Interruptor 2"] = 1
    print("Desliguei o Interruptor 1 e liguei o Interruptor 2")

    # Simula a situação das lâmpadas
    lampadas["Lâmpada 1"] = 2  # Lâmpada quente (Interruptor 1)
    lampadas["Lâmpada 2"] = 1  # Lâmpada acesa (Interruptor 2)
    lampadas["Lâmpada 3"] = 0  # Lâmpada apagada (Interruptor 3)

    # Passo 3: Vá até as salas das lâmpadas e identifique o estado
    for nome_lampada, estado in lampadas.items():
        if estado == 1:
            print(f"{nome_lampada} está acesa.")
        elif estado == 2:
            print(f"{nome_lampada} está quente.")
        else:
            print(f"{nome_lampada} está apagada.")

    # Determinar qual interruptor controla qual lâmpada
    for nome_interruptor in interruptores.keys():
        if interruptores[nome_interruptor] == 1:
            print(f"{nome_interruptor} controla a lâmpada que está acesa.")
        else:
            print(f"{nome_interruptor} controla a lâmpada que está fria.")

    print("Análise final:")
    print("Lâmpada quente e acesa: Controlada pelo Interruptor 1")
    print("Lâmpada acesa e quente: Controlada pelo Interruptor 2")
    print("Lâmpada apagada e fria: Controlada pelo Interruptor 3")


# Executa a função
identificar_interruptores()