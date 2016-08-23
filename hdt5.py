#-----------------------------------#
#           Laboratorio 5           #
#                                   #
# @utores: Gerardo Molina, 14492    #
#          Rodolfo Cacacho,15223    #
# Fecha: 22/09/16                   #
#-----------------------------------#

import random
import simpy

global tiempoT
tiempoT = []
Random_Seed = 111               # Seed to generate random
random.seed(Random_Seed)
Ram_Size = 100                # Size of ram
CPU_Speed = 1                 # Tiempo que atiende proceso
InstCPU = 6       # Cantidad de instrucciones que puede hacer el cpu por unidad de tiempo
Intervalo = 5       # Valor de intervalo paa random expovariate
Procesos = 25        # Cantidad de procesos a realizar

def genProcess(env, cant_Procesos, intervalo_Gen, instdCPU):
   global instruct
   for i in range(Procesos):
      var = random.expovariate(1.0/intervalo_Gen)
      cantM = random.randint(1, 10)
      cantI = random.randint(1, 10)
      env.process(setMem(env,i+1,cantM))
      global arribo
      arribo = env.now
      print ('El proceso %s entro al sistema' % (i+1))
      env.process(doProcess(i+1, env, cantM, cantI, instdCPU))
      yield env.timeout(var)
                
def setMem(env, nombre, memoria):
        global totalProcesos
        print ('El proceso %s recibe memoria' % nombre)
        with RamCola.request() as req:
                if Ram.level <= 0:
                    yield req
        yield Ram.get(memoria) #ready con memoria asignada
      
def doProcess(nombre, env, memoria, instruct, instdCPU):
        global TiempoTotal
        #Valores[1:cantprocesos]
        #ready
        if instruct > 0:
                with CPU.request() as req:
                        yield req
                        if instruct > 0:
                                while instruct > 0:
                                        if instruct > instdCPU:
                                                instruct = instruct - instdCPU
                                                wait = random.randint(1,2)
                                                if wait == 1:
                                                        print ('El proceso %s se encuentra reaizando operaciones de I/O' % nombre)
                                                        yield env.timeout(1)
                                                        env.process(doProcess(nombre, env, memoria, instruct, instdCPU))
                                                if wait == 2:
                                                        print ('El proceso %s se se mueve a estado Ready' % nombre)
                                                        env.process(doProcess(nombre, env, memoria, instruct, instdCPU))                  
                                        else:
                                                TiempoTotal = env.now - arribo #Tiempo que se tarda el proceso en el sistema
                                                tiempoT.append(TiempoTotal)
                                                print ('Estado terminated: proceso %s\nEste tardo %s en ejecutarse\n' % (nombre, TiempoTotal))
                                                intruct = 0
                                                yield env.timeout(1)
                                                yield Ram.put(memoria)

env = simpy.Environment()
Ram = simpy.Container(env, init = Ram_Size, capacity = Ram_Size)
RamCola = simpy.Resource(env,capacity = 1)
CPU = simpy.Resource(env,capacity = 5)

# Setup and start the simulation
print('Simulacion Procesos en CPU')

# Start processes and run
genProcesos = env.process(genProcess(env, Procesos, Intervalo, InstCPU)) #generan procesos
env.run()

#Variables para el calculo de la desviacion estandar
suma = 0
desvesta = 0
sumaRAC = []

for a in range (Procesos):
   suma = tiempoT[a] + suma

prom = suma / Procesos
sumaTR = 0

print ('\nTiempo Total: %s' % (suma))
print ('\nTiempo promedio por proceso es de: %s' % (prom))

for x in range (Procesos):
        resta = tiempoT[x] - prom
        restaAC = resta*resta
        sumaRAC.append(restaAC)
        sumaTR = sumaTR + sumaRAC[x]
   
desvesta = (sumaTR/Procesos)**0.5
print ('Devesviacion estandar = %s' % (desvesta))

