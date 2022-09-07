import time
from client import RobotClient


## Conectarse al robot

robot = RobotClient(address="192.168.0.15")  # Recuerda usar una dirección válida
robot.connect()

## Mover el robot (acá va tu código)

HOME_Q0 = 0
HOME_Q1 = 0
HOME_Q2 = 90

arreglo = [-30 10 30 60 90]
time.sleep(2)


robot.set_joints(q0=-30, q1=130, q2=135)
robot.set_joints(q0=0, q1=130, q2=135)
robot.set_joints(q0=30, q1=130, q2=135)
def look_right():
    robot.set_joints(q0=30, q1=60, q2=10)

def look_left():
    robot.set_joints(q0=30, q1=40, q2=10)

def look_up():
    robot.set_joints(q0=0, q1=40, q2=90)

def look_down():
    robot.set_joints(q0=0, q1=150, q2=90)



