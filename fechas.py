from datetime import datetime 

def calcular_dias (fecha1, fecha2):
    fecha1 = datetime.strptime(fecha1, '%Y-%m-%d')
    fecha2 = datetime.strptime(fecha2, '%Y-%m-%d') 
    diferencia_dias = fecha2 - fecha1
    return abs(diferencia_dias.days)
fecha_inicial = input("Ingresar la primera fecha:")
fecha_final = input("Ingresar la segunda fecha:") 

dias = calcular_dias(fecha_inicial, fecha_final )

print(f"La diferencia en días entre {fecha_inicial} y {fecha_final} es: {dias} dias") 


                               