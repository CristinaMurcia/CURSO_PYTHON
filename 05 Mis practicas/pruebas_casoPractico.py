class TareasPendientes:
    def __init__(self):
        # Inicializa la lista de tareas pendientes
        self.tareas = []

    def agregar_tarea(self, tarea):
        # Agrega una nueva tarea a la lista de tareas pendientes
        self.tareas.append({"descripcion": tarea, "completada": False})

    def marcar_completada(self, posicion):
        try:
            # Intenta marcar como completada la tarea en la posición especificada
            self.tareas[posicion]["completada"] = True
            print("Tarea marcada como completada.")
        except IndexError:
            # Captura el error si la posición especificada no existe en la lista de tareas
            print("La posición especificada no existe.")

    def mostrar_tareas(self):
        print("Tareas pendientes:")
        # Itera sobre todas las tareas y las imprime mostrando su estado (completada o pendiente)
        for i, tarea in enumerate(self.tareas):
            estado = "Completada" if tarea["completada"] else "Pendiente"
            print(f"{i+1}. {tarea['descripcion']} - {estado}")

    def eliminar_tarea(self, posicion):
        try:
            # Intenta eliminar la tarea en la posición especificada
            del self.tareas[posicion]
            print("Tarea eliminada correctamente.")
        except IndexError:
            # Captura el error si la posición especificada no existe en la lista de tareas
            print("La posición especificada no existe.")

def main():
    # Crea una instancia de la clase TareasPendientes
    tareas = TareasPendientes()

    while True:
        print("\nOpciones:")
        print("1. Agregar nueva tarea")
        print("2. Marcar tarea como completada")
        print("3. Mostrar todas las tareas")
        print("4. Eliminar tarea")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Solicita al usuario la descripción de la nueva tarea y la agrega a la lista
            tarea = input("Ingrese la descripción de la nueva tarea: ")
            tareas.agregar_tarea(tarea)
        elif opcion == "2":
            # Solicita al usuario la posición de la tarea a marcar como completada y lo hace
            posicion = int(input("Ingrese la posición de la tarea a marcar como completada: ")) - 1
            tareas.marcar_completada(posicion)
        elif opcion == "3":
            # Muestra todas las tareas pendientes
            tareas.mostrar_tareas()
        elif opcion == "4":
            # Solicita al usuario la posición de la tarea a eliminar y la elimina
            posicion = int(input("Ingrese la posición de la tarea a eliminar: ")) - 1
            tareas.eliminar_tarea(posicion)
        elif opcion == "5":
            # Sale del programa si el usuario elige esta opción
            print("¡Hasta luego!")
            break
        else:
            # Muestra un mensaje de error si el usuario ingresa una opción no válida
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
