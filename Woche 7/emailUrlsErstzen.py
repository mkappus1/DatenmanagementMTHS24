import re
import sys

def replace_emails_and_urls(text):
    """
    Ersetzt E-Mail-Adressen und URLs im Text durch Platzhalter.
    :param text: Eingabetext
    :return: Text mit ersetzten E-Mail-Adressen und URLs
    """
    # Muster für E-Mail-Adressen
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    
    # Muster für URLs (http, https, www)
    url_pattern = r'(https?://[^\s]+|www\.[^\s]+)'
    
    # E-Mails ersetzen
    text = re.sub(email_pattern, '@EMAIL@', text)
    
    # URLs ersetzen
    text = re.sub(url_pattern, '@URL@', text)
    
    return text

def process_files(input_file, output_file):
    """
    Liest einen Korpus aus einer Datei, bereinigt ihn und schreibt ihn in eine Ausgabedatei.
    :param input_file: Pfad zur Eingabedatei
    :param output_file: Pfad zur Ausgabedatei
    """
    try:
        # Datei lesen
        with open(input_file, 'r', encoding='utf-8') as infile:
            text = infile.read()
        
        # E-Mails und URLs ersetzen
        cleaned_text = replace_emails_and_urls(text)
        
        # Bereinigten Text schreiben
        with open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.write(cleaned_text)
        
        print(f"Die bereinigte Datei wurde erfolgreich in '{output_file}' gespeichert.")
    except FileNotFoundError:
        print(f"Die Datei '{input_file}' wurde nicht gefunden.")
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")

if __name__ == "__main__":
    # Prüfen, ob die richtigen Argumente übergeben wurden
    if len(sys.argv) != 3:
        print("Verwendung: python script.py <eingabedatei> <ausgabedatei>")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        process_files(input_file, output_file)
