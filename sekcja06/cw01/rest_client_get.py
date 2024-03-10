import sekcja06.cw01.person_dao as dao

print('DANE WSZYSTKICH OSÓB...')
persons = dao.get_persons()
for person in persons:
    print(person)

if persons:
    pid = int(input('Wybierz id: '))
    print(f'DANE OSOBY Z ID: {pid}')
    person = dao.get_person_by_id(pid)
    print(person)
else:
    print('Brak danych')