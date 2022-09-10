import numpy as np
def position_to_dof(x, y, z):
    """Acá va tu código para calcular la cinemática inversa
    
    La función debe recibir (x,y,z) en milimetros y retornar q0, q1 y q2 en grados"""


    #a0
    a = 94
    #a1
    b = 135
    #a2
    c = 147
    #a3
    d = 66



    q0 = np.arctan(y/x) # reemplaza el cero por la ecuación que describe q0 en función de (x,y)
    L = x/np.cos(q0)
    # reemplaza el cero por la ecuación que describe q0 en función de (x,y,z)
    q2 = np.arccos( ((L-d)**2 + (z-a)**2 - b**2 - c**2)/(2*b*c))  # reemplaza el cero por la ecuación que describe q0 en función de (x,y,z)
    q1 = np.arctan(z / (L - d)) - np.arctan(b * np.sin(q2) / (a + b * np.cos(q2)))
    print(q2)
    return int(np.degrees(q0)), int(np.degrees(q1)), int(np.degrees(q2))    # El robot solo entiende grados sexagesimales y enteros
