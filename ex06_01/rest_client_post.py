import person_data as pdata
import ex06_01.person_dao as dao

print('ADDING NEW PERSON...')
person = pdata.get_random_person()
print(person)

new_person_id = dao.save_person(person)
print(f'New person id: {new_person_id}')