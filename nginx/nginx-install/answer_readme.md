# Установка и обновление Nginx на CentOS/Almalinux

## Шаг 1: Установка Nginx
1. Чтобы установить Nginx:
    ```bash
    yum install nginx -y
    ```

2. Проверка версии Nginx:
    ```bash
    nginx -v
    ```
    результат:
    ```bash
    nginx version: nginx/1.20.1
    ```

## Шаг 2: Обновление Nginx
1. Обновим Nginx до самой последней версии:
    ```bash
    yum update nginx -y
    ```

2. Проверка версии, чтобы убедиться, что обновление выполнено успешно:
    ```bash
    nginx -v
    ```
    Результат:
    ```bash
    nginx version: nginx/1.26.2
    ```

## Шаг 3: Запуск Nginx
1. Запуск сервиса Nginx:
    ```bash
    systemctl start nginx
    ```

## Шаг 4: Проверка установки
1. Чтобы убедиться, что Nginx установлен и работает, сделаем:
    ```bash
    curl http://127.0.0.1
    ```

2. ответ:
    ```html
    <!DOCTYPE html>
    <html>
    <head>
    <title>Welcome to nginx!</title>
    <style>
    html { color-scheme: light dark; }
    body { width: 35em; margin: 0 auto;
    font-family: Tahoma, Verdana, Arial, sans-serif; }
    </style>
    </head>
    <body>
    <h1>Welcome to nginx!</h1>
    <p>If you see this page, the nginx web server is successfully installed and working. Further configuration is required.</p>
    <p>For online documentation and support please refer to <a href="http://nginx.org/">nginx.org</a>.<br/>
    Commercial support is available at <a href="http://nginx.com/">nginx.com</a>.</p>
    <p><em>Thank you for using nginx.</em></p>
    </body>
    </html>
    ```
