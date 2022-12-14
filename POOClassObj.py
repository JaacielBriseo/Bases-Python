class Auto:
    
    def __init__(self, marca, color, cantidad_ruedas,velocidad_max):
        self.marca = marca
        self.color = color
        self.cantidad_ruedas = cantidad_ruedas
        self.velocidad_max = velocidad_max
        self.motor = 2.0
        
    def __str__(self):
        return f"{self.motor}.{self.marca},{self.color},{self.cantidad_ruedas},{self.velocidad_max}"
    
    def acelerar(self):
        print(f"El auto ha acelerado hasta {self.velocidad_max} kms")
    
    def frenar(self):
        print('El auto ha frenado')

        

aventador = Auto("Lamborghini", 'blanco',4,320)
huracan = Auto("Lamborghini", 'rojo',4,300)

print(aventador)
print(aventador.color)
print(huracan)
print(huracan.color)

aventador.acelerar()
aventador.frenar()
aventador.acelerar()

aventador.color = 'Amarillo'
print(aventador)