import requests
from bs4 import BeautifulSoup

# URL der Webseite
url = "https://www.bag.admin.ch/bag/it/home/sitemap.html"

# HTTP-Anfrage an die Webseite
response = requests.get(url)

# Überprüfen, ob die Anfrage erfolgreich war
if response.status_code == 200:
    # HTML-Inhalt der Webseite parsen
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Alle Links (a-Tags) finden
    links = soup.find_all('a', href=True)
    
    # Links in eine Textdatei schreiben
    with open("links.txt", "w") as file:
        for link in links:
            href = link['href']
            file.write(href + "\n")
    
    print("Links wurden erfolgreich in die Datei 'links.txt' geschrieben.")
else:
    print(f"Fehler beim Abrufen der Webseite: {response.status_code}")
