from fastapi import FastAPI, Request
from prometheus_client import Counter, Histogram, Gauge, generate_latest, REGISTRY
import time

app = FastAPI()

# Метрика типа Counter для подсчета HTTP-запросов
http_requests_total = Counter(
    "http_requests_total", 
    "Number of HTTP requests received", 
    ["method", "endpoint"]
)

# Метрика типа Histogram для измерения времени запросов
http_requests_milliseconds = Histogram(
    "http_requests_milliseconds", 
    "Duration of HTTP requests in milliseconds", 
    ["method", "endpoint"]
)

# Метрика типа Gauge для хранения последнего результата sum1n
last_sum1n = Gauge(
    "last_sum1n", 
    "Value stores last result of sum1n"
)

# Метрика типа Gauge для хранения последнего результата fibo
last_fibo = Gauge(
    "last_fibo", 
    "Value stores last result of fibo"
)

# Метрика типа Gauge для размера списка
list_size = Gauge(
    "list_size", 
    "Value stores current list size"
)

# Метрика типа Gauge для последнего результата калькулятора
last_calculator = Gauge(
    "last_calculator", 
    "Value stores last result of calculator"
)

# Метрика типа Counter для ошибок калькулятора
errors_calculator_total = Counter(
    "errors_calculator_total", 
    "Number of errors in calculator"
)

# Пример функции для маршрута /sum1n
@app.post("/sum1n")
async def sum1n(request: Request):
    data = await request.json()
    num1 = data.get("num1")
    num2 = data.get("num2")
    
    try:
        result = num1 + num2
        last_sum1n.set(result)  # Обновляем метрику с последним результатом
    except Exception as e:
        errors_calculator_total.inc()  # Увеличиваем счетчик ошибок
        return {"error": str(e)}
    
    return {"result": result}

# Пример функции для маршрута /fibo
@app.post("/fibo")
async def fibo(request: Request):
    data = await request.json()
    n = data.get("n")
    
    try:
        result = fibonacci(n)
        last_fibo.set(result)  # Обновляем метрику с последним результатом
    except Exception as e:
        errors_calculator_total.inc()  # Увеличиваем счетчик ошибок
        return {"error": str(e)}
    
    return {"result": result}

# Пример функции для вычисления числа Фибоначчи
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Экспортер метрик на /metrics
@app.get("/metrics")
async def metrics():
    return generate_latest(REGISTRY)

# Middleware для отслеживания запросов
@app.middleware("http")
async def track_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    method = request.method
    endpoint = request.url.path

    # Увеличиваем счетчик запросов
    http_requests_total.labels(method=method, endpoint=endpoint).inc()
    
    # Измеряем время запроса
    duration = (time.time() - start_time) * 1000  # Время в миллисекундах
    http_requests_milliseconds.labels(method=method, endpoint=endpoint).observe(duration)

    return response

