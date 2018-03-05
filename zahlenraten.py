#Zahlenraten

import random
zufallszahl = random.randint(1,100)
titel = "Willlkommen beim Zahlen-Rate-Spiel"
text = "Bitte versuche meine Zahl wischen 1 und 100 zu erraten"
eingabetext = "Dein versuch: "

print(titel)
print(text)
anzahlderversuche = 0

fertig = False

while fertig == False:
    zahl = int(input(eingabetext))
    anzahlderversuche = anzahlderversuche +1
    
    if (zahl == zufallszahl):
        print("gewonnen!")
        fertig = True
    elif(zahl < zufallszahl):
        print("die gesuchte zahl ist größer")
    else:
        print("die gesuchte zahl ist kleiner")
        


print("super du hast dafür nur ", anzahlderversuche, "versuche benötigt")
print("ende")
    
