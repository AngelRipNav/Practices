#Ejercicio 24: Calcular el salario neto de un trabajador a partir de las horas trabajadas, el precio por hora y las tasas aplicables. 

def main():
    nombre = input("Introduce tu nombre: ")
    horas_trabajadas = int(input("Introduce las horas trabajadas: "))
    precio_hora = float(input("Introduce el precio por hora: "))
    if horas_trabajadas <= 35:
        salario_bruto = horas_trabajadas * precio_hora
    else:
        salario_bruto = 35 * precio_hora
        salario_bruto = salario_bruto + (horas_trabajadas - 35) * precio_hora * 1.5

    if salario_bruto <= 500:
        tasas = 0
    elif salario_bruto <= 900:
        tasas = 0.25
        tasas = (salario_bruto - 500) * tasas
    else:
        tasas = 0.45
        tasas = (salario_bruto - 900) * tasas + 100
    salario_neto = salario_bruto - tasas

    print("Nombre:", nombre)
    print(f"Salario bruto: {salario_bruto:.2f} euros")
    print(f"Tasas: {tasas:.2f} euros")
    print(f"Salario neto: {salario_neto:.2f} euros")


if __name__ == "__main__":
    main()


