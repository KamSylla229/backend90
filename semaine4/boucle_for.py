def sommes_liste(nombres):
    total=0
    for nombre in nombres:
        total= total + nombre
    return total


assert sommes_liste([ 2,3,4,5,6 ]) == 20
assert sommes_liste([]) == 0          
assert sommes_liste([-2, -3,-4,-5]) == -14
print("Tous les tests passent")