<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Hello World</title>
</head>
<body>
    <h1 style="color:red">Hello World</h1>
    <ul>
        {% for pr in product %}
            <li>
                {{ pr.name }} | 
                {{ pr.description }}
            </li>
        {% endfor %}
    </ul>
</body>
</html>
