import ex06_01.person_dao as dao

print('GETTING ALL PERSONS...')
persons = dao.get_persons()
for person in persons:
    print(person)

pid = int(input('Choose id: '))
person = dao.get_person_by_id(pid)

person['fname'] = input(f"First name [{person['fname']}]? ") or person['fname']
person['lname'] = input(f"Last name [{person['lname']}]? ") or person['lname']
person['age'] = input(f"First name [{person['age']}]? ") or person['age']
person['age'] = int(person['age'])
print(f'UPDATING PERSON WITH id: {pid}')
dao.update_person(person)

print('GETTING ALL PERSONS...')
persons = dao.get_persons()
for person in persons:
    print(person)
