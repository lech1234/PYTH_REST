import person_data as pdata
import sekcja06.cw01.person_dao as dao

print('DODAWANIE NOWEJ OSOBY...')
person = pdata.get_random_person()
print(person)

new_person_id = dao.save_person(person)
print(f'NOWA OSOBA OTRZYMAŁA ID: {new_person_id}')