palavra = str(input("Digite uma palavra: "));
query = "";
for c in range (0, len(palavra)):
    if palavra[c] == 'A' or palavra[c] == 'a':
        if c == 0:
            query = '.- '
        else:
            query += '.- '
    if palavra[c] == 'B' or palavra[c] == 'b':
        if c == 0:
            query = '-... '
        else:
            query += '-... '
    if palavra[c] == 'C' or palavra[c] == 'c':
        if c == 0:
            query = '-.-. '
        else:
            query += '-.-. '
    if palavra[c] == 'D' or palavra[c] == 'd':
        if c == 0:
            query = '-.. '
        else:
            query += '-.. '
    if palavra[c] == 'E' or palavra[c] == 'e':
        if c == 0:
            query = '. '
        else:
            query += '. '
    if palavra[c] == 'F' or palavra[c] == 'f':
        if c == 0:
            query = '..-. '
        else:
            query += '..-. '
    if palavra[c] == 'G' or palavra[c] == 'g':
        if c == 0:
            query = '--. '
        else:
            query += '--. '
    if palavra[c] == 'H' or palavra[c] == 'h':
        if c == 0:
            query = '.... '
        else:
            query += '.... '
    if palavra[c] == 'I' or palavra[c] == 'i':
        if c == 0:
            query = '.. '
        else:
            query += '.. '
    if palavra[c] == 'J' or palavra[c] == 'j':
        if c == 0:
            query = '.--- '
        else:
            query += '.--- '
    if palavra[c] == 'K' or palavra[c] == 'k':
        if c == 0:
            query = '-.- '
        else:
            query += '-.- '
    if palavra[c] == 'L' or palavra[c] == 'l':
        if c == 0:
            query = '.-.. '
        else:
            query += '.-.. '
    if palavra[c] == 'M' or palavra[c] == 'm':
        if c == 0:
            query = '-- '
        else:
            query += '-- '
    if palavra[c] == 'N' or palavra[c] == 'n':
        if c == 0:
            query = '-. '
        else:
            query += '-. '
    if palavra[c] == 'O' or palavra[c] == 'o':
        if c == 0:
            query = '--- '
        else:
            query += '--- '
    if palavra[c] == 'P' or palavra[c] == 'p':
        if c == 0:
            query = '.--. '
        else:
            query += '.--. '
    if palavra[c] == 'Q' or palavra[c] == 'q':
        if c == 0:
            query = '--.- '
        else:
            query += '--.- '
    if palavra[c] == 'R' or palavra[c] == 'r':
        if c == 0:
            query = '.-.'
        else:
            query += '.-. '
    if palavra[c] == 'S' or palavra[c] == 's':
        if c == 0:
            query = '... '
        else:
            query += '... '
    if palavra[c] == 'T' or palavra[c] == 't':
        if c == 0:
            query = '- '
        else:
            query += '- '
    if palavra[c] == 'U' or palavra[c] == 'u':
        if c == 0:
            query = '..- '
        else:
            query += '..- '
    if palavra[c] == 'V' or palavra[c] == 'v':
        if c == 0:
            query = '...- '
        else:
            query += '...- '
    if palavra[c] == 'W' or palavra[c] == 'w':
        if c == 0:
            query = '.-- '
        else:
            query += '.-- '
    if palavra[c] == 'X' or palavra[c] == 'x':
        if c == 0:
            query = '-..- '
        else:
            query += '-..-'
    if palavra[c] == 'Y' or palavra[c] == 'y':
        if c == 0:
            query = '-.-- '
        else:
            query += '-.-- '
    if palavra[c] == 'Z' or palavra[c] == 'z':
        if c == 0:
            query = '--.. '
        else:
            query += '--.. '
print()
print(f'{palavra} em código morse:\n{query} ')
    