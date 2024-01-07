contact = dict()

def Find_Name():
    print("Enter full name: ")
    name = input()
    if name in contact:
        print('Cell phone:', contact[name][0], 'Comment:', contact[name][1])
    else:
        print('Contact not found.')

def Dell_Name():
    print("Enter the name of the contact to be deleted: ")
    del contact[input()]
    print('Contact was deleted')

def Change_Name():
    print("Enter the name of the changed contact and the new name separated by a space: ")
    name1, name2 = input().split()
    if name1 in contact:
        contact[name2] = contact.pop(name1)
        print('New name of the contact', name2, ', cell phone:', contact[name2][1], ', comment:', contact[name2][2])
    else:
        print('Contact not found.')

def Append_Name():
    print('Enter the full name: ')
    name = input()
    s = []
    print('Enter cell phone: ')
    s.append(input())
    print('Enter the comment: ')
    s.append(input())
    contact[name] = s
    print('New contact:', name, ', cell phone:', contact[name][0], ', comment:', contact[name][1])

def Print_Full_Name():
    print('\n',contact)

def Print_Menu():
    print('Menu: ')
    print('Enter 1 to get the contact')
    print('Enter 2 to delete contact')
    print('Enter 3 to change the contact')
    print('Enter 4 to add a contact')
    print('Enter 5 to display all contacts')
    print('Enter 0 to end the program')

with open('input.txt', 'r+') as contacts:
    A = contacts.readline().split(' ', 1)
    while A[0]:
        contact[A[0]] = A[1].split()
        A = contacts.readline().split(' ', 1)

Print_Menu()
Menu = [1, 2, 3, 4, 5, 0]
a = int(input())
while not (a in Menu):
    Print_Menu()
    a = int(input())

while a != 0:
    if a == 1:
        Find_Name()
    elif a == 2:
        Dell_Name()
    elif a == 3:
        Change_Name()
    elif a == 4:
        Append_Name()
    elif a == 5:
        Print_Full_Name()
    Print_Menu()
    a = int(input())

# Не нужно закрывать и снова открывать файл.
# contacts.close()
# contacts = open('input.txt', 'w')

# Запись в файл.
with open('input.txt', 'w') as contacts:
    for key, value in contact.items():
        contacts.write(key + ' ' + ' '.join(value) + '\n')
