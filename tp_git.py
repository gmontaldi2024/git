"""
Nombre y Apellido: Gaston Montaldi
TP N5
Comision : Martes 
"""

def crearempleado(linea):
    empldicc = {}
    items = linea.split(",")
    for item in items:
        caract = item.split(":")
        empldicc[caract[0].strip()] = caract[1].strip()
    return empldicc

with open("empleados.txt", "r") as empleados:
    lineas = empleados.read()
lineas = lineas.split("\n")

def leerEmpleados():
    lista = []
    with open("archivo.txt", "r") as empleados:
        lineas = empleados.read()
    lineas = lineas.split("\n")
    for linea in lineas:
        empldicc = crearempleado(linea)
        lista.append(empldicc)
    return lista

ingreso = input("Ingrese un id: ")
while ingreso != "id":
    if empleados["id"] != ingreso:
        print("Error. Id no existente")
    else:
        print(empleados)

# no he podido terminar el trabajo, me falta la ultima parte de cambiar el salario