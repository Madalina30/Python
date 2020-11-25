# declararea unei liste care să conțină elementele 7, 8, 9, 2, 3, 1, 4, 10, 5, 6 (în această ordine)
lista = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

# afișarea unei alte liste ordonată ascendent (lista inițială trebuie păstrată în aceeași formă)
print(sorted(lista))

# afișarea unei liste ordonată descendent (lista inițială trebuie păstrată în aceeași formă)

print(sorted(lista, reverse=True))

# afișarea numerelor pare din listă (folosind DOAR slice, altă metodă va fi considerată invalidă)

print(lista[::2])

# afișarea numerelor impare din listă (folosind DOAR slice, altă metodă va fi considerată invalidă)

print(lista[1::2])

# afișarea elementelor multipli ai lui 3
print(lista[2], lista[4], lista[9])

# a se păstra acuratețea indexilor - aceștia trebuie să fie cât mai specifici
