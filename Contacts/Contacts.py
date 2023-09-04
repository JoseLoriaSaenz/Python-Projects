conctact_list = {'number': 4,
                 'students': 
                    [
                        {'name': 'Sarah Holderness', 'email': 'sarah.holderness@gamil.com'},
                        {'name': 'Peter Smith', 'email': 'peter.smith@gamil.com'},
                        {'name': 'Sam Wesley', 'email': 'sam.wesley@gamil.com'},
                        {'name': 'Paul Hoit', 'email': 'paul.hoit@gamil.com'},
                    ]
                }

email_list = []
print('Student emails:')
for student in conctact_list['students']:
    email_list.append(student['email'])


print(email_list)