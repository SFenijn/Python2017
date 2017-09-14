tst = ' test  '
print(tst.strip())
print(tst.index('e'))
tst = tst.strip()
print(tst.index('e'))

#Voorbeeld van eval waardoor je bijvoorbeeld een programma kan laten crachen omdat een variable nog niet is gedefiniëerd.

input_val1 = eval(input('Geef je input: '))
print(input_val1)
input_val2 = eval(input('Geef je input:'))
print(input_val2)