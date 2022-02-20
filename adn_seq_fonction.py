def seq_comp(seq):
    comp= []
    for base in seq :
        if base == 'A':
            comp.append('T')
        if base == 'T':
            comp.append('A')
        if base == 'G':
            comp.append('C')
        if base == 'C':
            comp.append('G')
    return comp


seq = ['A', 'T', 'C', 'G', 'A', 'T', 'C', 'G', 'A', 'T', 'C', 'G', 'C']
print("la sequence d'adn est                  '5-{}-3'".format("".join(seq)))
print("la sequence d'adn complémentaire est   '3-{}-5'".format("".join(seq_comp(seq))))