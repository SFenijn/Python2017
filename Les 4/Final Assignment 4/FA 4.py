leeftijd = (float(input('Wat is uw leeftijd?')))
afstandKM = (float(input('Wat is de afstand in KM die u aflegt?')))
weekendrit = input('Is het weekend? ja/nee')


def standaardprijs(afstandKM):
    'berekend hoeveel een kaartje kost aan de hand van de afgelegde km.'
    if afstandKM > 50:
        afstandKM = 15 + 0.60 * afstandKM
        return afstandKM
    elif (afstandKM <= 50) and (afstandKM > 0):
        afstandKM = 0.80 * afstandKM
        return afstandKM
    else:
        afstandKM = 0
        return afstandKM

def ritprijs(leeftijd, weekendrit, afstandKM):
    'kijkt naar uitzonderingen op het standaardtarief.'
    if (leeftijd < 12) or (leeftijd >= 65):
        if weekendrit == 'ja':
            prijs = afstandKM * 0.65
        else:
            prijs = afstandKM * 0.7
    else:
        if weekendrit == 'ja':
            prijs = afstandKM * 0.6
        else:
            prijs = afstandKM
    return prijs

print(ritprijs(leeftijd, weekendrit, afstandKM))





