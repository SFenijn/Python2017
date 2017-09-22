for i in range(4):
    for j in range(i+1):
        print(j, end= ' ')
    print()

outfile = open('oefenenles_6.txt', 'w')
outfile.write('De 3 regels in deze file eindigen met een new line caracter. \n')
outfile.write('\n')
outfile.write('Boven deze regel staat een lege regel.')
outfile.close()

infile