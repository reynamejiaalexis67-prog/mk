class Empleado:  

    def __init__(self, nombre:str,  # nombre del parametro / parametro
                 dias_trabajados:int, 
                 horas_trabajadas:float,  
                 descuento:float):  
                 
        # metodo constructor (__init__)

        self.nombre = nombre  # atributo del objeto 
        self.dias_trabajados = dias_trabajados  
        self.horas_trabajadas = horas_trabajadas 
        self.descuento = descuento  


    def calcular_salario_base(self):  # nombre del metodo
        costo = (self.horas_trabajadas * 8) + (self.dias_trabajados * 200) - (self.descuento)
        return costo  # valor de retorno