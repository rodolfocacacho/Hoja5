#-----------------------------------#
#           Laboratorio 5           #
#                                   #
# @utores: Gerardo Molina, 14492    #
#          Rodolfo Cacacho 15223    #
# Fecha: 22/09/16                   #
#-----------------------------------#

import random
import simpy


SEMILLA = 50
MEMORIA_RAM = 100
MEMORIA_MIN = 1
MEMORIA_MAX = 10
NUMERO_INSTRUCCIONES = 3
NUMERO_PROCESOS=25
INTERVAL_CUSTOMERS=10


def memoria(self,env):
    self.memoria = simpy.Container(env, init=0, capacity=100)
    

def proceso(env):

    inicio_proceso = env.now
 
        
    tiempo_total = env.now - inicio_proceso

    print "Tiempo del proceso:%f"% tiempo_total



# Se inicia la simulacion

random.seed(SEMILLA)
env = simpy.Environment()
inst=simpy.Resource(env,capacity=3)

# Se inicia el proceso y se corre
counter = simpy.Resource(env, capacity=1)
env.process(source(env, NUMERO_PROCESOS, INTERVAL_CUSTOMERS, counter))
env.run()

