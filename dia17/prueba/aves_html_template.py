from string import Template

aves_template = Template('''<h2>$spanish_name</h2>
                            <h3>$english_name</h3>
                            <img src="$image_url">
                        ''')

html_template = Template('''<!DOCTYPE html>
                            <html lang="es">
                            <head>
                            <meta charset="utf-8">
                            <meta http-equiv=”Content-Type” content=”text/html />
                            <meta name="viewport" content="width=device-width, initial-scale=1.0">
                            <title>Aves de Chile</title>
                            </head><body><h1 align="center">Aves de Chile</h1>
                            $body
                            </body></html>''')

