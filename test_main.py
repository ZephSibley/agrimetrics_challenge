from fastapi.testclient import TestClient
from datetime import timedelta

from main import app
from main import SCHEDULE

client = TestClient(app)

# TODO: Mock out the SCHEDULE list out so we're not testing global state


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_read_schedule():
    response = client.get("/schedule")
    assert response.status_code == 200
    assert response.json() == {"schedule": []}


def test_read_order():
    response = client.get("/order")
    assert response.status_code == 200
    assert response.json() == {"message": "OK"}
    assert len(SCHEDULE) == 3
    assert SCHEDULE[-1][1] == 'Take a break'
    assert SCHEDULE[-1][0] - SCHEDULE[-2][0] == timedelta(seconds=60)
    assert SCHEDULE[-2][0] - SCHEDULE[-3][0] == timedelta(seconds=150)


def test_read_order_again():
    response = client.get("/order")
    assert response.status_code == 200
    assert response.json() == {"message": "OK"}
    assert len(SCHEDULE) == 5
    assert SCHEDULE[-1][1] == 'Take a break'
    assert SCHEDULE[-1][0] - SCHEDULE[-2][0] == timedelta(seconds=60)
    assert SCHEDULE[-2][0] - SCHEDULE[-3][0] == timedelta(seconds=150)
    assert SCHEDULE[-4][1] != 'Take a break'
    assert SCHEDULE[-3][0] - SCHEDULE[-4][0] == timedelta(seconds=60)


def test_read_schedule_with_orders():
    response = client.get("/schedule")
    assert response.status_code == 200
    schedule = response.json()['schedule']
    assert type(schedule) == list
    assert len(schedule) == 5
