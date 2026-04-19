class Personaje:
    def __init__(self, nombre, vida, ataque, tipo_personaje, rol):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.tipo_personaje = tipo_personaje
        self.rol = rol
    
    def info_personaje(self):
        print (f"Nombre:{self.nombre} ")
        print (f"Vida:{self.vida} ")
        print (f"Ataque:{self.ataque} ")
        print (f"Tipo de personaje:{self.tipo_personaje} ")
        print (f"rol:{self.rol} ")