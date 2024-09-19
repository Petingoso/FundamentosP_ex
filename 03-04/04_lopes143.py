initSeg = eval(input("Escreva o número de segundos: "))

days = initSeg//86400
hour = (initSeg%86400)//3600
mins = ((initSeg%86400)%3600)//60
segs = ((initSeg%86400)%3600)%60

print("Dias: ", days, "; Horas: ", hour, "; Minutos: ", mins, "; Segundos: ", segs)
