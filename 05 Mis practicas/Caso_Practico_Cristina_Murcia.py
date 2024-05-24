class TareasPendientes:
    def __init__(self):
        # Se inicializa la lista de tareas pendientes
        self.tareas = []

    def agregar_tarea(self, tarea):
        # Aquí se agrega una nueva tarea a la lista de tareas pendientes
        self.tareas.append({"descripcion": tarea, "completada": False})

    def marcar_completada(self, posicion):
        try:
            # Para marcar como completada la tarea en la posición especificada
            self.tareas[posicion]["completada"] = True
            print("Tarea marcada como completada.")
        except IndexError:
            # Si la posición especificada no existe en la lista de tareas devuelve un error
            print("La posición especificada no existe.")

    def mostrar_tareas(self):
        print("\nTareas pendientes:\n")
        # Imprime mostrando el estado (completada o pendiente)
        for i, tarea in enumerate(self.tareas):
            estado = "Completada" if tarea["completada"] else "Pendiente"
            print(f"{i+1}. {tarea['descripcion']} - {estado}")

    def eliminar_tarea(self, posicion):
        try:
            # Elimina la tarea en la posición especificada
            del self.tareas[posicion]
            print("Tarea eliminada correctamente.")
        except IndexError:
            # Captura el error si la posición especificada no existe en la lista de tareas
            print("La posición especificada no existe.")

def main():
    # Crea una instancia de la clase TareasPendientes
    tareas = TareasPendientes()

    while True:
        print("\n =======================================")
        print("\n    CASO PRACTICO CRISTINA MURCIA      ")
        print("\n =======================================\n")
        print("\nOpciones:")
        print("1. Agregar nueva tarea")
        print("2. Marcar tarea como completada")
        print("3. Mostrar todas las tareas")
        print("4. Eliminar tarea")
        print("5. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            # Solicita al usuario la descripción de la nueva tarea y la agrega a la lista
            tarea = input("Ingrese la descripción de la nueva tarea: ")
            tareas.agregar_tarea(tarea)
            
        elif opcion == "2":
            # Solicita al usuario la posición de la tarea a marcar como completada
            posicion = int(input("Ingrese la posición de la tarea a marcar como completada: ")) - 1
            tareas.marcar_completada(posicion)
        elif opcion == "3":
            # Muestra todas las tareas pendientes
            tareas.mostrar_tareas()
        elif opcion == "4":
            # Solicita  la posición de la tarea a eliminar y la elimina
            posicion = int(input("Ingrese la posición de la tarea a eliminar: ")) - 1
            tareas.eliminar_tarea(posicion)
        elif opcion == "5":
            # Sale del programa si se elige esta opción
            print("\nHas salido del programa")
            print("\n!Hasta la vista!\n")
            break
        else:
            # Muestra un mensaje de error si se ingresa una opción no válida
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
