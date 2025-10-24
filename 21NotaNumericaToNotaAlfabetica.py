#Actividad 21: Programa que lee una calificación numérica entre 0 y 10 y la transforma en calificación alfabética, escribiendo el resultado

def main():
    nota = float(input("Introduce la nota: "))
    if nota < 3 and nota >= 0:
        print("Muy Deficiente")
    elif nota < 5 and nota >= 3:
        print("Insuficiente")
    elif nota < 6 and nota >= 5:
        print("Suficiente")
    elif nota < 7 and nota >= 6:
        print("Bien")
    elif nota < 9 and nota >= 7:
        print("Notable")
    elif nota <= 10 and nota >= 9:
        print("Sobresaliente")
    else:
        print("Nota incorrecta")



if __name__ == "__main__":
    main()