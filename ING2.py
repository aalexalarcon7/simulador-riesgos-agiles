import random

RIESGOS_POSIBLES = {
    "Fallo en integración continua": "Revisar pipeline y realizar pruebas automatizadas",
    "Retraso por enfermedad": "Asignar tareas de respaldo a otro miembro del equipo",
    "Cambio en requisitos del cliente": "Solicitar confirmación escrita de requerimientos",
    "Problemas de comunicación": "Implementar reuniones diarias breves (daily stand-up)",
    "Falta de recursos técnicos": "Solicitar soporte técnico o herramientas adecuadas",
    "Conflictos en el equipo": "Facilitar espacios de resolución de conflictos y feedback",
    "Retrasos en entregas de terceros": "Establecer acuerdos con fechas límite claras y seguimiento",
    "Tareas mal estimadas": "Revisar estimaciones con el equipo y usar datos históricos",
    "Fallo en pruebas de calidad": "Incluir pruebas automatizadas y QA en el flujo de trabajo",
    "Desmotivación del equipo": "Fomentar reconocimiento, apoyo y feedback regular"
}

def categorizar_prioridad(valor):
    if valor <= 6:
        return "Bajo"
    elif valor <= 14:
        return "Medio"
    else:
        return "Alto"

class Riesgo:
    def __init__(self, nombre, probabilidad, impacto):
        self.nombre = nombre
        self.probabilidad = probabilidad
        self.impacto = impacto
        self.prioridad = probabilidad * impacto
        self.categoria = categorizar_prioridad(self.prioridad)
        self.mitigacion = RIESGOS_POSIBLES[nombre]

    def reporte(self):
        return (
            f"  Riesgo: {self.nombre}\n"
            f"    Probabilidad: {self.probabilidad} / 5\n"
            f"    Impacto: {self.impacto} / 5\n"
            f"    → Prioridad: {self.prioridad} ({self.categoria})\n"
            f"    Mitigación: {self.mitigacion}\n"
        )

class SimuladorDeRiesgos:
    def __init__(self):
        self.resultados = [] 

    def ejecutar(self, cantidad_sprints):
        self.resultados.clear()
        for sprint in range(1, cantidad_sprints + 1):
            cantidad_riesgos = random.randint(1, 3)
            riesgos_disponibles = list(RIESGOS_POSIBLES.keys())
            riesgos_sprint = []

            for _ in range(cantidad_riesgos):
                nombre_riesgo = random.choice(riesgos_disponibles)
                riesgos_disponibles.remove(nombre_riesgo)
                probabilidad = random.randint(1, 5)
                impacto = random.randint(1, 5)
                riesgo = Riesgo(nombre_riesgo, probabilidad, impacto)
                riesgos_sprint.append(riesgo)

            self.resultados.append((sprint, riesgos_sprint))

    def obtener_reporte_completo(self):
        if not self.resultados:
            return "❗ No se ha simulado ningún sprint todavía.\n"
        texto = "\n📋 Informe de Riesgos por Sprint:\n\n"
        for sprint, lista_riesgos in self.resultados:
            texto += f"--- Sprint {sprint} ---\n"
            for riesgo in lista_riesgos:
                texto += riesgo.reporte() + "\n"
        return texto

    def obtener_reporte_altos(self):
        if not self.resultados:
            return "❗ No se ha simulado ningún sprint todavía.\n"
        texto = "\n🔥 Riesgos de Alta Prioridad:\n\n"
        encontrados = False
        for sprint, lista_riesgos in self.resultados:
            for riesgo in lista_riesgos:
                if riesgo.categoria == "Alto":
                    texto += f"--- Sprint {sprint} ---\n"
                    texto += riesgo.reporte() + "\n"
                    encontrados = True
        if not encontrados:
            texto += "No se detectaron riesgos de alta prioridad.\n"
        return texto

    def obtener_resumen_estadistico(self):
        if not self.resultados:
            return "❗ No se ha simulado ningún sprint todavía.\n"
        texto = "\n📊 Resumen Estadístico por Sprint:\n\n"
        for sprint, lista_riesgos in self.resultados:
            num_riesgos = len(lista_riesgos)
            suma_prioridades = sum([riesgo.prioridad for riesgo in lista_riesgos])
            promedio_prioridad = suma_prioridades / num_riesgos if num_riesgos > 0 else 0
            categoria_global = categorizar_prioridad(promedio_prioridad)

            texto += f"--- Sprint {sprint} ---\n"
            texto += f"  Total de Riesgos: {num_riesgos}\n"
            texto += f"  Promedio de Prioridad: {promedio_prioridad:.2f} ({categoria_global})\n"
            texto += f"  Categoría General del Sprint: {categoria_global}\n\n"
        return texto

    def guardar_en_archivo(self, nombre_archivo):
        try:
            with open(nombre_archivo, "w", encoding="utf-8") as f:
                f.write(self.obtener_reporte_completo())
            print(f"\n✅ Informe guardado como '{nombre_archivo}'")
        except Exception as e:
            print(f"❌ Error al guardar el archivo: {e}")

def mostrar_menu():
    simulador = SimuladorDeRiesgos()
    while True:
        print("\n📊 Menú Principal")
        print("1. Simular sprints")
        print("2. Ver informe completo")
        print("3. Ver solo riesgos de alta prioridad")
        print("4. Ver resumen estadístico por sprint")
        print("5. Guardar informe en archivo de texto")
        print("6. Salir")

        opcion = input("Seleccione una opción (1-6): ")

        if opcion == "1":
            try:
                cantidad = int(input("Ingrese la cantidad de sprints a simular: "))
                if cantidad <= 0:
                    raise ValueError("La cantidad debe ser positiva.")
                simulador.ejecutar(cantidad)
                print(f"\n✅ Simulación de {cantidad} sprint(s) completada.")
            except ValueError as e:
                print(f"❗ Error: {e}")
        elif opcion == "2":
            print(simulador.obtener_reporte_completo())
        elif opcion == "3":
            print(simulador.obtener_reporte_altos())
        elif opcion == "4":
            print(simulador.obtener_resumen_estadistico())
        elif opcion == "5":
            if not simulador.resultados:
                print("❗ Primero debe simular al menos un sprint.")
                continue
            nombre_archivo = input("Ingrese el nombre del archivo (ej: informe.txt): ")
            simulador.guardar_en_archivo(nombre_archivo)
        elif opcion == "6":
            print("👋 Fin del programa.")
            break
        else:
            print("❗ Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    mostrar_menu()

