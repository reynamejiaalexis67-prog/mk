from entidades.empleado import Empleado  # importacion de clase
from entidades.marketin import Marketing  
from entidades.operador import Operador  
from entidades.ingeniero import Ingeniero  

try:
  
  
    print(" bienvenido a la creacion de cheques de temaki lastawi")

    print("como se llama el empleado?")
    nombre = input()  # parametro ingresado por el usuario

    print("cuantos dias trabajo el empleado?")
    dias_trabajados = int(input())  

    print("cuantas horas trabajo en toda la semana la semana?")
    horas_trabajadas = float(input()) 

    persona = input("el trabajador nos debe? ") 

    if persona == "si":
        print("cuanto le descontamos?")
        descuento = float(input())  
    else:
        descuento = 0  # valor asignado

    tipo = input("tipo de empleado (INGENIERO/MARKETING/OPERADOR): ").lower()  
    #lowe para que todo texto sea convertido a minuscula
    
    
    if tipo == "ingeniero":

        bono_salida = float(input("bono salida: "))  # parametro
        bono_inteligencia = float(input("bono inteligencia: "))  

        empleado = Ingeniero(nombre,
                             dias_trabajados,
                             horas_trabajadas,
                             descuento,
                             bono_salida,
                             bono_inteligencia)  
        # objeto creado 

        total = empleado.calcular_salario()  # llamada al metodo 

        print(empleado.nombre)

        print("el salario total es:", total, " de pesos mexicanos")  # uso del valor de retorno


    elif tipo == "marketing":

        bono_venta = float(input("bono_venta:")) 
        bono_satifaccion = float(input("bono_satifaccion:"))  # parametro

        empleado = Marketing(nombre,
                             dias_trabajados,
                             horas_trabajadas,
                             descuento,
                             bono_satifaccion,
                             bono_venta)  
        # objeto creado 

        total = empleado.calcular_salario()  # llamada al metodo

        print("el salario total es:", total, "de pesos mexicanos")  # valor de retorno

        print(empleado.nombre)


    elif tipo == "operador":

        bono_por_pieza = float(input("bono por pieza:"))  # parametro

        empleado = Operador(nombre,
                            dias_trabajados,
                            horas_trabajadas,
                            descuento,
                            bono_por_pieza)  
        # objeto creado 

        total = empleado.calcular_salario()  # llamada al metodo 

        print("el salario total es:", total, " de pesos mexicanos")  # valor de retorno

        print(empleado.nombre)

    else:

        print("no se encontro ningu tipo de empleado")

except ValueError:
    print("valor no reconocido, por favor pon caracteres correctos")