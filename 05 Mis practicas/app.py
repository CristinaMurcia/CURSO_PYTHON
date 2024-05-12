from flask import Flask, render_template, request

app = Flask(__name__)

class TareasPendientes:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append({"descripcion": tarea, "completada": False})

    def marcar_completada(self, posicion):
        try:
            self.tareas[posicion]["completada"] = True
        except IndexError:
            pass

    def mostrar_tareas(self):
        return self.tareas

    def eliminar_tarea(self, posicion):
        try:
            del self.tareas[posicion]
        except IndexError:
            pass

tareas = TareasPendientes()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form['action'] == 'agregar':
            tarea = request.form['tarea']
            tareas.agregar_tarea(tarea)
        elif request.form['action'] == 'marcar':
            posicion = int(request.form['posicion'])
            tareas.marcar_completada(posicion)
        elif request.form['action'] == 'eliminar':
            posicion = int(request.form['posicion'])
            tareas.eliminar_tarea(posicion)
    return render_template('index.html', tareas=tareas.mostrar_tareas())

if __name__ == '__main__':
    app.run(debug=True)
