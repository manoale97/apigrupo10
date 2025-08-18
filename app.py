from flask import Flask, jsonify, request
from datetime import datetime
import random

app = Flask(__name__)

##diccionario con las frases predeterminadas
frases_galleta = {
    "Enero": {
        "Frase 1": "Cada amanecer es una página en blanco, escribe en ella tus mejores intenciones.",
        "Frase 2": "El entusiasmo con el que inicias será la energía que te acompañe todo el año."
    },
    "Febrero": {
        "Frase 1": "El amor no solo se da, también se cultiva dentro de ti.",
        "Frase 2": "Un gesto de bondad puede cambiar el día de alguien… y el tuyo también."
    },
    "Marzo": {
        "Frase 1": "La acción es el puente entre tus sueños y la realidad.",
        "Frase 2": "Los pequeños pasos diarios construyen grandes caminos."
    },
    "Abril": {
        "Frase 1": "Así como la lluvia nutre la tierra, los desafíos nutren tu crecimiento.",
        "Frase 2": "No temas a los cambios, ellos son la raíz de tus oportunidades."
    },
    "Mayo": {
        "Frase 1": "Tu constancia será el motor que mueva tus metas.",
        "Frase 2": "El esfuerzo invisible es el que más frutos dará."
    },
    "Junio": {
        "Frase 1": "Escucha a tu corazón, él te dirá lo que la razón calla.",
        "Frase 2": "Tu creatividad florece cuando te permites experimentar."
    },
    "Julio": {
        "Frase 1": "Celebra tus logros, por pequeños que parezcan.",
        "Frase 2": "La energía positiva que entregas siempre regresa multiplicada."
    },
    "Agosto": {
        "Frase 1": "La disciplina hoy es la libertad del mañana.",
        "Frase 2": "El silencio también tiene respuestas, aprende a escucharlo."
    },
    "Septiembre": {
        "Frase 1": "Cada aprendizaje es una semilla de sabiduría que florecerá en el futuro.",
        "Frase 2": "No midas tu camino con la vara de otros, avanza a tu ritmo."
    },
    "Octubre": {
        "Frase 1": "Tu imaginación es la chispa que enciende nuevas oportunidades.",
        "Frase 2": "Atrévete a salir de la rutina, ahí nace la magia."
    },
    "Noviembre": {
        "Frase 1": "Ser agradecido convierte lo que tienes en suficiente.",
        "Frase 2": "El valor está en reconocer lo bueno incluso en los días grises."
    },
    "Diciembre": {
        "Frase 1": "Cierra el año con gratitud y abrirás el siguiente con abundancia.",
        "Frase 2": "Cada final es en realidad un nuevo inicio disfrazado."
    }
}

## get principal para la API
@app.route('/')
def home():
    return jsonify({'message': 'Bienvenido a la API de galletas de la fortuna'})

## metodo POST para obtener las frases 
@app.route('/api/abrirGalleta', methods=['POST'])
def abrirGalleta():
    data =request.get_json()
    nombre = data.get('nombre')
    ## fecha actual
    fecha = datetime.now()
    if nombre is None:
        return jsonify({'error': 'Faltan datos para obtener su fortuna'}), 400
    # Obtener el mes actual en español
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    mes_actual = meses[fecha.month - 1]
    frases_mes = frases_galleta.get(mes_actual, {})
    if not frases_mes:
        return jsonify({'error': 'No hay frases para este mes'}), 404
    frase = random.choice(list(frases_mes.values()))
    return jsonify({
        'nombre': nombre,
        'mes': mes_actual,
        'frase': frase,
        'resultado': 'Hola ' + nombre + ', tu galleta de la fortuna dice: ' + frase
    })

## metodo put para actualizar la lista de frases
@app.route('/api/actualizarFrases', methods=['PUT'])
def actualizarFrases():
    data = request.get_json()
    mes = data.get('mes')
    nuevas_frases = data.get('frases')
    if mes is None or nuevas_frases is None:
        return jsonify({'error': 'Faltan datos para actualizar las frases'}), 400
    if mes not in frases_galleta:
        return jsonify({'error': 'Mes no encontrado'}), 404
    frases_galleta[mes] = nuevas_frases
    return jsonify({'message': 'Frases actualizadas correctamente'}), 200

## metodo delete para borrar alguna frase
@app.route('/api/borrarFrase', methods=['DELETE'])
def borrarFrase():
    data = request.get_json()
    mes = data.get('mes')
    frase = data.get('frase')
    if mes is None or frase is None:
        return jsonify({'error': 'Faltan datos para borrar la frase'}), 400
    if mes not in frases_galleta:
        return jsonify({'error': 'Mes no encontrado'}), 404
    frases_mes = frases_galleta[mes]
    if frase not in frases_mes.values():
        return jsonify({'error': 'Frase no encontrada'}), 404
    # Borrar la frase
    for key, value in list(frases_mes.items()):
        if value == frase:
            del frases_mes[key]
            break
    return jsonify({'message': 'Frase borrada correctamente'}), 200

## metodo para crear una nueva frase
@app.route('/api/crearFrase', methods=['POST'])
def crearFrase():
    data = request.get_json()
    mes = data.get('mes')
    frase = data.get('frase')
    if mes is None or frase is None:
        return jsonify({'error': 'Faltan datos para crear la frase'}), 400
    if mes not in frases_galleta:
        frases_galleta[mes] = {}
    # Crear una nueva frase con un ID único
    id_nueva_frase = len(frases_galleta[mes]) + 1
    frases_galleta[mes][f'Frase {id_nueva_frase}'] = frase
    return jsonify({'message': 'Frase creada correctamente'}), 201

## metodo get para obtener todas las frases
@app.route('/api/obtenerFrases', methods=['GET'])
def obtenerFrases():
    return jsonify(frases_galleta), 200

## metodo get simplificado para que un invitado sin nombre pueda obtener su frase
@app.route('/api/obtenerFraseInvitado', methods=['GET'])
def obtenerFraseInvitado():
    # Obtener la fecha actual
    fecha = datetime.now()
    # Obtener el mes actual en español
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    mes_actual = meses[fecha.month - 1]
    frases_mes = frases_galleta.get(mes_actual, {})
    if not frases_mes:
        return jsonify({'error': 'No hay frases para este mes'}), 404
    frase = random.choice(list(frases_mes.values()))
    return jsonify({
        'mes': mes_actual,
        'frase': frase,
        'resultado': 'Tu galleta de la fortuna dice: ' + frase
    })
