# ============================================================
# UTILS.PY v2 - Funciones auxiliares
# ============================================================


# ------------------------------------------------------------
# ENTRADAS DE TEXTO
# ------------------------------------------------------------

# Pide un texto y valida que no este vacio
def pedir_texto(mensaje):
    seguir = True
    texto = ""
    while seguir:
        texto = input(f"\n{mensaje}: ").strip()
        if len(texto) == 0:
            print("\nError: El campo no puede estar vacio.\n")
        else:
            seguir = False
    return texto

# Pide un texto y valida que no este vacio y que solo tenga letras y espacios
def pedir_nombre(mensaje):
    seguir = True
    texto = ""
    while seguir:
        texto = input(f"\n{mensaje}: ").strip()
        if len(texto) == 0:
            print("\nError: El campo no puede estar vacio.\n")
        elif not texto.replace(" ", "").isalpha():
            print("\nError: Solo se permiten letras y espacios.\n")
        else:
            seguir = False
    return texto

# Pide un email y valida que tenga @ y un punto despues del @
def pedir_email(mensaje):
    seguir = True
    email = ""
    while seguir:
        email = input(f"\n{mensaje}: ").strip().lower()
        if len(email) == 0:
            print("\nError: El campo no puede estar vacio.\n")
        elif "@" not in email:
            print("\nError: El email debe contener @.\n")
        else:
            partes = email.split("@")
            if len(partes) != 2 or len(partes[0]) == 0:
                print("\nError: El formato del email no es valido (ej: nombre@gmail.com).\n")
            elif "." not in partes[1] or partes[1].startswith(".") or partes[1].endswith("."):
                print("\nError: El dominio del email no es valido (ej: nombre@gmail.com).\n")
            else:
                seguir = False
    return email


# ------------------------------------------------------------
# ENTRADAS NUMERICAS
# ------------------------------------------------------------

# Comprueba si un texto es un numero entero valido (admite negativos)
def es_entero(texto):
    resultado = False
    if len(texto) > 0:
        if texto[0] == "-" and len(texto) > 1:
            resultado = texto[1:].isnumeric()
        else:
            resultado = texto.isnumeric()
    return resultado

# Comprueba si un texto es un numero decimal valido (admite negativos y punto o coma)
def es_decimal(texto):
    resultado = False
    texto_norm = texto.replace(",", ".")
    if len(texto_norm) > 0:
        if texto_norm[0] == "-" and len(texto_norm) > 1:
            partes = texto_norm[1:].split(".")
        else:
            partes = texto_norm.split(".")
        if len(partes) == 1:
            resultado = partes[0].isnumeric()
        elif len(partes) == 2:
            resultado = partes[0].isnumeric() and partes[1].isnumeric()
    return resultado

# Pide un numero entero entre x e y con mensaje personalizado
def pedir_num_extra(x, y, z):
    seguir = True
    numero = 0
    while seguir:
        texto = input(f"{z} entre {x} y {y}: ").strip()
        if not es_entero(texto):
            print("\nError: Debes introducir un numero entero.\n")
        else:
            numero = int(texto)
            if numero >= x and numero <= y:
                seguir = False
            else:
                print(f"\nError: El numero debe estar entre {x} y {y}.\n")
    return numero

# Pide un numero entero entre x e y (version para menus internos con salto de linea)
def pedir_Num_Premium(x, y, z):
    seguir = True
    numero = 0
    while seguir:
        texto = input(f"\n{z}").strip()
        if not es_entero(texto):
            print("\nError: Debes introducir un numero entero.\n")
        else:
            numero = int(texto)
            if numero >= x and numero <= y:
                seguir = False
            else:
                print(f"\nError: El numero debe estar entre {x} y {y}.\n")
    return numero

# Pide un numero entero estrictamente mayor que x con mensaje personalizado
def mayor_premium(z, x):
    seguir = True
    numero = 0
    while seguir:
        texto = input(f"\n{z} (mayor que {x}): ").strip()
        if not es_entero(texto):
            print("\nError: Debes introducir un numero entero.\n")
        else:
            numero = int(texto)
            if numero > x:
                seguir = False
            else:
                print(f"\nError: El numero debe ser mayor que {x}.\n")
    return numero

# Pide un numero decimal (float) entre x e y con mensaje personalizado
def pedir_float(x, y, z):
    seguir = True
    numero = 0.0
    while seguir:
        texto = input(f"\n{z} (entre {x} y {y}): ").strip()
        if not es_decimal(texto):
            print("\nError: Debes introducir un numero valido (ej: 9.99).\n")
        else:
            numero = float(texto.replace(",", "."))
            if numero >= x and numero <= y:
                seguir = False
            else:
                print(f"\nError: El numero debe estar entre {x} y {y}.\n")
    return numero

# Pide un numero decimal (float) mayor que x con mensaje personalizado
def pedir_float_mayor(z, x):
    seguir = True
    numero = 0.0
    while seguir:
        texto = input(f"\n{z} (mayor que {x}): ").strip()
        if not es_decimal(texto):
            print("\nError: Debes introducir un numero valido (ej: 9.99).\n")
        else:
            numero = float(texto.replace(",", "."))
            if numero > x:
                seguir = False
            else:
                print(f"\nError: El numero debe ser mayor que {x}.\n")
    return numero


# ------------------------------------------------------------
# CONFIRMACIONES
# ------------------------------------------------------------

# Pide si o no, acepta: si, no
def si_no(m):
    seguir = True
    respuesta = ""
    while seguir:
        respuesta = input(m).strip().lower()
        if respuesta == "si" or respuesta == "no":
            seguir = False
        else:
            print("\nError: La respuesta tiene que ser si o no.\n")
    return respuesta

# Confirmacion rapida, acepta: s, n, si, no — devuelve True o False
def confirmar(mensaje):
    seguir = True
    resultado = False
    while seguir:
        respuesta = input(f"\n{mensaje} (s/n): ").strip().lower()
        if respuesta == "s" or respuesta == "si":
            resultado = True
            seguir = False
        elif respuesta == "n" or respuesta == "no":
            resultado = False
            seguir = False
        else:
            print("\nError: Responde con s o n.\n")
    return resultado


# ------------------------------------------------------------
# FECHAS
# ------------------------------------------------------------

# Pide y valida una fecha en formato DD/MM/AAAA
# anio_min: año minimo permitido (por defecto 2000)
# anio_max: año maximo permitido (por defecto 2100)
# mensaje:  texto que se muestra al pedir la fecha
def fecha(mensaje="Introduce la fecha (DD/MM/AAAA)", anio_min=2000, anio_max=2100):
    dias_por_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    seguir = True
    nueva_fecha = ""
    while seguir:
        nueva_fecha = input(f"\n{mensaje}: ").strip()
        if len(nueva_fecha) != 10 or nueva_fecha[2] != "/" or nueva_fecha[5] != "/":
            print("\nError: El formato debe ser DD/MM/AAAA.\n")
        elif not nueva_fecha[0:2].isnumeric() or not nueva_fecha[3:5].isnumeric() or not nueva_fecha[6:10].isnumeric():
            print("\nError: El dia, mes y año deben ser numeros.\n")
        else:
            dia  = int(nueva_fecha[0:2])
            mes  = int(nueva_fecha[3:5])
            anio = int(nueva_fecha[6:10])
            if anio < anio_min or anio > anio_max:
                print(f"\nError: El año debe estar entre {anio_min} y {anio_max}.\n")
            elif mes < 1 or mes > 12:
                print("\nError: El mes debe estar entre 1 y 12.\n")
            else:
                max_dia = dias_por_mes[mes]
                if mes == 2 and (anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)):
                    max_dia = 29
                if dia < 1 or dia > max_dia:
                    print(f"\nError: El dia debe estar entre 1 y {max_dia} para el mes {mes}.\n")
                else:
                    seguir = False
    return nueva_fecha


# ------------------------------------------------------------
# MENUS Y DISPLAY
# ------------------------------------------------------------

# Muestra una lista de opciones de menu
def mostrarMenu(menu):
    for op in menu:
        print(op)

# Imprime un titulo con bordes de = arriba y abajo, centrado en el ancho indicado
def centrar_titulo(titulo, ancho=60):
    print("\n" + "=" * ancho)
    print(f"=== {titulo} ===".center(ancho))
    print("=" * ancho)

# Recorta un texto a 'maximo' caracteres y añade '...' si se pasa
def truncar(texto, maximo):
    resultado = texto
    if len(texto) > maximo:
        resultado = texto[0:maximo - 3] + "..."
    return resultado

# Muestra una lista simple de strings numerada (pasos, horarios, platos...)
def mostrar_lista_numerada(lista):
    if len(lista) == 0:
        print("  (lista vacia)")
    else:
        indice = 1
        for elemento in lista:
            print(f"  {indice}. {elemento}")
            indice = indice + 1

# Calcula el subtotal de un producto (precio * cantidad)
def calcular_subtotal(precio, cantidad):
    return precio * cantidad


# ------------------------------------------------------------
# BUSQUEDAS
# ------------------------------------------------------------

# Busca en una lista de diccionarios por el campo "numero"
def buscar(lista, numBuscar):
    resultado = None
    enc = False
    cont = 0
    while cont < len(lista) and not enc:
        if lista[cont]["numero"] == numBuscar:
            resultado = lista[cont]
            enc = True
        else:
            cont = cont + 1
    return resultado

# Busca en una lista de diccionarios por el campo "id"
def buscarv2(lista, numBuscar):
    resultado = None
    enc = False
    cont = 0
    while cont < len(lista) and not enc:
        if lista[cont]["id"] == numBuscar:
            resultado = lista[cont]
            enc = True
        else:
            cont = cont + 1
    return resultado

# Comprueba si un ID esta libre en una lista de diccionarios, devuelve True si esta disponible
# campo: nombre de la clave a comprobar, normalmente "numero" o "id"
def id_disponible(lista, numero, campo):
    libre = True
    enc = False
    cont = 0
    while cont < len(lista) and not enc:
        if lista[cont][campo] == numero:
            enc = True
            libre = False
        else:
            cont = cont + 1
    return libre


# ------------------------------------------------------------
# MAIN (solo para probar el utils directamente)
# ------------------------------------------------------------

def main():
    centrar_titulo("TEST DE UTILS", 60)

    nombre = pedir_nombre("Introduce tu nombre")
    print(f"Nombre guardado: {nombre}")

    email = pedir_email("Introduce tu email")
    print(f"Email guardado: {email}")

    precio = pedir_float(0, 999, "Introduce un precio")
    print(f"Precio guardado: {precio:.2f} euros")

    titulo_largo = "Este es un titulo extremadamente largo que descuadraria cualquier tabla"
    print(f"Truncado a 35: '{truncar(titulo_largo, 35)}'")

    print("\nLista de ejemplo:")
    mostrar_lista_numerada(["Paso uno", "Paso dos", "Paso tres"])

    lista_prueba = [{"numero": 101}, {"numero": 102}, {"numero": 103}]
    print(f"\nID 101 disponible: {id_disponible(lista_prueba, 101, 'numero')}")
    print(f"ID 999 disponible: {id_disponible(lista_prueba, 999, 'numero')}")

    if confirmar("¿Quieres continuar?"):
        print("Has dicho que si.")
    else:
        print("Has dicho que no.")

    fecha_resultado = fecha("Introduce tu fecha de nacimiento", anio_min=1900, anio_max=2025)
    print(f"Fecha guardada: {fecha_resultado}")

if __name__ == "__main__":
    main()
