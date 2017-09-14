#Hier vraag ik om uurloon en maak er een Float van.

uur_L = float(input('Wat is uw uurloon? '))

#Hier vraag ik hoeveel uur de persoon heeft gewerkt.

uur_t = float(input('Hoeveel uur heeft u gewerkt?'))

#Hier bereken ik het salaris.

salaris = uur_L * uur_t

#Hier geef ik een overzicht op het salaris.

print('Omdat u', uur_t, 'uur heeft gewerkt. Heeft u met een uurloon van', uur_L,'euro een salaris van', salaris, 'euro ontvangen.')
