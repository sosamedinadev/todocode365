#Importar modulos necesarios
from nltk.chat.util import Chat, reflections

#Crear patrones de respuesta
patrones = [
    [r'Hola|Holi|buenas', ['Hola, como estas?', 'Buenas, que tal?']],
    [r'bien|genial|increible', ['Me alegro','Que bien']],
    [r'mal|triste', ['Lamento eso, me podrias contar el por que?', 'Lo lamento, por que estas asi?']],
    [r'mi nombre es (.*)',['Ohh %1, suena lindo, yo soy Emily una plantilla basica de chatbot creado para tus necesidades.']],
    [r'.*gracias|te agradezco', ['No es nada, aqui estoy para ti.']]
]

#Crear chatbot con el modulo Chat de la libreria NLTK
chatbot = Chat(patrones, reflections)

#Crear bucle conversacional
while True:
    entrada = input('Tu: ')
    #Condicion para romper el bucle
    if entrada.lower() == 'salir':
        break
    #Generar respuesta desde entrada
    respuesta = chatbot.respond(entrada)
    #Imprimir respuesta
    print(f'Chatbot: {respuesta}')