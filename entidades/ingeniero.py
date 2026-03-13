from entidades.empleado import Empleado  # importacion de clase

class Ingeniero(Empleado):  # Clase / herencia de Empleado
    
    def __init__(self, nombre:str,  # nombre del parametro 
                 dias_trabajados:int,  
                 horas_trabajadas:float, 
                 descuento:float, 
                 bono_salida:float,  
                 bono_inteligencia:float):  
        
        # metodo constructor
        
        super().__init__(nombre, dias_trabajados, horas_trabajadas, descuento)  
        # llamada al constructor de la clase padre / argumentos del constructor
        
        self.bono_salida = bono_salida  # atributo del objeto
        self.bono_inteligencia = bono_inteligencia 
        
        
    def calcular_salario(self):  # nombre del metodo 
        costo_base = self.calcular_salario_base()  # llamada a metodo
        total = costo_base + self.bono_salida + self.bono_inteligencia
        return total  # valor de retorno