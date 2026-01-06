from fastapi.testclient import TestClient

from api.main import app

client = TestClient(app)


#testear gets
def test_read_laptop_by_id():
    response = client.get("/laptop/10")
    assert response.status_code == 200

def test_read_by_max_price():
    response = client.get("/laptop/precio/10")
    assert response.status_code == 404
    assert response.json() == {"error":"Laptop price not found"}

def test_post_success():
    response = client.post(url="/laptop",
                           headers={"Content-Type": "application/json"},
                           json={"modelo": "modelo ty",
                                 "precio": 800,
                                 "OS": "windows",
                                 "marca": "apple"
                               })

    assert response.status_code == 200

def test_post_failure():
    response = client.post(url="/laptop",
                           headers={"Content-Type": "application/json"},
                           json={"modelo": "modelo ty",
                                 "precio": 800,
                                 "OS": "windows"
                               })
    
    assert response.status_code == 422

def test_delete_success():
    response = client.delete("laptop/?laptop_id=1005")
    assert response.status_code == 200


def test_delete_failure():
    response = client.delete("laptop/?laptop_id=1")
    assert response.status_code == 404