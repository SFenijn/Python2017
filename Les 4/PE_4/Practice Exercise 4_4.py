def new_password(oldP, newP):
    'Deze functie kijkt of het nieuwe paswoord anders is dan het oude paswoord. Ook controleerd het of het meer dan zes karakters heeft.'
    if oldP != newP and len(newP) >= 6:
        print('Wachtwoord is gewijzigd')
    else:
        print('Wachtoord kon niet gewijzigd worden.')
print(new_password('passwoord', 'passwoord2'))