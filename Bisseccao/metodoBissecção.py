import math
# tem problema nao usar o with open?
arq_entrada = open("../entradas.txt", "r")

lista = arq_entrada.readlines()

arq_entrada.close()

# strip() remove espaços em branco e quebras de linha \n.
formula = lista[0].strip()
a = float(lista[1].strip())
b = float(lista[2].strip())
tolerancia = float(lista[3].strip())


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

    # ta certo criar o arquivo de saida por aq?
    arq_saida = open("saida.txt", "w")
    arq_saida.write(str(x))  # preciso converter de novo pra string?
    arq_saida.close()
else:
    print("Tente outro intervalo, pois f(a) e f(b) têm o mesmo sinal.")
