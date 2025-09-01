from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_and_get_task():
    payload = {"title": "Test", "description": "Desc", "status": "created"}
    r = client.post("/tasks/", json=payload)
    assert r.status_code == 201
    data = r.json()
    assert "uuid" in data
    tid = data["uuid"]

    r2 = client.get(f"/tasks/{tid}")
    assert r2.status_code == 200
    assert r2.json()["title"] == "Test"


def test_list_tasks():
    client.post("/tasks/", json={"title": "L", "description": "", "status": "created"})
    r = client.get("/tasks/")
    assert r.status_code == 200
    assert isinstance(r.json(), list)


def test_update_task():
    r = client.post("/tasks/", json={"title": "A", "description": "", "status": "created"})
    tid = r.json()["uuid"]

    r2 = client.put(f"/tasks/{tid}", json={"status": "in_progress", "title": "AA"})
    assert r2.status_code == 200
    body = r2.json()
    assert body["status"] == "in_progress"
    assert body["title"] == "AA"


def test_delete_task_and_404_after():
    r = client.post("/tasks/", json={"title": "D", "description": "", "status": "created"})
    tid = r.json()["uuid"]

    r2 = client.delete(f"/tasks/{tid}")
    assert r2.status_code == 204

    r3 = client.get(f"/tasks/{tid}")
    assert r3.status_code == 404
    assert r3.json()["detail"] == "Task not found"


def test_not_found_cases():
    missing = "00000000-0000-0000-0000-000000000000"
    assert client.get(f"/tasks/{missing}").status_code == 404
    assert client.put(f"/tasks/{missing}", json={"title": "x"}).status_code == 404
    assert client.delete(f"/tasks/{missing}").status_code == 404
