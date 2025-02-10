'''
1. Crea una pequeña aplicación que sirva para gestionar las notas de un
curso y las guarde en un documento .txt
2. Organiza la información del archivo para que quede guardada ordenada
alfabéticamente.
3. Crea una función que modifique la nota del alumno indicado en el
archivo txt.
Api
'''

try:
    fichero = open('notas.txt')

except Exception as error:
    pass
    print('ERROR AL ABRIR EL FICHERO')
else:
    respuesta = 'a'
    while (respuesta != '*'):
        print('[0] Añadir alumnos y notas')
        print('[1] Organizar información alfabéticamente')
        print('[2] Modificar nota alumno')
        print('[*] SALIR')
        respuesta = input()

        if (respuesta == 0):
            with open("notas.txt", "w", encoding="utf-8")as f:
                f.write('Nahuel: 8')
                f.write('Jorge: 10')
                f.write('Luis: 10')
        elif (respuesta == 1):
            with open("notas.txt", "r", encoding="utf-8") as f:
                lista = f.readlines()
                reorganizado = lista.sort
                f.writelines(reorganizado)
        elif (respuesta == 2):
            with open("notas.txt", "w", encoding="utf-8") as f:


finally:
    fichero.close()


'''
1. Haz uso del api https://open.er-api.com/v6/latest/usd para realizar una
calculadora la cual transforme de euros a dólares.
'''
from urllib import request
from json import loads

f = request.urlopen("https://open.er-api.com/v6/latest/eur")
datos_json = f.read().decode("utf-8")
datos_dicc = loads(datos_json)

euros = input('Introduca la cantidad de €: ')

conversion = datos_dicc['rates'] ['USD']

dolares = float(euros) * conversion

print(dolares)
