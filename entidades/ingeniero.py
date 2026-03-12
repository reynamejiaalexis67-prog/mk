from entidades.empleado import Empleado

class Ingeniero(Empleado):
    
    def __init__(self, nombre:str,
                 dias_trabajados:int,
                 horas_trabajadas:float,
                 descuento:float,
                 bono_salida:float,
                 bono_inteligencia:float):
        
        
        super().__init__(nombre, dias_trabajados, horas_trabajadas, descuento)
        
        self.bono_salida=bono_salida
        self.bono_inteligencia=bono_inteligencia
        
        
        
    def calcular_salario_ingeniero(self):
        costo_base = self.calcular_salario_base()
        total = self.calcular_salario_ingeniero + self.bono_salida + self.bono_inteligencia
        return total 