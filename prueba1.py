print("what is your elo in lol?")
elo_str = input("Ingrese su elo en lol y presione Enter: ")

try:
    elo = float(elo_str)
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
while True:
    if elo.isdigit():
        numero= int(elo)
        break
    else:
        print("error: Por favor ingrese un valor válido")
print("Gracias por usar el programa")                    