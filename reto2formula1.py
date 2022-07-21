distancia_metrosP1, record_V_actualP2, tiempo_segundosP1 = input().split()
distancia_metrosP1 = float(distancia_metrosP1) 
record_V_actualP2 =  float(record_V_actualP2)
tiempo_segundosP1 =  float(tiempo_segundosP1)

distanciaKmP1 = float(distancia_metrosP1 / 1000)
tiempoHoraP1  = float(tiempo_segundosP1 / 3600)
#record mi piloto
velocidadMediaP1 = int(distanciaKmP1 / tiempoHoraP1)
ochentaPorcP2 = record_V_actualP2 + (record_V_actualP2 * 0.8)
#record_P_actualP2 = record_V_actualP2 + (record_V_actualP2*0.20)

record_a_MetrosP2 = record_V_actualP2*1000
record_a_SegundosP2 = round((3600/record_a_MetrosP2),4)
record_a_segundosP1 = round((tiempo_segundosP1 / distancia_metrosP1),4)


c_veinte= record_V_actualP2 + (record_V_actualP2/100 * 20)

print(velocidadMediaP1, ochentaPorcP2)
print(record_a_segundosP1, record_a_SegundosP2)
print(c_veinte)


if  record_a_segundosP1 == record_a_SegundosP2:
    print("VELOCIDAD NORMAL")
elif  record_a_segundosP1 < record_a_SegundosP2 and tiempoHoraP1==299: 
    print("NUEVO RECORD")
elif velocidadMediaP1 >= c_veinte: #
    print("ENTREVISTA")
elif distancia_metrosP1 <0 and record_V_actualP2 <0 and tiempo_segundosP1 <0:
    print("ERROR")
