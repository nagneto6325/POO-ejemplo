# === Gestión de Vehículos con Programación Orientada a Objetos ===

# Clase base Vehiculo
class Vehiculo:
    def __init__(self, marca: str, modelo: str, año: int):
        self.marca = marca
        self.modelo = modelo
        self.año = año
    
    def mostrar_info(self):
        return f"{self.año} {self.marca} {self.modelo}"
    
    def encender(self):
        return f"El vehículo {self.marca} {self.modelo} está encendido."


# Clase derivada Coche
class Coche(Vehiculo):
    def __init__(self, marca: str, modelo: str, año: int, puertas: int):
        super().__init__(marca, modelo, año)
        self.puertas = puertas
    
    def mostrar_info(self):
        return f"{super().mostrar_info()} - {self.puertas} puertas"
    
    def tocar_claxon(self):
        return "¡Pii Pii! 🚗"


# Clase derivada Moto
class Moto(Vehiculo):
    def __init__(self, marca: str, modelo: str, año: int, tipo: str):
        super().__init__(marca, modelo, año)
        self.tipo = tipo
    
    def mostrar_info(self):
        return f"{super().mostrar_info()} - Tipo: {self.tipo}"
    
    def hacer_caballito(self):
        return "🏍️ La moto está haciendo un caballito!"


# Programa principal
if __name__ == "__main__":
    print("=== Registro de Vehículos ===")
    opcion = input("¿Quieres registrar un coche o una moto? (coche/moto): ").strip().lower()

    marca = input("Marca: ")
    modelo = input("Modelo: ")
    año = int(input("Año: "))

    if opcion == "coche":
        puertas = int(input("Número de puertas: "))
        vehiculo = Coche(marca, modelo, año, puertas)
    elif opcion == "moto":
        tipo = input("Tipo de moto (deportiva, scooter, etc.): ")
        vehiculo = Moto(marca, modelo, año, tipo)
    else:
        print("Opción no válida.")
        exit()

    print("\n=== Información del vehículo ===")
    print(vehiculo.mostrar_info())
    print(vehiculo.encender())

    if isinstance(vehiculo, Coche):
        print(vehiculo.tocar_claxon())
    elif isinstance(vehiculo, Moto):
        print(vehiculo.hacer_caballito())
