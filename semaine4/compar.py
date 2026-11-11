def compter_pairs(nombres):
    nombre_pair=0
    for nombre in nombres:
        if nombre % 2 == 0:
            nombre_pair = nombre_pair + 1
    return nombre_pair



assert compter_pairs([ 2,3,4,5,6 ]) == 3
assert compter_pairs([]) == 0          
assert compter_pairs([0,-4,]) == 2
assert compter_pairs([-3, -4]) == 1
print("Tous les tests passent")
            
    

    