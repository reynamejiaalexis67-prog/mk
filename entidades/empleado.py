class Empleado:
    
    def __init__(self,nombre:str,
                 dias_trabajados:int,
                 horas_trabajadas:float,
                 descuento:float):
        
        
     self.nombre=nombre       
     self.dias_trabajados=dias_trabajados        
     self.horas_trabajadas=horas_trabajadas        
     self.descuento=descuento  
     
     
     
     
    def calcular_salario_base(self):
        costo = (self.horas_trabajadas * 80) + (self.dias_trabajados* 6) -(self.descuento)
        return costo       