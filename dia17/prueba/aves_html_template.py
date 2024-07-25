from string import Template

aves_template = Template('''
    <div class="bird-card">
        <img src="$image_url" alt="$spanish_name">
        <div class="bird-info">
            <h3 class="spanish-name">$spanish_name</h3>
            <p class="english-name">$english_name</p>
        </div>
    </div>
''')

html_template = Template('''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aves de Chile</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');
        
        body {
            font-family: 'Roboto', sans-serif;
            background-color: #f0f0f0;
            background-image: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23000000' fill-opacity='0.05'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
            margin: 0;
            padding: 0;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        
        h1 {
            text-align: center;
            color: #2c3e50;
            font-size: 2.5em;
            margin-bottom: 30px;
        }
        
        .bird-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 20px;
        }
        
        .bird-card {
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            overflow: hidden;
            transition: transform 0.3s ease;
        }
        
        .bird-card:hover {
            transform: translateY(-5px);
        }
        
        .bird-card img {
            width: 100%;
            height: 200px;
            object-fit: cover;
            transition: transform 0.3s ease;
        }
        
        .bird-card:hover img {
            transform: scale(1.1);
        }
        
        .bird-info {
            padding: 15px;
        }
        
        .spanish-name {
            margin: 0;
            color: #2c3e50;
            font-size: 1.2em;
        }
        
        .english-name {
            margin: 5px 0 0;
            color: #7f8c8d;
            font-size: 0.9em;
            font-style: italic;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Aves de Chile</h1>
        <div class="bird-grid">
            $body
        </div>
    </div>
</body>
</html>
''')