""" 
METODO ORIGINAL DA BISSECCAO

import math

formula = input("Digite a formula em função de x: ")

a = float(input("Informe o valor inferior do intervalo (a): "))
b = float(input("Informe o valor superior do intervalo (b): "))
tolerancia = float(input("Informe o valor da tolerância: "))


def f(x):
    return eval(formula, {
        "x": x,
        "sin": math.sin,
        "cos": math.cos,
        "exp": math.exp,
        "ln": math.log,
        "sqrt": math.sqrt
    })


f_a = f(a)
f_b = f(b)


if (f_a * f_b) < 0:
    x = (a + b)/2
    resultado = f(x)
    # pode deixar sem o abs(x - x_anterior) > tolerancia? esta certo esse criterio de parada?
    while abs(resultado) > tolerancia and (b - a) > tolerancia:
        if f(a)*resultado < 0:
            b = x
        else:
            a = x
        x = (a + b)/2
        resultado = f(x)

    print(f"Raiz aproximada: {x}")
else:
    print("Tente outro intervalo, pois f(a) e f(b) têm o mesmo sinal.")
"""
