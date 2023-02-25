import ex06_01.person_dao as dao

print('GETTING ALL PERSONS...')
persons = dao.get_persons()
for person in persons:
    print(person)

pid = int(input('Choose id: '))
print(f'GETTING PERSON WITH id: {pid}')
person = dao.get_person_by_id(pid)
print(person)
