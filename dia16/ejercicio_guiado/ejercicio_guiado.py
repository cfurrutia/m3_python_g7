import requests
import json
from string import Template
img_template = Template('<img src="$url">')

def request_get(url):
    return json.loads(requests.get(url).text)
out = request_get('https://jsonplaceholder.typicode.com/photos')[:5]
print(len(out))

print(out[0].keys())    # dict_keys(['albumId', 'id', 'title', 'url', 'thumbnailUrl'])

print(out[0]) # {'albumId': 1, 'id': 1, 'title': 'accusamus beatae ad facilis cum similique qui sunt',
#'url': 'https://via.placeholder.com/600/92c952', 'thumbnailUrl': 'https://via.placeholder.com/150/92c952'} 

imagen = img_template.substitute(url = 'hola')
print(imagen)

html_template = Template('''<!DOCTYPE html>
<html>
<head>
<title>Título de la Página</title>
</head>
<body>
<h1>Nuestra página Web</h1>
$body
</body>
</html>
''')

lista_url = [elemento['url'] for elemento in out]
texto_img = ''
for url in lista_url:
    texto_img += img_template.substitute(url = url)+'\n'
print(texto_img)




