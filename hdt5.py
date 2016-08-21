
#-----------------------------------#
#           Laboratorio 5           #
#                                   #
# @utores: Gerardo Molina, 14492    #
#          Rodolfo Cacacho          #
# Fecha: 22/09/16                   #
#-----------------------------------#

import random
import simpy


SEMILLA = 50
MEMORIA_RAM = simpy.Container(env, init=0, capacity=100)
MEMORIA_MIN = 1
MEMORIA_MAX = 10
NUMERO_INSTRUCCIONES = 3
NUMERO_PROCESOS=25
INTERVAL_CUSTOMERS=10

def proceso(env,cantidad_memoria,tiempo_proceso,num_inst):

    ## ---- new ---- ##
    inicio_proceso = env.now
    yield env.timeout(tiempo_proceso)
    yield MEMORIA_RAM.get(cantidad_memoria)
    print('Se admitio el proceso')
    print('con un tiempo de:%f'% env.now)
    print('con una cantidad de memoria de:%f'% cantidad_memoria)

    ## ---- ready ----##
    for i in range(num_inst):
        CPU.request() as req:
            yield req
            if (cantidad_instrucciones-instrucciones_completas)>=limite:
                realizar=limite
            else:
                realizar=cantidad_instrucciones-instrucciones_completas
            env.timeou(realizar/limite)
            instrucciones_completas=instrucciones_completas+realizar
            print('Esta listo(ready)')
            print('Instrucciones completadas:%f'%instrucciones_completas)
            print('Tiempo:%f'%env.now)
            

    tiempo_total = env.now - inicio_proceso
    print "Tiempo del proceso:%f"% tiempo_total



# Se inicia la simulacion

random.seed(SEMILLA)
env = simpy.Environment()
inst=simpy.Resource(env,capacity=3)

# Se inicia el proceso y se corre
counter = simpy.Resource(env, capacity=1)
ourGen=generador(NUMERO_PROCESOS)
#env.process(proceso(env))
#env.run()

