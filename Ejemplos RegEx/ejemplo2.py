import re

cadena = "Hola, a todos (los ITC's) de este grupo."
m = re.search(r'ITC', cadena)
if m:
    print(m.span())
    print(m.string)
    print(m.group())

m = re.search(r'IRS', cadena)
if m:
    print(m.span())
    print(m.string)
    print(m.group())
else:
    print(m)

m = re.match(r'hola', cadena, re.IGNORECASE | re.ASCII)
if m:
    print(m.span())
    print(m.string)
    print(m.group())

print(cadena.split())

for palabra in re.finditer(r"[a-z']+", cadena, re.IGNORECASE):
    print(palabra.group(0))
