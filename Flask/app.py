from flask import Flask, jsonify, request

app = Flask(__name__)

usuarios = {}

@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    return jsonify(usuarios)


@app.route('/usuarios', methods=['POST'])
def agregar_usuarios():
    nuevo_usuario = request.get_json()
    print(nuevo_usuario)

    if "email" not in nuevo_usuario:
        return "El email es requerido", 400

    email = nuevo_usuario["email"]
    if email in usuarios:
        return "El usuario ya existe", 400
    
    usuarios[email] = nuevo_usuario
    return "Usuario agregado con éxito", 201



@app.route('/usuarios/<string:email>', methods=['PUT'])
def actualizar_usuario(email):
    datos_actualizados = request.get_json()

    if email not in usuarios:
        return "Usuario no encontrado", 404

    usuario = usuarios[email]
    usuario.update(datos_actualizados)
    return "Usuario actualizado con éxito"



@app.route('/usuarios/<string:email>', methods=['DELETE'])
def eliminar_usuario(email):
    if email not in usuarios:
        return "Usuario no encontrado", 404

    del usuarios[email]
    return "Usuario eliminado con éxito"



if __name__ == '__main__':
    app.run()