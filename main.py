import json

hojas_de_vida = []

def cargar_desde_json():
    global hojas_de_vida
    try:
        with open("datos.json", "r", encoding="utf-8") as archivo:#
            with open("datos.json", "r", encoding="utf-8") as archivo:
                with open("datos.json", "r", encoding="utf-8") as archivo:
                    hojas_de_vida = json.load(archivo)
        print("📂 Datos cargados desde datos.json")
    except FileNotFoundError:
        hojas_de_vida = []
        print(" No se encontró datos.json, se empezará desde cero")


def guardar_en_json():
    with open("datos.json", "w", encoding="utf-8") as archivo:
        json.dump(hojas_de_vida, archivo, ensure_ascii=False, indent=4)
    print(" Datos guardados en datos.json")


def registrar_hoja_de_vida():
    hoja = {}

    hoja["nombre"] = input("Nombre completo: ")
    hoja["documento"] = input("Número de documento: ")
    hoja["contacto"] = input("Número de contacto: ")
    hoja["direccion"] = input("Dirección: ")
    hoja["correo"] = input("Correo electrónico: ")
    hoja["fecha_nacimiento"] = input("Fecha de nacimiento (dd/mm/aaaa): ")

    hoja["formacion"] = []
    while input("¿Agregar formación académica? (s/n): ").lower() == "s": #lower() es una función integrada para cadenas que convierte todos los caracteres de mayúsculas a minúsculas
        hoja["formacion"].append({
            "institucion": input("Institución: "),
            "titulo": input("Título: "),
            "años": input("Años: ")
        })

    hoja["experiencia"] = []
    while input("¿Agregar experiencia laboral? (s/n): ").lower() == "s":
        hoja["experiencia"].append({
            "empresa": input("Empresa: "),
            "cargo": input("Cargo: "),
            "funciones": input("Funciones: "),
            "duracion": input("Duración: ")
        })

    hoja["referencias"] = []
    while input("¿Agregar referencia? (s/n): ").lower() == "s":
        hoja["referencias"].append({
            "nombre": input("Nombre: "),
            "relacion": input("Relación: "),
            "telefono": input("Teléfono: ")
        })

    hoja["habilidades"] = []
    while input("¿Agregar habilidad o certificación? (s/n): ").lower() == "s":
        hoja["habilidades"].append(input("Escribe la habilidad: "))

    hojas_de_vida.append(hoja)
    print(" Hoja de vida registrada con éxito.\n")


def consultar_hoja():
    criterio = input("Buscar por (nombre/documento/correo): ").lower()
    valor = input("Ingresa el valor a buscar: ").lower()
    encontrados = []

    for hoja in hojas_de_vida:
        if hoja.get(criterio, "").lower() == valor:
            encontrados.append(hoja)

    if encontrados:
        for hoja in encontrados:
            print("\n Hoja de vida encontrada:")
            for clave, valor in hoja.items():
                print(f"{clave.capitalize()}: {valor}")
    else:
        print(" No se encontraron resultados.")


def menu():
    cargar_desde_json()
    while True:
        print("\n----- MENÚ -----")
        print("1. Registrar hoja de vida")
        print("2. Consultar hoja de vida")
        print("3. Guardar y salir")

        opcion = input("Elige una opción: ")
        if opcion == "1":
            registrar_hoja_de_vida()
        elif opcion == "2":
            consultar_hoja()
        elif opcion == "3":
            guardar_en_json()
            print(" Programa finalizado.")
            break
        else:
            print(" Opción no válida. Intenta de nuevo.")

# Ejecutar el programa
menu()
