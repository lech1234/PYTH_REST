import sekcja06.cw01.person_dao as dao

print('DANE WSZYSTKICH OSÓB...')
persons = dao.get_persons()
for person in persons:
    print(person)

pid = int(input('WYBIERZ ID OSOBY: '))
person = dao.get_person_by_id(pid)

person['fname'] = input(f"Imię [{person['fname']}]? ") or person['fname']
person['lname'] = input(f"Nazwisko [{person['lname']}]? ") or person['lname']
person['age'] = input(f"Wiek [{person['age']}]? ") or person['age']
person['age'] = int(person['age'])
print(f'AKTUALIZACJA DANYCH OSOBY Z ID: {pid}')
dao.update_person(person)

print('DANE WSZYSTKICH OSÓB...')
persons = dao.get_persons()
for person in persons:
    print(person)
