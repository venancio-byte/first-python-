from datetime import date
nombre= input("Ingrese su nombre y presione Enter: ")
edad= int(input("Ingrese su edad y presione Enter: "))
año_nacimiento= date.today().year-edad
año_actual= date.today().year
año_nacimiento= año_actual-edad
print("Hola, mi nombre es", nombre, "y nací en el año", año_nacimiento)