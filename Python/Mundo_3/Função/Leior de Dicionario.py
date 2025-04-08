def nota(*n,situ=False):
    """
    ->Function to analyze notes and quotes from various students.
    :To n: one or more notes and situations from several students. (accepts several)
    :To situ: optional value, indicating whether or not to add the situation.
    :return: dictionary with various information about situations about the situation of the class
    """
    notas = {}
    notas["Total"] = len(n)
    notas["Maior"] = max(n)
    notas["Menor"] = min(n)
    notas["Media"] = sum(n)/len(n)
    if situ:
        if notas["Media"] >= 7:
            notas["situação"] = "Otima"
        elif notas["Media"] > 5:
            notas["situação"] = "Regular"
        else :
            notas["situação"] = "Ruim"
    return notas    

print(nota(6,5,4,3,situ=True))