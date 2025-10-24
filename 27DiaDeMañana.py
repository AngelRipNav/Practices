#Ejercicio 27: Te dice el dia de mañana


def main():
    dia = int(input("Introduce el dia: "))
    mes = int(input("Introduce el mes: "))
    ano = int(input("Introduce el año: "))
    dia = dia + 1
    if mes < 1 or mes > 12 or (dia < 1 or dia > 31):
        print("Fecha incorrecta")
    else:
        if mes in (1, 3, 5, 7, 8, 10, 12):
            if dia > 31:
                dia = 1
                mes = mes + 1
                if mes > 12:
                    mes = 1
                    ano = ano + 1
        elif mes in (4, 6, 9, 11):
            if dia > 30:
                dia = 1
                mes = mes + 1
        elif mes == 2:
            if dia > 28:
                dia = 1
                mes = mes + 1
        print(f"La fecha del día siguiente es: {dia}/{mes}/{ano}")

if __name__ == "__main__":
    main()