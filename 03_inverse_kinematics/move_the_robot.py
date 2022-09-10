import time
from inverse_kinematics import *

from client import RobotClient
from inverse_kinematics import position_to_dof


## Conectarse al robot

r = RobotClient(address="192.168.0.14")  # Recuerda usar una dirección válida
r.connect()
r.home()    # Revisa el archivo client.py para que veas qué hace esta función


## Función para mover el robot usando cartesianas
def move_robot_to_xyz(robot: object, x: object, y: object, z: object) -> object:
    q0, q1, q2 = position_to_dof(x, y, z)
    robot.set_joints(q0, q1, q2)

## Para poder crear figuras, es necesario diseñar funciones tales que realicen acciones iterables, para esto
## es posible usar el ciclo for y listas para encerrar los movimientos que ha de efectuar el robot.
## No obstante, pueden haber muchas formas más y la verdad no estoy seguro si el código que hice es factible o
## siquiera bien planteado.

## Funcion dibuja_una_linea() permite mover el robot entre dos puntos arbitrarios desde (a,b)
## hacia (c,d). Se requiere fijar una altura (z) que será constante.
def dibuja_una_linea(a,b,c,d,z):
    Cx = [a,c]
    Cy = [b,d]
    for coordenadax, coordenaday in zip(Cx,Cy):
        move_robot_to_xyz(r,x=coordenadax,y=coordenaday,z=z)
    return None

## Funcion dibuja_cuadrado() permite en teoría dibujar un cuadrado de largo L, eligiendo como vertice
## inferior un punto (x,y) arbitrario. Notar que el valor elegido para z se mantiene constante para
## el movimiento del brazo.
def dibuja_cuadrado(L,x,y,z):
    CCx = [x,x,x+L,x+L,x]
    CCy = [y,y+L,y+L,y,y]
    for cx, cy in zip(CCx, CCy):
        move_robot_to_xyz(r, x=CCx, y=CCy, z=z)
    return None

##z, y, x
move_robot_to_xyz(r,20,0,80)
time.sleep(2)
move_robot_to_xyz(r,20,30,80)
time.sleep(2)
move_robot_to_xyz(r,20,10,80)
time.sleep(2)
move_robot_to_xyz(r,20,80,80)

## Mover el robot (acá va tu código)
#move_robot_to_xyz(r, x=20, y=100, z=200)
## posicion de descanso (185,0,241)



