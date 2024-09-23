import random

# Begrüßung
print("Hallo Welt!")

# Benutzerinformationen abfragen
name = input("Wie heißt du? ")
alter = input("Wie alt bist du? ")
lieblingsfarbe = input("Was ist deine Lieblingsfarbe? ")

# Witzige oder freundliche Begrüßung basierend auf Benutzerdaten
witzige_antworten = [
    f"Ah, {name}! Schon {alter} Jahre alt und immer noch keine Falten – beeindruckend!",
    f"{name}, wenn du {alter} bist, dann bin ich wohl ein Dinosaurier!",
    f"{name}, wusstest du, dass {lieblingsfarbe} nicht nur eine Farbe, sondern auch ein Lebensstil ist? Respekt!",
    f"{name}, du siehst für {alter} erstaunlich gut aus – dein Geheimnis ist bestimmt die {lieblingsfarbe} Energie!",
    f"{name}, du hast echt einen guten Geschmack, {lieblingsfarbe} ist auch meine Lieblingsfarbe – und das will was heißen!"
]

# Zufällige Auswahl einer Begrüßung
begruessung = random.choice(witzige_antworten)

# Ausgabe
print(begruessung)
print(f"Schön, dich kennenzulernen, {name}! Ich hoffe, dein Tag ist so bunt wie {lieblingsfarbe}.")

# Abschluss mit einer kleinen Überraschung
print("P.S.: Wusstest du, dass Programmierer manchmal einfach Code schreiben, nur um hallo zu sagen? 🖐️")