km = eval(input("Introduza a distância percorrida em Km: "))
time =  eval(input("Introduza o tempo necessário para a percorrer em minutos: "))
kmh = km/(time/60)
mps = (km*1000)/(time*60)
print("Km/h: ", kmh)
print("m/s: ", mps)