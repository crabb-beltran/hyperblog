import datetime

mensaje = "prueba terminal comandos"
contador = 0
hora = datetime.datetime.now()

while contador < 90:
    print(f'La {mensaje} hora {hora} {contador}')
    contador +=1

print ("Gracias")

