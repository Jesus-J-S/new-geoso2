#!/usr/bin/env python3
"""
Script para modificar un template HTML usando Jinja2
"""

import json
from jinja2 import Environment, FileSystemLoader, Template
from datetime import datetime
import os

def main():

    base_dir = os.path.dirname(os.path.abspath(__file__))
    templates_dir = os.path.join(base_dir, "templates")
    output_dir = os.path.join(base_dir, "output")
    os.makedirs(output_dir, exist_ok=True)

    os.makedirs("output", exist_ok=True)

    env = Environment(loader=FileSystemLoader("templates"))

    imagenes = [ "img/foto1.jpg", "img/foto2.png", "img/foto3.png", "img/foto4.jpg", "img/foto5.jpg", "img/foto6.jpg"]
    template_carrusel = env.get_template("carrusel.html")
    html_carrusel = template_carrusel.render(imagenes=imagenes)
    with open("output/carrusel.html", "w", encoding="utf-8") as f:
        f.write(html_carrusel)
    print("Carrusel generado: output/carrusel.html")
    # Leer el template
    with open('template.html', 'r', encoding='utf-8') as file:
        template_content = file.read()

    # Crear el objeto Template de Jinja2
    template = Template(template_content)

    # Leer datos desde el archivo JSON
    with open('datos.json', 'r', encoding='utf-8') as file:
        datos = json.load(file)

    # Agregar la fecha actual (se genera dinámicamente)
    datos['fecha'] = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

    # Renderizar el template con los datos
    html_generado = template.render(datos)

    # Guardar el resultado en output.html
    with open('output.html', 'w', encoding='utf-8') as file:
        file.write(html_generado)

    print('✓ Template procesado exitosamente')
    print('✓ Archivo generado: output.html')

if __name__ == '__main__':
    main()
