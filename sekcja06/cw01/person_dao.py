import requests

# gdy uruchomimy sekcja05.cw01.serwer.py:
__base_url = 'http://127.0.0.1:5000/persons/'


# metoda GET: pobieranie zasobów
# URI: /
def get_persons() -> list[dict]:
    headers = {'Accept': 'application/json'}

    response = requests.get(url=__base_url, headers=headers)
    response.raise_for_status()
    return response.json()


# metoda GET: pobieranie zasobów
# URI: /<person_id>
def get_person_by_id(person_id: int) -> dict:
    get_url = __base_url + str(person_id)
    headers = {'Accept': 'application/json'}

    response = requests.get(url=get_url, headers=headers)
    response.raise_for_status()
    return response.json()


# metoda POST - dodawanie zasobów
# URI: /
def save_person(data: dict) -> int:
    headers = {'Content-Type': 'application/json'}

    response = requests.post(url=__base_url, headers=headers, json=data)
    response.raise_for_status()
    url, pid = response.headers['Location'].rsplit('/', maxsplit=1)
    return int(pid)


# metoda DELETE - usuwanie zasobów
# URI: /<person_id>
def delete_person_by_id(person_id: int) -> None:
    del_url = __base_url + str(person_id)

    response = requests.delete(url=del_url)
    response.raise_for_status()


# metoda PUT - aktualizacja zasobów
# URI: /
def update_person(data: dict):
    headers = {'Content-Type': 'application/json'}

    response = requests.put(url=__base_url, headers=headers, json=data)
    response.raise_for_status()
    return response
