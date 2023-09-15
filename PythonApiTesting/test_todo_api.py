import requests
ENDPOINT = "https://todo.pixegami.io/"

response = requests.get(ENDPOINT)
print(response)

data = response.json()
status = response.status_code
print(data)
print(status)\

def test_can_call_endpoint():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200
def test_can_create_task():
    p1 = payload_create()
    p2 = payload_update()
    response = requests.put(ENDPOINT+"/create-task", json = p1)
    assert response.status_code == 200
    data = response.json()
    print(data)
    task = data["task"]["task_id"]
    print(task)

    get_task_response = requests.get(ENDPOINT+f"/get-task/{task}")
    assert get_task_response.status_code == 200
    get_task_data =  get_task_response.json()
    assert get_task_data["content"] == p1["content"]
    assert get_task_data["user_id"] == p1["user_id"]

    update_task_new = update_task(p2)
    assert update_task_new.status_code == 200


def create_task(payload):
    return requests.put(ENDPOINT+"/create-task", json = payload)

def update_task(payload):
    return requests.put(ENDPOINT+"/update-task", json = payload)


def payload_create():
    p = {
    "content": "myfake content",
    "user_id": "1234Stark",
    "task_id": "Faketask",
    "is_done": False
    }
    return p
def payload_update():
    p = {
    "content": "myfake content",
    "user_id": "1234Stark",
    "task_id": "Faketask1",
    "is_done": False
    }
    return p
