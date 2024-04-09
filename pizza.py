# Info
# Autor: Juan Cataldo [jcataldoaguilera@gmail.com]
# Fecha: 2024-04-05
# RLAB-23-02-09-0044-2
#

# Librerias
from ingredientes import carnes, vegetales, masas

# Desarrollo
class Pizza():
    size = 'familiar'
    price = 10000
    
    @staticmethod
    def validate(elemento, valores):
        return elemento in valores
    
    def pedido(self):
        self.carne = input(
            """ Ingrese el ingrediente protéico:
            Pollo, Vacuno, Carne Vegetal
            ->"""
        ).lower()
        c1 = self.validate(self.carne, carnes)
        self.vegetales = []
        
        self.vegetales.append(input(
            """ Ingrese el primer ingrediente vegetal:
            Tomate, Champiñon, Aceituna
            ->"""
        ).lower())
        v1 = self.validate(self.vegetales[0], vegetales)
        
        self.vegetales.append(input(
            """ Ingrese el segundo ingrediente vegetal:
            Tomate, Champiñon, Aceituna
            ->"""
        ).lower())
        v2 = self.validate(self.vegetales[1], vegetales)
                
        self.masa = input(
            """ Ingrese el tipo de masa:
            Tradicional o Delgada
            ->"""
        ).lower()
        m1 = self.validate(self.masa, masas)
        
        self.pizza_valida = c1 and v1 and v2 and self.validate(self.masa, masas)
        
if __name__ == '__main__':
    pizza1 = Pizza()
    pizza1.pedido()
    if pizza1.pizza_valida:
        print("La Pizza es valida")
    else:
        print("La Pizza no es valida")