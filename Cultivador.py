yucaInt= 0
papaInt = 0
zanahoriaInt = 0

tipo_de_tuberculoInt = int (input ('<<<<< MENÚ DE OPCIONES>>>>>\n\n1. papa\n2. yuca\n3. zanahoria\n ->'))
if tipo_de_tuberculoInt ==1:
    for  i in range (3):
        ltsInt = int(input('Con litros gastastes hoy -> '))
        papaInt += ltsInt
print('Los litros consumidos esta semana para la riega de la papita fueron: ',papaInt)        

if tipo_de_tuberculoInt ==2:
     for  i in range (2):
            ltsInt = int(input('Con litros gastastes hoy  -> '))
            yucaInt += ltsInt
print('Los litros consumidos esta semana para la riega de la yuquita fueron: ',yucaInt)   

if tipo_de_tuberculoInt == 3:
 for  i in range (2):
        ltsInt = int(input('Con litros gastastes hoy  -> '))
        zanahoriaInt += ltsInt
print('Los litros consumidos esta semana para la riega de la zanahorita fueron: ',zanahoriaInt)