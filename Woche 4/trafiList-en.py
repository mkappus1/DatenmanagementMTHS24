import trafilatura

# Textdatei mit URL-Liste einlesen
with open('deine_datei_ersetzt_en.txt', 'r') as file:
    urls = file.read().splitlines()

# Jede URL abarbeiten und den Inhalt speichern
for idx, url in enumerate(urls, start=1):
    # Inhalte von der URL herunterladen und extrahieren
    downloaded = trafilatura.fetch_url(url)
    if downloaded:
        text = trafilatura.extract(downloaded)
        if text:
            # Datei erstellen und Inhalt speichern
            filename = f'BAG_webseite_en_{idx}.txt'
            with open(filename, 'w') as output_file:
                output_file.write(text)
            print(f'Inhalt von {url} wurde in {filename} gespeichert.')
        else:
            print(f'Inhalt von {url} konnte nicht extrahiert werden.')
    else:
        print(f'{url} konnte nicht heruntergeladen werden.')
