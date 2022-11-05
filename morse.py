palavra = str(input("Digite uma palavra: "));
query = "";
for c in range (0, len(palavra)):
    if palavra[c] in 'AaÁáÂâÀà':
        if c == 0:
            query = '.- '
        else:
            query += '.- '
    if palavra[c] in 'Bb':
        if c == 0:
            query = '-... '
        else:
            query += '-... '
    if palavra[c] in 'Cc':
        if c == 0:
            query = '-.-. '
        else:
            query += '-.-. '
    if palavra[c] in 'Dd':
        if c == 0:
            query = '-.. '
        else:
            query += '-.. '
    if palavra[c] in 'EéÊê':
        if c == 0:
            query = '. '
        else:
            query += '. '
    if palavra[c] in 'Ff':
        if c == 0:
            query = '..-. '
        else:
            query += '..-. '
    if palavra[c] in 'Gg':
        if c == 0:
            query = '--. '
        else:
            query += '--. '
    if palavra[c] in 'Hh':
        if c == 0:
            query = '.... '
        else:
            query += '.... '
    if palavra[c] in 'Ii':
        if c == 0:
            query = '.. '
        else:
            query += '.. '
    if palavra[c] in 'Jj':
        if c == 0:
            query = '.--- '
        else:
            query += '.--- '
    if palavra[c] in 'Kk':
        if c == 0:
            query = '-.- '
        else:
            query += '-.- '
    if palavra[c] in 'Ll':
        if c == 0:
            query = '.-.. '
        else:
            query += '.-.. '
    if palavra[c] in 'Mm':
        if c == 0:
            query = '-- '
        else:
            query += '-- '
    if palavra[c] in 'Nn':
        if c == 0:
            query = '-. '
        else:
            query += '-. '
    if palavra[c] in 'OoÓóÔô':
        if c == 0:
            query = '--- '
        else:
            query += '--- '
    if palavra[c] in 'Pp':
        if c == 0:
            query = '.--. '
        else:
            query += '.--. '
    if palavra[c] in 'Qq':
        if c == 0:
            query = '--.- '
        else:
            query += '--.- '
    if palavra[c] in 'Rr':
        if c == 0:
            query = '.-.'
        else:
            query += '.-. '
    if palavra[c] in 'Ss':
        if c == 0:
            query = '... '
        else:
            query += '... '
    if palavra[c] in 'Tt':
        if c == 0:
            query = '- '
        else:
            query += '- '
    if palavra[c] in 'UuÚú':
        if c == 0:
            query = '..- '
        else:
            query += '..- '
    if palavra[c] in 'Vv':
        if c == 0:
            query = '...- '
        else:
            query += '...- '
    if palavra[c] in 'Ww':
        if c == 0:
            query = '.-- '
        else:
            query += '.-- '
    if palavra[c] in 'Xx':
        if c == 0:
            query = '-..- '
        else:
            query += '-..-'
    if palavra[c] in 'Yy':
        if c == 0:
            query = '-.-- '
        else:
            query += '-.-- '
    if palavra[c] in 'Zz':
        if c == 0:
            query = '--.. '
        else:
            query += '--.. '
print()
print(f'{palavra} em código morse:\n{query} ')
    