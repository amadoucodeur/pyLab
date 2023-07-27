

def plus_longue_sous_sequence(arr):
    out = []
    # copie de la sequence
    arrReversed = [*arr]
    # renverssement de la sequence 
    arrReversed.reverse()
    for i in arrReversed:
        item = []
        newBoucle = True
        while newBoucle:
            
    # Determination de la liste la plus longue
    # n = 0
    # outed = out[0]
    # for y in out:
    #     if n < len(y):
    #         n = len(y)
    #         outed = y
    # return outed

print(plus_longue_sous_sequence([1,3,7,4,6,5]))