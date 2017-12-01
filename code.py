import time
import os
import random

global velocidad # 10 Generaciones por segundo
#Imprimir mundo con celulas vivas y muertas por defecto
def imprimirMundo(mundo, gen='X', vivo='⛆ ', muerto='  '):
    n = len(mundo) # Capturar numero de filas
    m = len(mundo[0]) # Capturar numero de columnas
    os.system('clear') # Limpiar la pantalla
    contador = 0 # Contador de celulas vivas
    for i in range(n):
        for j in range(m):
            print(vivo if mundo[i][j]==1 else muerto ,end='')
            contador += mundo[i][j]
        print("")
    print("\n\tPoblacion:",contador)
    print("\n\tGeneracion:",gen)
    global velocidad
    time.sleep(velocidad)
def siguienteGen(mundo):
    n = len(mundo)
    m = len(mundo[0])
    sigMundo = [ [0 for i in range(m)] for j in range(n)] # Inicializamos
    for i in range(n):
        for j in range(m):
            cont = 0 # Contador de vecinos
            cont += mundo[(i-1+n)%n][(j-1+m)%m] #1
            cont += mundo[(i-1+n)%n][j]         #2
            cont += mundo[(i-1+n)%n][(j+1)%m]   #3
            cont += mundo[i][(j-1+m)%m]         #4
            cont += mundo[i][(j+1)%m]           #5
            cont += mundo[(i+1)%n][(j-1+m)%m]   #6
            cont += mundo[(i+1)%n][j]           #7
            cont += mundo[(i+1)%n][(j+1)%m]     #8
            if mundo[i][j] == 1: # Si está viva
                if cont == 2 or cont == 3:
                    sigMundo[i][j] = 1 # La célula se mantiene viva
                else:
                    sigMundo[i][j] = 0 # La célula muere por soledad
            else: #Si está muerta
                if cont == 3: # Si una celula muerta tiene 3 celulas vivas vecinas, vivirá
                    sigMundo[i][j] = 1
                else: # Sino seguirá muerta
                    sigMundo[i][j] = 0
    return sigMundo
def genMundoRandom(n, m):
    mundo = [[0 for x in range (m)] for y in range(n)]
    for i in range(n):
        for j in range(m):
            mundo[i][j] = random.randint(0,1)
    return mundo

def ExportarSimulacion(mundo):
    nombreArchivo = input("Ingrese el nombre de su archivo (acabará en un .txt):")
    F = open(nombreArchivo+".txt","w")
    n = len(mundo)
    m = len(mundo[0])
    for i in range(n):
        row = ""
        for j in range(m):
            row +=str(mundo[i][j])
        F.write(row+"\n")

#A partir de aqui se usan las funciones basicas anteriores
def SimularNGen():
    N = int(input("\tIngrese cantidad de generaciones:"))
    n = int(input("\tIngrese la cantidad de filas:"))
    m = int(input("\tIngrese la cantidad de columnas:"))
    mundo = genMundoRandom(n,m)
    for gen in range(N):
        imprimirMundo(mundo,gen+1)
        mundo = siguienteGen(mundo)
    respuesta = input("\t\tDesea importar el resultado? Si=S , No= cualquier entrada :")
    if respuesta =='S':
        ExportarSimulacion(mundo)
def SimularInf():
    gen = 1
    n = int(input("\tIngrese la cantidad de filas:"))
    m = int(input("\tIngrese la cantidad de columnas:"))
    mundo = genMundoRandom(n, m)
    while(1):
        imprimirMundo(mundo, gen)
        mundo = siguienteGen(mundo)
        gen += 1

def CambiarVelocidad():
    global velocidad
    velocidadAct = int(input("\t\tIngrese la nueva velocidad en iteraciones por segundo rango(1,50):"))
    velocidad = 1/max(1,min(50,velocidadAct)) # Limita el rango entre 1 y 50
    print("\t\tLa frecuencia ahora es:",velocidad)
    time.sleep(1)

def ImportarMundo():
    os.system("clear")
    print("\n\n\tEl formato del archivo debe ser: ")
    print("\t# 'n' lineas de 'm' caracteres { 0, 1 } cada una :)")
    nombreArchivo = input("\t\tIngrese el nombre del archivo: ")
    F = open(nombreArchivo,"r")
    contenido = F.read().split("\n")
    mundo = []
    for row in contenido:
        rowMundo = []
        for cel in row:
            rowMundo.append(1 if cel=='1' else 0)
        if len(rowMundo):
            mundo.append(rowMundo)
    imprimirMundo(mundo)
    F.close()
    time.sleep(8)


def menu():
    global velocidad
    velocidad = 1/5
    while True:
        os.system("clear") #os.system('cls')
        print("\n\n\t1.- Simular random en pantalla N generaciones")
        print("\t2.- Simular random en pantalla indefinidamente")
        print("\t3.- Cambiar velocidad de simulacion")
        print("\t4.- Importar Mundo desde archivo y simular")
        print("\t0.- Safari ;)")
        print("\n\tNota: la frecuencia es 5 generaciones por segundo.")
        opcion = input("\n\t\tIngrese una opción:")
        # Simulando el switch con diccionario
        mapa = {
          '1': SimularNGen,
          '2': SimularInf,
          '3': CambiarVelocidad,
          '4': ImportarMundo,
          '0': '' #salir
        }
        if not opcion in mapa:
            print("\n\n\t\tIngrese una opcion correcta")
            time.sleep(1)
        elif opcion=='0':
            exit()
        else:
            mapa[opcion]()

menu() #Inicializar el programa
