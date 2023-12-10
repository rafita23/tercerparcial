from flask import Flask
from decouple import config
from modelo.Estudiantes import ModeloEstudiante
from config import config


app = Flask(__name__)

# RUTA PARA PETICION GET

@app.route("/")
def hello_world():
    return  "  hola mundo Rafael"
#mostrar todos los clientes
@app.route("/estudiantes", methods=['GET'])
def listar_estudiantes():
    resul=ModeloEstudiante.listar_Estudiante()
    return resul

#buscar un solo cliente
@app.route("/estudiantes/:<codigo>", methods=['GET'])
def lista_estudiante(codigo):
    resul=ModeloEstudiante.lista_Estudiante(codigo)
    return resul


@app.route("/estudiantes", methods=['POST'])
def guardar_estudiantes():
    resul=ModeloEstudiante.registrar_cliente()
    return resul

##actualizar
@app.route("/estudiantes/:<codigo>", methods=['PUT'])
def actualizar_estudiantes(codigo):
    resul=ModeloEstudiante.actualizar_cliente(codigo)
    return resul

##eliminar
@app.route("/estudiantes/:<codigo>", methods=['DELETE'])
def elimnar_estudiantes(codigo):
    resul=ModeloEstudiante.eliminar_usuario(codigo)
    return resul

def pag_noencontrada(error):
    return "<h1>NO SE ENCONTRÓ NING PAG. RAFA :( </h1>",404



if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404,pag_noencontrada)
    app.run(host='0.0.0.0',debug=True)