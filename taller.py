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


