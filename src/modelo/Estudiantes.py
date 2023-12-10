from modelo.Conexion import conexion2023
from flask import jsonify, request 

def buscar_estudiante(codigo):
    try:
        conn = conexion2023()
        cur = conn.cursor()
        cur.execute("""select * FROM cliente WHERE id = %s""", (codigo,))
        datos = cur.fetchone()
        conn.close()
        if datos != None:
            usuario = {'identificador': datos[0], 'nombre': datos[1],
                       'apellido': datos[2], 'direccion': datos[3]}
            return usuario
        else:
            return None
    except Exception as ex:
            raise ex

class ModeloEstudiante():
    @classmethod
    def listar_Estudiante(self):
        
            conn = conexion2023()
            cursor=conn.cursor()
            cursor.execute("SELECT * FROM cliente")
            datos = cursor.fetchall()
            Estudiantes = []
            for fila in datos:
                estudiante = {'identificador': fila[0],
                       'nombre': fila[1],
                       'apellido': fila[2],
                       'direccion': fila[3]}
                Estudiantes.append(estudiante)
            conn.close()
            return jsonify({'usuarios': Estudiantes, 'mensaje': "Clientes listados.", 'exito': True})
    
    @classmethod
    def lista_Estudiante(self,codigo):
            usuario = buscar_estudiante(codigo)
            if usuario != None:
                return jsonify({'usuarios': usuario, 'mensaje': "cliente encontrado.", 'exito': True})
            else:
                return jsonify({'mensaje': "Usuario no encontrado.", 'exito': False})
    

    @classmethod
    def registrar_cliente(self):
            
            usuario = buscar_estudiante(request.json['identificador_e'])
            if usuario != None:
                return jsonify({'mensaje': "el identificador  ya existe, no se puede duplicar.", 'exito': False})
            else:
                conn = conexion2023()
                cur = conn.cursor()
                cur.execute('INSERT INTO cliente values(%s,%s,%s,%s)', (request.json['identificador_e'], request.json['nombre_e'], request.json['apellido_e'],
                                                                        request.json['direccion_e']))
                conn.commit()
                conn.close()
                return jsonify({'mensaje': "Usuario registrado.", 'exito': True})
   
    @classmethod
    def actualizar_cliente(self,codigo):
        try:
            usuario = buscar_estudiante(codigo)
            if usuario != None:
                conn = conexion2023()
                cur = conn.cursor()
                cur.execute("""UPDATE cliente SET nombre=%s, apellido=%s, direccion=%s
                WHERE id=%s""",
                        (request.json['nombre_e'], request.json['apellido_e'], request.json['direccion_e'], codigo))
                conn.commit()
                conn.close()
                return jsonify({'mensaje': "cliente actualizado.", 'exito': True})
            else:
                return jsonify({'mensaje': "cliente no encontrado.", 'exito': False})
        except Exception as ex:
                return jsonify({'mensaje': "Error", 'exito': False})
    

    @classmethod
    def eliminar_usuario(self,codigo):
        try:
            usuario = buscar_estudiante(codigo)
            if usuario != None:
                conn = conexion2023()
                cur = conn.cursor()
                cur.execute("DELETE FROM cliente WHERE id = %s", (codigo,))
                conn.commit()
                conn.close()
                return jsonify({'mensaje': "Usuario eliminado.", 'exito': True})
            else:
                return jsonify({'mensaje': "Usuario no encontrado.", 'exito': False})
        except Exception as ex:
            return jsonify({'mensaje': "Error", 'exito': False})