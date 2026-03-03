'''
Programa que lee una calificación numérica entre 0 y 10 de cada alumno del aula, se acabará cuando a la pregunta ¿Otro alumno si/no? se le conteste que no.

Debes escribir una función para solicitar la nota (validándola) el método debe devolver una nota válida.
Otra función a la que se le pase una nota numérica y devuelva una calificación alfabética:
de 0 a <3 Muy Deficiente.
de 3 a <5 Insuficiente.
de 5 a <6 Suficiente.
de 5 a <6 Bien.
de 6 a <9 Notable
de 9 a 10 Sobresaliente
'''

#Funcion que comprueba que las respuestas sean si o no
def si_no(m):
    bucle = True
    while bucle:
        respuesta = input(m).strip().lower()
        if respuesta == "si" or respuesta == "no":
            bucle=False
        else:
            print("\nError: La respuesta tiene que ser si o no\n")
    return respuesta

#Funcion que comprueba que el numero esta dentro del rango establecidos
def solicitar_nota():
    si = True
    while si:
        nota = float(input("Introduce la nota del alumno (0-10): "))
        if 0 <= nota and nota <= 10:
            si=False
        else:
            print("\nError: La nota debe estar entre 0 y 10\n")
    return nota

#Funcion que transcribe las numericos a alfanumericos
def nota_a_calificacion(nota):
    notita=""

    if nota < 3:
        notita = "Muy Deficiente"
    elif nota < 5:
        notita = "Insuficiente"
    elif nota < 6:
        notita ="Suficiente"
    elif nota < 7:
        notita = "Bien"
    elif nota < 9:
        notita = "Notable"
    else:
        notita = "Sobresaliente"

    return notita

#Funcion Principal
def main():
    si=True
    print("=== Sistema de Calificaciones ===\n")
    #Bucle principal que se encarga de pedir las notas hasta que el usuario diga que no.    
    while si:
        #Guardar la informacion de nota
        nota = solicitar_nota()        
        #Guardar la informacion de la calificacion
        calificacion = nota_a_calificacion(nota)
        
        print(f"Calificación: {nota} - {calificacion}\n")

        respuesta = si_no((f"¿Otro alumno? (si/no): "))
        
        if respuesta != "si" and respuesta != "sí":
            print("\nPrograma finalizado.")
            si = False
        print("=" * 25) 

if __name__ == "__main__":
    main()
