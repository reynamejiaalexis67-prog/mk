from entidades.empleado import Empleado


class Marketing(Empleado):
    
    def __init__(self, nombre:str,
                 dias_trabajados:int,
                 horas_trabajadas:float,
                 descuento:float,
                 bono_venta:float,
                 bono_satifaccion:float):
        
        super().__init__(nombre, dias_trabajados, horas_trabajadas, descuento)
        
        self.bono_venta=bono_venta
        self.bono_satifaccion=bono_satifaccion
        
        
    def calcular_salario_marketing(self):
        costo_base = self.calcular_salario_base()
        total = self.calcular_salario_ingeniero + self.bono_venta + self.bono_satifaccion
        return total 