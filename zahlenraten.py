#Zahlenraten

import random
titel = "Willlkommen beim Zahlen-Rate-Spiel"
print(titel)

von = int(input("Bitte die zufakkszahk-unterschranke festgestellt: "))
bis = int(input("Bitte die zufakkszahk-oberschranke festgestellt:"))

zufallszahl = random.randint(von, bis)
text = "Bitte versuche meine Zahl wischen" ,von, " und " ,bis, " zu erraten"
print(text)


eingabetext = "Dein versuch: "


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
