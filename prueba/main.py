from get_aves import request_aveschile
from aves_html_template import aves_template, html_template
# Solicitar datos de aves desde la API
aves_data = request_aveschile("https://aves.ninjas.cl/api/birds")    

# Función para generar HTML
def get_aves_chile():

    aves_html = ''  # Crear espacio para almacenar HTML de aves
    for bird in aves_data:
        aves_chile = aves_template.substitute(spanish_name=bird['name']['spanish'],
                                            english_name=bird['name']['english'],
                                            image_url=bird['images']['main'])
        aves_html += aves_chile
        
    # Crear el HTML 
    html = html_template.substitute(body=aves_html)

    with open('aves_chile.html', mode="w", encoding="utf-8") as f: # Escribir el HTML en un archivo llamado 'aves_chile.html'
        f.write(html)
        

# Llamar funcion para generar HTML
get_aves_chile()    

