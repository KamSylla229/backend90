def moyenne(notes):
    if len(notes) == 0 :
        return None
    return sum(notes) / len(notes)



assert moyenne([10, 15, 20]) == 15.0
assert moyenne([12]) == 12.0
assert moyenne([]) is None
print("Tous les tests passent")

