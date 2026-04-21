class Personaje:
    def __init__(self, nombre, vida, ataque, tipo_personaje, rol):
        self.__nombre = nombre
        self.__vida = vida
        self.__ataque = ataque
        self.__tipo_personaje = tipo_personaje
        self.__rol = rol
    
    def info_personaje(self):
        print (f"Nombre:{self.__nombre} ")
        print (f"Vida:{self.__vida} ")
        print (f"Ataque:{self.__ataque} ")
        print (f"Tipo de personaje:{self.__tipo_personaje} ")
        print (f"rol:{self.__rol} ")

    def personaje_vivo(self):
        return self.__vida > 0
    
    def curar_pj(self, cantidad):
        self.__vida += cantidad
        print(f"Vida actual: {self.__vida}")
    
    def get_personaje_vida(self):
        return self.__vida
    
    def set_personaje_vida(self, nuevodato):
        self.__vida = nuevodato

    def get_curar_pj(self):
        return self.__vida
    
    def set_curar_pj(self, nuevodato_curar):
        self.__vida = nuevodato_curar


pj1 = Personaje("Juan el mago", 100, 100, "Magia", "Mago")
pj1.info_personaje()
print(pj1.personaje_vivo())

pj1.set_personaje_vida(40)
print(pj1.get_personaje_vida())
