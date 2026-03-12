from entidades.empleado import Empleado
from entidades.marketin import Marketing
from entidades.operador import Operador
from entidades.ingeniero import Ingeniero

try:

    print("como se llama el empleado?")
    nombre=input()

    print("cuantos dias trabajo el empleado?")
    dias_trabajados=int(input())

    print("cuantas horas trabajo a la semana?")
    horas_trabajadas=float(input())

    persona=input("el trabajador nos debe?")
    if persona == "si":
      print("cuanto le descontamos?")
      deuda=float(input())
    else:
        print("okay")
        
except ValueError: print("valor no reconocido, por favor pon caracteres correctos para  la ocacion ")
    


   








