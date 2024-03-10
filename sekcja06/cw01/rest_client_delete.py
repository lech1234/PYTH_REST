import sekcja06.cw01.person_dao as dao

print('DANE WSZYSTKICH OSÓB...')
persons = dao.get_persons()
for person in persons:
    print(person)

pid = int(input('Podaj id osoby do usunięcia: '))
print(f'USUWANIE OSOBY Z ID: {pid}...')
dao.delete_person_by_id(pid)

print('DANE WSZYSTKICH OSÓB...')
persons = dao.get_persons()
for person in persons:
    print(person)
