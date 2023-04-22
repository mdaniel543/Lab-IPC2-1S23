from flask import Flask, request, Response
from lxml import etree

app = Flask(__name__)

# Almacenamiento de usuarios utilizando un objeto ElementTree
usuarios = etree.Element("usuarios")

def obtener_usuario_element(email):
    for usuario in usuarios.findall("usuario"):
        if usuario.find("email").text == email:
            return usuario
    return None


@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    return Response(etree.tostring(usuarios), content_type="application/xml")



@app.route('/usuarios', methods=['POST'])
def agregar_usuario():
    try:
        nuevo_usuario = etree.fromstring(request.data)
    except Exception as e:
        return str(e), 400

    email = nuevo_usuario.find("email")
    if email is None:
        return "El email es requerido", 400

    if obtener_usuario_element(email.text) is not None:
        return "El usuario ya existe", 400

    usuarios.append(nuevo_usuario)
    return "Usuario agregado con éxito", 201


@app.route('/usuarios/<string:email>', methods=['PUT'])
def actualizar_usuario(email):
    try:
        datos_actualizados = etree.fromstring(request.data)
    except Exception as e:
        return str(e), 400

    usuario = obtener_usuario_element(email)
    if usuario is None:
        return "Usuario no encontrado", 404

    for dato in datos_actualizados:
        usuario.find(dato.tag).text = dato.text

    return "Usuario actualizado con éxito"



@app.route('/usuarios/<string:email>', methods=['DELETE'])
def eliminar_usuario(email):
    usuario = obtener_usuario_element(email)
    if usuario is None:
        return "Usuario no encontrado", 404

    usuarios.remove(usuario)
    return "Usuario eliminado con éxito"



if __name__ == '__main__':
    app.run(debug=True)