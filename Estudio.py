# #1 inversion

#cap_inv=float(input("Capital que desa invertir"))
#gan=cap_inv*0.02
#print(f"la gannacia que va a genear el dinero es: ${gan:.2f}")

# #2 vendedor

#sb=float(input("Ingrese el salario basico"))
#v1=float(input("Ingrese el precio de la venta 1"))
#v2=float(input("Ingrese el precio de la venta 2"))
#v3=float(input("Ingrese el precio de la venta 3"))

#tot_vta=v1+v2+v3
#com=tot_vta*0.10
#tpag=sb+com

#print(f"El dinero que obtendra por comisiones es: ${com:.2f}")
#print(f"el dinero total es: ${tpag:.2f}")

# #3 tienda

#tc=float(input("Ingrese el precio del producto"))
#d=tc*0.15
#tp=tc-d
#print(f"El total a pagar es de: ${tp:.2f}")

# #4 alumno

#c1=float(input("Ingree su primer calificación"))
#c2=float(input("Ingree su segunda calificación"))
#c3=float(input("Ingree su tercera calificación"))
#ef=float(input("Ingree la nota de su examen final"))
#tf=float(input("Ingree la nota de su trabajo final"))
#prom=(c1+c2+c3)/3
#ppar=prom*0.55
#pef=ef*0.30
#ptf=tf*0.15
#cf=ppar+pef+ptf
#print(f"La calificacion final es: {cf:.2f}")


# #5 maestro

#nh=int(input("ingrese el numero de hombres"))
#nm=int(input("ingrese el numero de mujeres"))
#ta=nh+nm
#ph=nh*100/ta
#pm=nm*100/ta

#print(f"el porcentaje de hombres es: {ph:.0f}%")
#print(f"el porcentaje de mujeres es: {pm:.0f}%")

# #6

#fnac=int(input("Ingrese el año de nacimiento"))
#fact=int(input("Ingrese el año actual"))
#edad=fact-fnac
#print(f"Su edad es: {edad:.0f} años")

########################################
#Problemas compuestos
#######################################

# #1
#pesos=float(input("Ingrese el número de pesos que desea cambiar"))
#dolar=float(input("Ingrese el valor del dolar(En pesos)"))

#cambio=pesos/dolar
#print(cambio)

# #2
#numero=int(input("Ingrese un numero para sacarle el valor absoluto "))
#resul=abs(numero)
#print(f"El valor absoluto del número es: {resul}")

# #3
#presion=float(input("Ingrese el valor de la presión"))
#volumen=float(input("Ingrese el valor del volumen"))
#temperatura=float(input("Ingrese la temperatura"))

#masa=(presion*volumen)/(0.37*(temperatura+460))

# #4
#edad=int(input("Ingrese su edad"))

#numpulsaciones=(220-edad)/10

# #5
#salb=float(input("Ingrese su salario"))

#incre=salb*0.25
#saltot=salb+incre

#print(f"El nuevo salario es: {saltot} ")

# #6
#presuanu=float(input("Ingrese el presupuesto anual del hospital"))

#ginecolo=presuanu*0.40
#traumatolo=presuanu*0.30
#pedatri=presuanu*0.30
#print(f"El presupuesto que va a recibir ginecologia es: {ginecolo} "
#     f"el de tramatologia es: {traumatolo} "
#    f"el de pediatria es: {pedatri}")

# #7
#compra=float(input("Ingrese el precio del articulo"))

#ganan=compra*0.30
#venta=compra+ganan
#print(f"el precio con el que debe vender el articulo para ganar el 30% es: {venta}")

# #8
#lunes=float(input("Ingrese el tiempo del día lunes(en minutos)"))
#miercoles=float(input("Ingrese el tiempo del día miercoles (en minutos)"))
#viernes=float(input("Ingrese el tiempo del día viernes(en minutos)"))

#prom=(lunes+miercoles+viernes)/3

# #9
#perso1=float(input("Ingrese el valor de la primera persona"))
#perso2=float(input("Ingrese el valor de la segunda persona"))
#perso3=float(input("Ingrese el valor de la tercera persona"))

#total=perso1+perso2+perso3
#inve1=perso1*100/total
#inve2=perso2*100/total
#inve3=perso3*100/total

#print(f"El porcentaje que invirtio la persona 1 es: {inve1:.2f}%"
#      f"el de la persona 2 es: {inve2:.2f}%"
#      f"el de la persona 3 es: {inve3:.2f}%")

# #10
caliexmat=float(input("Ingrese el resultado del examen final de matematicas"))
tarea1mat=float(input("Ingrese la nota de la primera tarea"))
tarea2mat=float(input("Ingrese la nota de la segunda tarea"))
tarea3mat=float(input("ingrese la nota de la tercera tarea"))
promma=(tarea1mat+tarea2mat+tarea3mat)/3
prexamat=caliexmat*0.9
prepommat=promma*0.1
ttporcenmat=prepommat+prexamat
print(f"El promedio de  matematicas es: {ttporcenmat:.2f}")

caliexfi=float(input("Ingrese el resultado del examen final de física"))
tarea1fi=float(input("Ingrese la nota de la primera tarea"))
tarea2fi=float(input("Ingrese la nota de la segunda tarea"))
promfi=(tarea1fi+tarea2fi)/2
prexafi=caliexfi*0.8
prepomfi=promfi*0.2
ttporcenfi=prexafi+prepomfi
print(f" el promedio de física es: {ttporcenfi:.2f}")

caliexqui=float(input("Ingrese el resultado del examen de química"))
tarea1qui=float(input("Ingrese la nota de la primera tarea"))
tarea2qui=float(input("Ingrese la nota de la segunda tarea"))
tarea3qui=float(input("Ingrese la nota de la tercera tarea"))
promqui=(tarea1qui+tarea2qui+tarea3qui)/3
prexaqui=caliexqui*0.85
prepomqui=promqui*0.15
ttporcenqui=prexaqui+prepomqui

print(f" el promedio de química es: {ttporcenqui:.2f}")


