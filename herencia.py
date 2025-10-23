#Autor: Sebastian Triana

#Caso de uso: Ejercicio herencia y polimorfismo

class Animal:
    def __init__(self, especie, edad, nombre):
        self.especie = especie
        self.edad = edad
        self.nombre = nombre

    def hablar(self):
        pass
    
    def moverse(self):
        pass

    def describir(self):
        print("Soy un animal del tipo" , type(self).__name__)

class raton(Animal):
    def __init__(self, especie, edad, nombre):
        super().__init__(especie, edad, nombre)

    def hablar(self):
        print("aha, aha yo soy mickey mouse")

    def moverse(self):
        print("caminando en dos patas...")

class panda(Animal):
    def __init__(self, especie, edad, nombre, guerrero_dragon):
        super().__init__(especie, edad, nombre)
        self.guerrero_dragon = guerrero_dragon

    def hablar(self):
        print("me gustan los donplings")

    def moverse(self):
        print("rueda bajo la colina a gran velocidad")

    def guerrero(self):
        if self.guerrero_dragon == True:
            print(f"Yo soy {self.nombre}, un {self.especie} y soy el Guerrero Dragón!!")
        else:
            print(f"Yo soy {self.nombre}, un {self.especie} y no soy el Guerrero Dragón :(")
    
def menu():
    opcion = input("**Elija el ejemplo que desee** \n-Presione (1) para ejemplo con raton \n-Presione (2) para ejemplo con panda \n Opcion: ")
    if opcion == "1":
        print("\nEjemplo de herencia con Raton:\n")
        r = raton("ratón", 99, "mickey")
        r.describir()
        r.hablar()
        r.moverse()
    else:
        print("\nEjemplo de herencia con panda:\n")
        p = panda("panda", 18, "po", True)
        p.describir()
        p.guerrero()

def main():
    menu()
    
if __name__ == "__main__":
    main()
