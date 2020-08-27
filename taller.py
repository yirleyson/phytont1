'''
class Vendedor():
    sb=''
    v1=''
    v2=''
    v3=''
    pass #
persona=Vendedor()
persona.sb=float(input("Digite su salario basico "))
persona.v1=float(input("Ingrese la venta #1 "))
persona.v2=float(input("Ingrese la venta #2 "))
persona.v3=float(input("Ingrese la venta #3 "))
tot_vta=persona.v1+persona.v2+persona.v3
com=tot_vta*0.10
tpag=persona.sb+com
print(f"Él total de pago es: {tpag} Y el total de la comisión es: {com}")
'''
'''
class Alumno():
    c1=''
    c2=''
    c3=''
    ef=''
    tf=''
    pass #
estudiante=Alumno()
estudiante.c1=float(input("Ingrese la nota #1 "))
estudiante.c2=float(input("Ingrese la nota #2 "))
estudiante.c3=float(input("Ingrese la nota #3 "))
estudiante.ef=float(input("Ingrese la nota del examen final "))
estudiante.tf=float(input("Ingrese la nota del taller final "))
prom=(estudiante.c1+estudiante.c2+estudiante.c3)/3
ppar=prom*0.55
pef=estudiante.ef*0.30
ptf=estudiante.tf*0.15
cf=ppar+pef+ptf
print(f"La calificación es: {cf}")
'''

####################################################################
#Trabajo con tkinter
from tkinter import *

ventana=Tk()
ventana.geometry("600x500")
ventana.title("Aplicación")

text1=Entry(ventana)
text1.grid(row=0 , column=1 , padx=5 , pady=5)

cali1=Label(ventana, text="Ingrese la nota #1")
cali1.grid(row=0 , column=0 , padx=5 , pady=5,sticky="e")
#############################################
text2=Entry(ventana)
text2.grid(row=1 , column=1 , padx=5 , pady=5)

cali2=Label(ventana, text="Ingrese la nota #2")
cali2.grid(row=1 , column=0 , padx=5 , pady=5,sticky="e")
##############################################
text3=Entry(ventana)
text3.grid(row=2 , column=1 , padx=5 , pady=5)

cali3=Label(ventana, text="Ingrese la nota #3")
cali3.grid(row=2 , column=0 , padx=5 , pady=5,sticky="e")

text4=Entry(ventana)
text4.grid(row=3 , column=1 , padx=5 , pady=5)

exafi=Label(ventana, text="Ingrese la nota del examen final")
exafi.grid(row=3 , column=0 , padx=5 , pady=5,sticky="e")

text5=Entry(ventana)
text5.grid(row=4 , column=1 , padx=5 , pady=5)

tallfi=Label(ventana, text="Ingrese la nota del taller final")
tallfi.grid(row= 4, column=0 , padx=5 , pady=5,sticky="e")

def botoncalcu():
  
    prom = (float(text1.get()) + float(text2.get())+ float(text3.get())) / 3
    ppar = prom * 0.55
    pef = float(text4.get()) * 0.30
    ptf = float(text5.get()) * 0.15
    cf = ppar + pef + ptf
    print(cf)

boton=Button(ventana, text="Calcular", command=botoncalcu)
boton.grid(row=5 , column=1 , padx=5 , pady=5)

ventana.mainloop()

