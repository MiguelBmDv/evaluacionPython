# CREACION DE DOS ESTRUCTURAS DE DATOS, UNA CON LOS CANDIDATOS, Y OTRA VACIA CON EL REGISTRO DE LOS VOTOS
candidatoList = {1:"Miguel",2:"Laura",3:"Cristian"}
regVotantes = []

#CREACION MAIN DE LA CLASE VOTANTES CON UN METODO CONSTRUCTOR
class Votantes:
    def __init__(self, idV, nombre, apellido):
       self.idV = idV
       self.nombre = nombre
       self.apellido = apellido 
#CREACION DE LA SUBCLASE VOTO, QUE HEREDA EL METODO CONSTRUCTOR DE VOTANTES Y AÑADE OTROS ATRIBUTOS
class Voto(Votantes):
    def __init__(self,idCandidato, nombreCandidato, idV, nombre, apellido):
       super().__init__(idV, nombre, apellido)
       self.idCandidato = idCandidato
       self.nombrecandidato = nombreCandidato
#CREACION DE METODO DE CLASE REGISTRO, QUE AYUDARA A REGISTRAR CADA VOTO Y VALIDAR QUE NO SE REPITAN
    @classmethod
    def registro(cls):
        while True:
            print("\nBienvenido al registro de votantes")
            idV = int(input("Ingrese su identificacion: "))
            for votante in regVotantes: 
                if votante.idV == idV:
                    print("Su voto ya se registro")
                    break
            else:
                nombre = input("Ingrese su primer nombre: ")
                apellido = input("Ingrese su primer apellido: ")
                idCandidato = int(input("Ingrese el numero del candidato a votar (0:Voto en blanco 1:Miguel, 2:Laura, 3:Cristian): "))
                if idCandidato == 1:
                    nombreCandidato = "Miguel"
                elif idCandidato == 2:
                    nombreCandidato = "Laura"
                elif idCandidato == 3:
                    nombreCandidato = "Cristian"
                elif idCandidato == 0:
                    nombreCandidato = "Voto en blanco"
                return cls(idCandidato, nombreCandidato,idV, nombre, apellido)  
#CREACION DE METODO DE CLASE AVANCE QUE MOSTRARA LOS RESULTADOS EN TIEMPO REAL DE LAS VOTACIONES SIN TERMINAR LA JORNADA
    @classmethod
    def avance(cls):
        print("Avances electorales: ")
        cont=0
        for votante in regVotantes: 
            can1=1
            if votante.idCandidato == can1:
                cont+=1
        cont2=0
        for votante in regVotantes: 
            can2=2
            if votante.idCandidato == can2:
                cont2+=1
        cont3=0
        for votante in regVotantes: 
            can3=3
            if votante.idCandidato == can3:
                cont3+=1
        cont4=0
        for votante in regVotantes: 
            votoBlanco=0
            if votante.idCandidato == votoBlanco:
                cont4+=1
        print(f"Candidato Miguel: {cont} \nCandidata Laura: {cont2}\nCandidato Cristian: {cont3} \nVoto en blanco: {cont4}")
#CREACION DE METODO DE CLASE RESULTADO QUE FINALIZA LA JORNADA ELECTORAL Y MUESTRA EL GANADOR O EN QUE TERMINO EL RESULTADO
    @classmethod
    def resultado(cls):
        print("Resultados electorales: ")
        cont1=0
        for votante in regVotantes: 
            can1=1
            if votante.idCandidato == can1:
                cont1+=1
        cont2=0
        for votante in regVotantes: 
            can2=2
            if votante.idCandidato == can2:
                cont2+=1
        cont3=0
        for votante in regVotantes: 
            can3=3
            if votante.idCandidato == can3:
                cont3+=1
        cont4=0
        for votante in regVotantes: 
            votoBlanco=0
            if votante.idCandidato == votoBlanco:
                cont4+=1
        totalVotos= cont1+cont2+cont3+cont4
        if cont1 == cont2 and cont1 == cont3:
            print(f"Ocurrio un empate de votos entre todos los candidatos, cada uno con un total de {cont1} votos")
        elif cont1 > cont2 and cont1 > cont3:
            print(f"El Ganador es: \nEl candidato Miguel con {cont1} votos de un total de {totalVotos} votos")
        elif cont2 > cont1 and cont2 > cont3:
            print(f"El Ganador es: \nLa candidata Laura con {cont2} votos de un total de {totalVotos} votos")
        elif cont3 > cont1 and cont3 > cont2:
            print(f"El Ganador es: \nEl candidato Cristian con {cont3} votos de un total de {totalVotos} votos")
        elif cont1 == cont2 :
            print(f"Ocurrio un empate de votos entre Miguel y Laura, cada uno con un total de {cont1} votos")
        elif cont2 == cont3 :
            print(f"Ocurrio un empate de votos entre Cristian y Laura, cada uno con un total de {cont2} votos")
        elif cont1 == cont3 :
            print(f"Ocurrio un empate de votos entre Cristian y Miguel, cada uno con un total de {cont3} votos")

#FUNCION QUE TRAE EL MENU PARA PODER VISUALIZAR LAS OPCIONES Y LLAMAR METODOS DE CLASE
def menu():
     while True:
        print("\nBienvenido jurado al menu principal digite: \n0. Mostrar candidatos \n1. para registrar un voto \n2. para mostrar avances de la votacion \n3. Terminar jornada de votacion")
        opc = int(input("Digite una opcion para continuar: "))
        
        if opc == 0:
            print ("Los candidatos son:\n")
            for i,j in candidatoList.items():
                print(i,j)
        if opc == 1:
            votanteRegistro = Voto.registro()
            regVotantes.append(votanteRegistro)
        if opc == 2:
            Voto.avance()
        if opc == 3:
            Voto.resultado()
            break
        
#PROGRAMA PRINCIPAL 
menu()
             