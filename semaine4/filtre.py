def filtrer_pairs(nombres):
    resultat = []
    for n in nombres:
        if n % 2 == 0 :
            resultat.append(n)
    return resultat


assert filtrer_pairs([1, 2, 3, 4]) == [2, 4]
assert filtrer_pairs([1, 3]) == []
assert filtrer_pairs([]) == []
print("Tous les tests passent")