import pandas as pd
import seaborn as sns
import matplotlib.pyplot as pit


#Importando csv
df=pd.read_csv("Fifa_world_cup_matches.csv")

print("OKEY! Archivo cargado correctamente")

#Mostrando las primeras filas del data frame
#print(df.head())

#cuenta la cantidad de filas y columnas que tiene
#filas,columnas = df.shape
#print (f"el detaframe tiene {filas} filas y {columnas} columnas")

#Cuenta las cantidades de goles que hizo el equipo 1
#total_golteam1 = df["number of goals team1"].count()
#print(f"Cantidad de filas con goles validos: {total_golteam1}")


#print("<-----Analisis avanzado de datos----->")


#Cuenta la cantidad de filas con una condicion
#filtro_avanzado = df['category'].str.startswith('Group A', na=False)
#df_filtrado = df[filtro_avanzado]


#Muestra los paises que estan en el grupo A
#total_registros = df_filtrado['category'].count()
#print(f"Cantidad de paises en el grupo A: {total_registros}")


#Suma los valores de las columnas
#suma_puntos=df_filtrado['total attempts team1'].sum()
#print(f"Total de puntaje en team1 es: {suma_puntos}")


#print("<-----Reporte automatizado----->")
#print(f"Total de puntaje en team1 es: {suma_puntos}")


#if Default_limite_alto:= (suma_puntos > 1000):
#   print("Alerta: Critico y alta prioridad")
#   print("Revisar inmediatamente")


#elif suma_puntos > 500:
#   print("Aviso: puntajes moderados/altos")
#   print("Requiere revision proximo campeonato")


#else:
#   print("El puntaje esta dentro de los parametros")
#   print("No requiere revision")




#-------------------------------
#GRAFICPO 1: Grafico de barras (con seaborn)
#-------------------------------


#print("\n Generando grafico de Barras")


#sns.set_theme(style="whitegrid")
#pit.figure(figsize=(9,5))


#Define al grafico
#sns.barplot(
#   data= df, #Contiene los datos
#   x="category", #Define que datos aparecen en el eje x
#   y="total attempts team1", #Define que datos aparecen en el eje y
#   estimator=sum,
#   errorbar=None, #Desactiva las barras de error
#   palette="viridis" #Paleta de color
#)


#Otorga el titulo del grafico
#it.title("Distibucion de las categorias", fontsize=14)
#pit.xlabel("Categoria", fontsize=11)
#pit.ylabel("Empates team1", fontsize=11)


#pit.tight_layout()
#pit.xticks(rotation=40, fontsize=6)
#pit.savefig("grafico_barras.png", dpi=300)
#pit.close()
#print("grafico de barras guardada exitosamente")


#------------------------------
# GRAFICO 2: Grafico de torta (con seaborn)
#------------------------------


#print("\n Generando grafico de torta")


#datos_torta=(df.groupby("category")["total attempts team1"].sum().nlargest(5))


#pit.figure(figsize=(7,7))
#pit.pie(
#   datos_torta,
#   labels=datos_torta.index,
#   autopct="%1.1f%%",
 #  colors=sns.color_palette("Set2")[0:5],
  # startangle=140,
   #wedgeprops={'edgecolor':'white','linewidth':2}
#)


#pit.tight_layout()
#pit.xticks(rotation=40, fontsize=6)
#pit.savefig("grafico_torta.png", dpi=300)
#pit.close()
#print("Grafico de torta guardada exitosamente")



#-------------------------Ejercicio 1-------------------------

filas,columnas = df.shape
print (f"La tabla contiene: {filas} filas y {columnas} columnas")

#-------------------------Ejercicio 2-------------------------

filtro_exacto = df['category'] == 'Group A'
df_filtrado = df[filtro_exacto]

total_registros = df_filtrado['category'].count()
print(f"Cantidad de partidos en el grupo A: {total_registros}")

#-------------------------Ejercicio 3-------------------------

filtro_avanzado = df['category'].str.startswith('G', na=False)
df_filtrado = df[filtro_avanzado]

#-------------------------Ejercicio 4-------------------------

df_dos_columnas = df_filtrado[['category', 'passes team1']]
print(df_dos_columnas.head())

#-------------------------Ejercicio 5-------------------------
df_agrupado = df.groupby('category')['passes team1'].sum().sort_values(ascending=False)
print(df_agrupado)

#-------------------------Ejercicio 6-------------------------
umbral_critico = 2000  

if (suma_puntos := df_dos_columnas['passes team1'].sum()) > umbral_critico:
    print(f"Total de pases: {suma_puntos}")
    print("Prioridad Alta")
else:
    print(f"Total de pases: {suma_puntos}")
    print("Estado Normal")
#-------------------------Ejercicio 7-------------------------
sns.set_theme(style="whitegrid")
pit.figure(figsize=(9,5))

sns.barplot(
   data= df,
   x="category", 
   y="passes team1", 
   hue="category",    
   legend=False,
   estimator=sum,
   errorbar=None,
   palette="viridis" 
)

pit.title("Grafico", fontsize=14)
pit.xlabel("category", fontsize=11)
pit.ylabel("passes team1", fontsize=11)

pit.tight_layout()
pit.xticks(rotation=40, fontsize=6)
pit.savefig("grafico_barras.png", dpi=300)
pit.close()
print("grafico de barras guardada exitosamente")

#-------------------------Ejercicio 8-------------------------
datos_torta=(df.groupby("category")["passes team1"].sum().nlargest(5))

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

#-------------------------Ejercicio 9-------------------------
condicion_extra = df['total attempts team1'] > 15
 
resultado = df.loc[
    filtro_avanzado & condicion_extra,
    ['team1', 'total attempts team1', 'passes team1']
]
 
print(resultado)
print(f'\nFilas seleccionadas: {len(resultado)}')

#→  ¿Cuántas filas quedaron después de aplicar el doble filtro?
#    Quedaron 6 filas
#→  ¿El resultado con .loc[] es igual al que hubieran obtenido en dos pasos separados?
#    Si, pero el codigo seria más largo y más "desordenado" 
#→  ¿Qué pasa si cambian & por | en el filtro? ¿Tiene sentido para sus datos?
#    Si uso & me aparecen 6 filas seleccionadas, en cambio con | me aparecen 51 filas seleccionadas.
#    En mi caso no tendria sentido usar | porque incluye partidos de otros grupos o que tengan pocos remates

#-------------------------Ejercicio 10-------------------------
# Paso 1: diagnóstico
print('Nulos por columna:')
print(df.isnull().sum())
 
# Paso 2: introducir nulos si no hay (para practicar)
df_con_nulos = df.copy()
df_con_nulos.loc[[0, 3, 7], 'passes team1'] = None
 
# Paso 3: confirmar
print('\nNulos después de modificar:')
print(df_con_nulos.isnull().sum())
 
# Paso 4a: eliminar filas con nulos
df_sin_nulos = df_con_nulos.dropna()
 
# Paso 4b: reemplazar nulos con la media
media = df_con_nulos['passes team1'].mean()
df_rellenado = df_con_nulos.fillna({'passes team1': round(media, 2)})
 
# Paso 5: comparar
print(f'\nOriginal:   {len(df_con_nulos)} filas')
print(f'Con dropna: {len(df_sin_nulos)} filas  (se eliminaron filas)')
print(f'Con fillna: {len(df_rellenado)} filas  (se rellenaron los huecos)')

#→  ¿Cuál de las dos estrategias (dropna o fillna) es más conveniente para sus datos? ¿Por qué?
#    Fillna es más conveviente de utilizar en esta dataset, porque tengo pocos datos.
#→  ¿Qué problema puede generar fillna con la media si los nulos son muchos? 
#    RESPONDERR
#→  ¿Cambiaría algo en sus análisis anteriores si hubiera nulos reales en sus datos?
#    RESPONDER

#-------------------------Ejercicio 11-------------------------
import matplotlib.pyplot as plt
 
# Paso 1 y 2: agrupar y ordenar
agrupado = df.groupby('columna_texto')['columna_numerica'].sum().sort_values()
 
# Paso 3: gráfico de líneas
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(agrupado.index, agrupado.values, marker='o',
        color='#2E75B6', linewidth=2, markersize=8)
 
# Paso 4: detectar y anotar el máximo
idx_max = agrupado.idxmax()          # categoría con valor más alto
val_max = agrupado.max()             # valor más alto
 
ax.annotate(
    f'Máximo: {val_max:,.0f}',       # texto de la anotación
    xy=(idx_max, val_max),           # punto al que apunta la flecha
    xytext=(1, val_max * 0.85),      # posición del texto
    arrowprops=dict(arrowstyle='->', color='red'),
    fontsize=11, color='red', fontweight='bold'
)
 
# Paso 5: configuración final
ax.set_title('Evolución por categoría', fontsize=14, fontweight='bold')
ax.set_xlabel('Categoría')
ax.set_ylabel('Total')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('grafico_lineas.png', dpi=150)
plt.show()
