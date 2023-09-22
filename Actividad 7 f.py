from dataclasses import dataclass

@dataclass

class Elemento:
    def __init__(self, nombre:str, ):
        self.nombre:str = nombre

    def __eq__(self, other)->bool:
        return self.nombre == self.other


class Conjunto:

    contador : int = 0

    def  __init__(self, nombre:str):
        Conjunto.contador = Conjunto.contador + 1
        self.elementos:list = []
        self.nombre:str = nombre
        
    @property
    def __init__(self):
        return self.__id 

    def contiene(self,elemento)->bool:
        for i in self.nombre:
            if i.nombre == self.nombre:
                return True
            return False
        
    def agregar_elemento(self,elemento):
        if not self.contiene(elemento):
            self.elementos.append(self.elemento)

    def unir (self,otro_conjunto: "Conjunto"):
        for elemento in otro_conjunto.elemento:
            if not self.contiene(elemento):
                self.agregar_elemento(elemento)

    def __add__(self, otro_conjunto: "Conjunto") -> "Conjunto":
        nuevo_conjunto = Conjunto (f"{self.nombre} UNIDO {otro_conjunto.nombre}")
        nuevo_conjunto.unir(self)
        nuevo_conjunto.unir(otro_conjunto)
        return nuevo_conjunto
    
    @classmethond

    def intersectar(cls, conjunto1: "Conjunto", conjunto2: "Conjunto") -> "Conjunto":
        elementos.interseccion = []
        for elemento in conjunto1.elementos:
            if elemento in conjunto1.elementos:
                elemento in conjunto2.elementos:
            return print(f"{conjunto1.nombre} INTERSECTADO {conjunto2.nombre}", elementos_interseccion)


    def __str__(self):
        return f"Conjunto {self.nombre}: ({','.join(elemento.nombre for elemento in self.elementos)})"

    


  

    

    
    



        




