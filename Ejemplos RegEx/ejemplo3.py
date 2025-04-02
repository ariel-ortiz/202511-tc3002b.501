import re

expreg = r'([aeiou]+)(\d*)|(hola)'
m = re.fullmatch(expreg, 'hola')
if m:
    print(m.group(0))
    print(m.group(1))
    print(m.group(2))
    print(m.group(3))

print(re.sub(r'[aiou]', 'e', 'una mosca parada en la pared'))
print(re.sub(r'feo|oloroso|chiquito',
             '<censurado>',
             'el feo y oloroso perro está muy chiquito'))
print(re.sub(r'([aeiou])',
             r'\1f\1',
             'una mosca parada en la pared'))
