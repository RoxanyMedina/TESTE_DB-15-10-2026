def somar(a, b):
    return a + b

def dividir(a, b):
    return a / b

def classificar_idade(idade):
    if idade < 0:
        raise ValueError("Idade não pode ser negativa")

    if idade >= 18:
        return "MAIOR DE IDADE"

    return "MENOR DE IDADE"