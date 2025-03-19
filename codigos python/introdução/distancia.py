import math 

t1=float(input(" digite a latitude do primeiro ponto em graus: "))
g1=float(input("digite a longitude do primeiro ponto em graus: "))
t2=float(input("digite a latitude do segundo ponto em graus: "))
g2=float(input("digite a longitude do segundo ponto em graus: "))

t1r=math.radians(t1)
g1r=math.radians(g1)
t2r=math.radians(t2)
g2r=math.radians(g2)

distancia=6371.01*math.acos(math.sin(t1r)*math.sin(t2r)+math.cos(t1r)*math.cos(t2r)*math.cos(g1r-g2r))

print("a distancia entre os dois pontos é",distancia,"quilômetros.")
