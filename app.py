  
from functions import showMenu, create, remove, show, update

n = 1

while n > 0:
    showMenu()
    n = int(input('Uildliin dugaar oruulna uu: '))
    if n == 1:
        show()
    elif n == 2:
        create()
    elif n == 3:
        remove()
    elif n == 4:
        update()
    else:
        print('Ta programaas garlaa...')
        break