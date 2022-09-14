import string

class Nodo():
    
    def __init__(self, dato = None, siguiente = None):
        self.dato = dato
        self.siguiente = siguiente

class Lista_simple(): 
    def __init__(self):
        self.cabeza = None
    
    # Método para agregar elementos en el frente de la linked list
    def agregar_al_inicio(self, dato):
        self.cabeza = Nodo(dato=dato, siguiente=self.cabeza)  

    # Método para verificar si la estructura de datos esta vacia
    def vacio(self):
        return self.cabeza == None

    # Método para agregar elementos al final de la linked list
    def agregar_al_final(self, dato):
        if not self.cabeza:
            self.cabeza = Nodo(dato=dato)
            return
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = Nodo(dato=dato)
    
    # Método para eleminar nodos
    def borrar_nodo(self, key):
        actual = self.cabeza
        temporal = None
        while actual and actual.dato != key:
            temporal = actual
            actual = actual.siguiente
        if temporal is None:
            self.cabeza = actual.siguiente
        elif actual:
            temporal.siguiente = actual.siguiente
            actual.siguiente = None

    # Método para obtener el ultimo nodo
    def obtener_ultimo_nodo(self):
        temp = self.cabeza
        while(temp.siguiente is not None):
            temp = temp.siguiente
        return temp.dato

    # Método para imprimir la lista de nodos
    def imprimir_lista(self,llave):
        nodo = self.cabeza
        while nodo != None:
            print( getattr(nodo.dato, llave)  ," => ")
            nodo = nodo.siguiente

class Paciente():
    
    nombre:string 
    edad:int
    sexo:string
    muestra:Lista_simple

    def __init__(self,nombre, edad,sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.muestra = Lista_simple()

class Doctor():
    
    nombre:string 
    edad:int
    sexo:string
    muestra:Lista_simple
    colgegiado:string

    def __init__(self,nombre, edad,sexo,colgegiado):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.colgegiado = colgegiado



class Celula():
    x:int
    y:int
    enferma:bool
    def __init__(self,x,y,enferma):
        self.x=x
        self.y=y
        self.enferma=enferma

if __name__ == "__main__":
    print("Iniciando archivo")
    #Cargo mi archivo
    #Creo lista pacientes
    ListaPacientes=Lista_simple()
    #Itero mi archivo
    #Creo paciente
    paciente1=Paciente('Auron',36,'Masculino')
    #Itero Muestra

    paciente1.muestra.agregar_al_inicio( Celula(0,0,True)  )
    paciente1.muestra.agregar_al_inicio( Celula(0,1,True)  )
    paciente1.muestra.agregar_al_inicio( Celula(0,2,False) )
    paciente1.muestra.agregar_al_inicio( Celula(0,3,True)  )
    paciente1.muestra.agregar_al_inicio( Celula(0,4,True)  )
    paciente1.muestra.agregar_al_inicio( Celula(0,5,False) )
    #Guardo paciente en la lista
    ListaPacientes.agregar_al_inicio(paciente1)
    ListaPacientes.agregar_al_inicio(Paciente('Dobals',31,'Masculino'))
    print('\n')
    ListaPacientes.imprimir_lista('edad')
    paciente1.muestra.imprimir_lista('enferma')
    print('Impresion:')
    