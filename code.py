import time
import os
import random
speed = 1/10 # 10 Generaciones por segundo
def imprimirMundo(mundo, vivo='⛆ ', muerto='  '):
    n = len(mundo)
    m = len(mundo[0])
    contador = 0
    for i in range(n):
        for j in range(m):
            print(vivo if mundo[i][j]==1) else muerto ,end='')
            contador += mundo[i][j]
          print("")
    print("\n\tPoblacion:",contador)
    time.sleep(speed)
    os.system('clear')
def siguienteGen(mundo):
    n = len(mundo)
    m = len(mundo[0])
    sigMundo = [ [0 for i in range(n)] for j in range(m)] # Inicializamos
    for i in range(n):
        for j in range(m):
            cont = 0 # Contador de vecinos
            cont += mundo[(i-1+n)%n][(j-1+m)%m]
            cont += mundo[(i-1+n)%n][j]
            cont += mundo[(i-1+n)%n][(j+1)%m]
            cont += mundo[i][(j-1+m)%m]
            cont += mundo[i][(j+1)%m]
            cont += mundo[(i+1)%n][(j-1+m)%m]
            cont += mundo[(i+1)%n][j]
            cont += mundo[(i+1)%n][(j+1)%m]
        if mundo[i][j] == 1: # Si está viva
            if cont != 2 && cont != 3: # La célula muere por soledad
                sigMundo[i][j] = 0
            else:
                sigMundo[i][j] = 1 # La célula se mantiene viva
        else: #Si está muerta
            if cont == 3 # Si una celula muerta tiene 3 celulas vivas vecinas, vivirá
                sigMundo[i][j] = 1
            else: # Sino seguirá muerta
                sigMundo[i][j] = 0
    return sigMundo
def SimularNGen():
    N = int(input("Ingrese cantidad de generaciones:"))

def menu():
    while(1):
        os.system("clear")
        print("\t1.- Simular random en pantalla N generaciones")
        print("\t2.- Simular random en pantalla indefinidamente")
        print("\t3.- Exportar una simulacion random a un archivo")
        print("\t4.- Cambiar velocidad de simulacion")
        print("\t5.- Safari ;)")
        print("\n\tNota: la velocidad es 10 generaciones por segundo.")
        opcion = int(input("\n\t\tIngrese una opción:"))
        # Simulando el switch con mapas
        mapa = {
          1: SimularNGen(),
          2: SimularInf(),
          3: ExportarRandom(),
          4: CambiarVelocidad(),
          5: exit()
        }
        if not opcion in mapa:
            print("Ingrese una opcion correcta")
        else:
            mapa[opcion]

menu() #Inicializar el programa
