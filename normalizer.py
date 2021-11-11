import os
import codecs
from nltk.corpus import stopwords
from cleaner import listado_palabras_vacias
import nltk
nltk.download('stopwords')

palabrasv = stopwords.words('spanish')
palabrasvac = listado_palabras_vacias()

try:
    directorio_normalizado = os.makedirs('normalizados', exist_ok=True)
except OSError:
    print('Error al crear el directorio normalizado')

# listar todos los archivos en el directorio
for nombre_archivo in os.listdir('textos'):
    if not os.path.isdir(os.path.join('normalizados', nombre_archivo)):
        # abrir el archivo
        with codecs.open(os.path.join('textos', nombre_archivo), 'r', encoding='utf-8', errors='replace') as archivo:
            # leer el archivo
            contenido = archivo.read().replace('\n', ' ').replace(',', '').replace('.', '')
            # normalizar el contenido
            contenido = contenido.lower()
            # split the content
            contenido = contenido.split()
            # limpiar signos de puntuación
            contenido = [palabra.strip('.,:;!¡?¿') for palabra in contenido]
            contenido = [palabra for palabra in contenido if palabra.isalpha()]
            # remove stopwords
            contenido = [
                palabra for palabra in contenido if palabra not in palabrasv]

            contenido = [
                palabra for palabra in contenido if palabra not in palabrasvac]
            # join the content
            contenido = ' '.join(contenido)

            # crear el archivo normalizado
            with open(os.path.join('normalizados', nombre_archivo), 'w', encoding='utf-8') as archivo_normalizado:
                archivo_normalizado.write(contenido)
                print('Archivo normalizado: ' + nombre_archivo)
                archivo_normalizado.close()
