import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Тест для маршрута /sum1n
def test_sum1n():
    response = client.get("/sum1n/10")
    assert response.status_code == 200
    assert response.json() == {"result": 55}

# Тест для маршрута /fibo
def test_fibo():
    response = client.get("/fibo?n=5")
    assert response.status_code == 200
    assert response.json() == {"result": 5}

# Тест для маршрута /reverse
def test_reverse():
    response = client.post("/reverse", headers={"string": "hello"})
    assert response.status_code == 200
    assert response.json() == {"result": "olleh"}

# Тест для маршрута /list (добавление элемента)
def test_add_to_list():
    response = client.put("/list", json={"element": "Apple"})
    assert response.status_code == 200
    assert response.json() == {"result": ["Apple"]}

# Тест для маршрута /list (получение элементов)
def test_get_list():
    response = client.get("/list")
    assert response.status_code == 200
    assert response.json() == {"result": ["Apple"]}

# Тест для маршрута /calculator (валидный запрос)
def test_calculator_valid():
    response = client.post("/calculator", json={"expr": "1,+,1"})
    assert response.status_code == 200
    assert response.json() == {"result": 2}

# Тест для маршрута /calculator (невалидный запрос)
def test_calculator_invalid():
    response = client.post("/calculator", json={"expr": "1,invalid,1"})
    assert response.status_code == 400
    assert response.json() == {"detail": "invalid"}

# Тест для маршрута /calculator (деление на ноль)
def test_calculator_div_by_zero():
    response = client.post("/calculator", json={"expr": "1,/,0"})
    assert response.status_code == 403
    assert response.json() == {"detail": "zerodiv"}

