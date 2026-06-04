import pandas as pd
import seaborn as sns
import matplotlib.pyplot as pit


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




#-------------------------------
#GRAFICPO 1: Grafico de barras (con seaborn)
#-------------------------------


print("\n Generando grafico de Barras")


sns.set_theme(style="whitegrid")
pit.figure(figsize=(9,5))


#Define al grafico
sns.barplot(
   data= df, #Contiene los datos
   x="category", #Define que datos aparecen en el eje x
   y="total attempts team1", #Define que datos aparecen en el eje y
   estimator=sum,
   errorbar=None, #Desactiva las barras de error
   palette="viridis" #Paleta de color
)


#Otorga el titulo del grafico
pit.title("Distibucion de las categorias", fontsize=14)
pit.xlabel("Categoria", fontsize=11)
pit.ylabel("Empates team1", fontsize=11)


pit.tight_layout()
pit.xticks(rotation=40, fontsize=6)
pit.savefig("grafico_barras.png", dpi=300)
pit.close()
print("grafico de barras guardada exitosamente")


#------------------------------
# GRAFICO 2: Grafico de torta (con seaborn)
#------------------------------


print("\n Generando grafico de torta")


datos_torta=(df.groupby("category")["total attempts team1"].sum().nlargest(5))


pit.figure(figsize=(7,7))
pit.pie(
   datos_torta,
   labels=datos_torta.index,
   autopct="%1.1f%%",
   colors=sns.color_palette("Set2")[0:5],
   startangle=140,
   wedgeprops={'edgecolor':'white','linewidth':2}
)


pit.tight_layout()
pit.xticks(rotation=40, fontsize=6)
pit.savefig("grafico_torta.png", dpi=300)
pit.close()
print("Grafico de torta guardada exitosamente")

