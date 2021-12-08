capitals=dict()
key = input("Sisesta country: ")
item = input("Sisesta capital: ")
capitals[key] = item
print(capitals)

data={'Russia': 'Moscow'}
country=input('Sisesta country: ')
if country in data:
    print('Capital is:', data[country])
else:
    print('See riigi on puudub')
