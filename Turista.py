total_distancia = 0
nombreStr = input("Ingrese su nombre por favor ->: ")
numero_escalas = int(input("Ingresa el numero de escalas ->: "))

 
for escala in range(numero_escalas):
    distance = int(input("ingrese la distancia de las escalas por favor ->: "))
    total_distancia += distance
    
print('Nombre: ', nombreStr)
print("la distancia total es -> ", total_distancia,'Km')
print('el numero de escalas es ->', numero_escalas)






