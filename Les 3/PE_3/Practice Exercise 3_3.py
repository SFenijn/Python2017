# Een persoon mag stemmen als hij/zij 18 of ouder is en hij/zij een een paspoort heeft.
# Plus nu ook met een afwijzing.
ltijd = float(input('Wat is uw leeftijd?'))
pas = (input('Heeft u een Nederlands paspoort?. Ja of Nee.'))
if ltijd >= 18 and pas == ('ja' or 'j'):
    print('Gefeliciteerd, u mag stemmen')
else:
    print('U mag niet stemmen.')