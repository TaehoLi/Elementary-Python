song = """by the rivers of babylon, there we sat down yeah we wept,
when we remember zion. when the wicked carried us away in captivity
required from us a song now how shall we sing the lord's song in a
strange land"""

alphabet = dict()
for c in song:
    if c.isalpha() == False:
        continue
    c = c.lower()
    if c not in alphabet:
        alphabet[c] = 1
    else:
        alphabet[c] += 1

for code in range(ord('a'), ord('z')+1):
    c = chr(code)
    num = alphabet.get(c,0)
    print(c, "=>", num)
