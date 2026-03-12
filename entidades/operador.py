from entidades.empleado import Empleado


class Operador(Empleado):
     def __init__(self, nombre:str,
                  dias_trabajados:float, 
                  horas_trabajadas:float,
                  descuento:float,
                  bono_por_pieza:float):
          super().__init__(nombre, dias_trabajados, horas_trabajadas, descuento)
          
          self.bono_por_pieza=bono_por_pieza
          
          
          
     def calcular_salario_operador(self):
              costo_base = self.calcular_salario_base()
              total = self.calcular_salario_operador + self.bono_por_pieza
              return total 
          
          
          
          
          