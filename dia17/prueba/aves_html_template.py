from string import Template

aves_template = Template('''<div class="item">
                            <h3>$spanish_name</h3>
                            <h3>$english_name</h3>
                            <img src="$image_url">
                            <hr>
                            </div>
                        ''')

html_template = Template('''<!DOCTYPE html>
                            <html lang="es">
                            <head>
                            <meta charset="utf-8">
                            <meta http-equiv=”Content-Type” content=”text/html />
                            <meta name="viewport" content="width=device-width, initial-scale=1.0">
                            <title>Aves de Chile</title>
                            <style>
                            .contenedor {
                            display: inline-block;    
                            }
                            .titulo {
                                text-align: center;
                                }
                            .item {
                                display: inline-block;    
                                text-align: justify;
                                }
                            .item hr{
                                color: rgb(241, 241, 241);
                            }    
                            
                            .item img{
                            width: 320px;
                            height: 320px;
                            margin: 5px;
                            }
                            </style>
                            </head>
                            <h1 class="titulo">Aves de Chile</h1>
                            <div class="contenedor">
                            $body
                            </div>
                            </body></html>''')

