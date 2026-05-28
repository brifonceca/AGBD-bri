import pandas as pd

#Importando csv
df=pd.read_csv("Fifa_world_cup_matches.csv")

print("OKEY! Archivo cargado correctamente")
# Mostrando las primeras filas del data frame
print(df.head())

#cuenta la cantidad de filas y columnas que tiene
filas,columnas = df.shape
print (f"el detaframe tiene {filas} filas y {columnas} columnas")

total_golteam1 = df["number of goals team1"].count()
print(f"Cantidad de filas con goles validos: {total_golteam1}")

print("<-----Analisis avanzado de datos----->")

#Cuenta la cantidad de filas con una condicion
filtro_avanzado = df['category'].str.startswith('Group A', na=False)
df_filtrado = df[filtro_avanzado]

#Muestra los paises que estan en el grupo A
total_registros = df_filtrado['category'].count()
#print(f"Cantidad de paises en el grupo A: {total_registros}")

#Suma los valores de las columnas
suma_puntos=df_filtrado['total attempts team1'].sum()
#print(f"Total de puntaje en team1 es: {suma_puntos}")

print("<-----Reporte automatizado----->")
print(f"Total de puntaje en team1 es: {suma_puntos}")

if Default_limite_alto:= (suma_puntos > 1000):
    print("Alerta: Critico y alta prioridad")
    print("Revisar inmediatamente")

elif suma_puntos > 500:
    print("Aviso: puntajes moderados/altos")
    print("Requiere revision proximo campeonato")

else:
    print("El puntaje esta dentro de los parametros")
    print("No requiere revision")