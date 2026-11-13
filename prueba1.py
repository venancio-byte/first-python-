print("what is your elo in lol?")
elo = input("Ingrese su elo en lol y presione Enter: ")

try:
    elo = float(elo)
except ValueError:
    print("Por favor ingrese un valor válido")
else:
    if elo < 0:
        print("Por favor ingrese un valor válido")
    elif elo < 1000:
        print("Tu elo es bajo")
    elif elo < 2000:
        print("Tu elo es medio")
    else:
        print("Tu elo es alto")
    if elo.is_integer():
        numero = int(elo)
    else:
        print("error: Por favor ingrese un valor válido")
print("Gracias por usar el programa")                    