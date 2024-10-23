# Nginx Config
## Конфигурация Nginx

```bash
server {
    listen 8080;  # Nginx слушает порт 8080
    server_name example.com;  # Доменное имя сервера

    location / {
        root /var/www/html;  # Корневая директория для основного контента
        index index.html;  # Файл по умолчанию для отдачи, если нет запроса на конкретный файл
    }

    location /images/ {
        alias /var/www/images/;  # Директория для изображений
    }

    location /gifs/ {
        alias /var/www/gifs/;  # Директория для gif-изображений
    }

    location /secret_word {
        return 201 'jusan-nginx-locations';  # Возвращает строку 'jusan-nginx-locations'
        add_header Content-Type text/plain;  # Добавляет заголовок с указанием текстового контента
    }
}


##проведение команды curl и его ответ
```bash
curl -H "Host: example.com" -i http://localhost:8080/secret_word
HTTP/1.1 201 Created
Server: nginx/1.26.2
Date: Tue, 22 Oct 2024 11:43:06 GMT
Content-Type: application/octet-stream
Content-Length: 21
Connection: keep-alive
Content-Type: text/plain

jusan-nginx-locations

##При выполнении команды curl:
```bash
curl -H "Host: example.com" http://localhost:8080/

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cats Page</title>
</head>

<body>
    <p>
    <h1>Cat with Flower</h1>
    <img src="/images/flower.png" alt="flower">
    </p>

    <p>
    <h1>Cat with Glasses</h1>
    <img src="/images/glasses.png" alt="glasses">
    </p>

    <p>
    <h1>Gray Cat</h1>
    <img src="/images/gray-animal.jpeg" alt="gray-animal">
    </p>

    <p>
    <h1>Cats mafia</h1>
    <img src="/images/mafia.png" alt="mafia">
    </p>

    <p>
    <h1>Sleepy Cat</h1>
    <img src="/images/sleep.png" alt="sleep">
    </p>
</body>

</html>





