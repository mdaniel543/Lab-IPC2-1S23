from flask import Flask, request, Response
from lxml import etree
import re

app = Flask(__name__)

def validar_email(email):
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(regex, email) is not None

def contar_palabras(mensaje):
    return len(mensaje.split())

def leer_usuarios_archivo():
    with open("usuarios.xml", "r") as archivo:
        return etree.parse(archivo).getroot()

def escribir_usuarios_archivo(usuarios):
    with open("usuarios.xml", "wb") as archivo:
        archivo.write(etree.tostring(usuarios.getroottree(), pretty_print=True))

def obtener_usuario_element(email, usuarios):
    for usuario in usuarios.findall("usuario"):
        if usuario.find("email").text == email:
            return usuario
    return None

@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    usuarios = leer_usuarios_archivo()
    return Response(etree.tostring(usuarios), content_type="application/xml")

@app.route('/usuarios/<string:email>', methods=['GET'])
def obtener_usuario(email):
    usuarios = leer_usuarios_archivo()
    usuario = obtener_usuario_element(email, usuarios)
    if usuario is not None:
        return Response(etree.tostring(usuario), content_type="application/xml")
    else:
        return "Usuario no encontrado", 404

@app.route('/usuarios', methods=['POST'])
def agregar_usuario():
    usuarios = leer_usuarios_archivo()
    try:
        nuevo_usuario = etree.fromstring(request.data)
    except Exception as e:
        return str(e), 400

    email = nuevo_usuario.find("email")
    if email is None:
        return "El email es requerido", 400
    
    if obtener_usuario_element(email.text, usuarios) is not None:
        return "El usuario ya existe", 400
    
    email_valido = validar_email(email.text)
    email_resultado = "correcto" if email_valido else "incorrecto"
    
        # Contar palabras del mensaje
    conteo_mensaje = contar_palabras(nuevo_usuario.find("mensaje").text)

    usuarios.append(nuevo_usuario)
    escribir_usuarios_archivo(usuarios)
    
    respuesta = f"""
        <respuesta>
            <email>{email_resultado}</email>
            <mensaje>{conteo_mensaje}</mensaje>
        </respuesta>
        """

    return Response(respuesta, content_type='application/xml')


@app.route('/usuarios/<string:email>', methods=['PUT'])
def actualizar_usuario(email):
    usuarios = leer_usuarios_archivo()
    try:
        datos_actualizados = etree.fromstring(request.data)
    except Exception as e:
        return str(e), 400

    usuario = obtener_usuario_element(email, usuarios)
    if usuario is None:
        return "Usuario no encontrado", 404

    for dato in datos_actualizados:
        usuario.find(dato.tag).text = dato.text

    escribir_usuarios_archivo(usuarios)
    return "Usuario actualizado con éxito"



@app.route('/usuarios/<string:email>', methods=['DELETE'])
def eliminar_usuario(email):
    usuarios = leer_usuarios_archivo()
    usuario = obtener_usuario_element(email, usuarios)
    if usuario is None:
        return "Usuario no encontrado", 404

    usuarios.remove(usuario)
    escribir_usuarios_archivo(usuarios)
    return "Usuario eliminado con éxito"

if __name__ == '__main__':
    app.run(debug=True)