import unicodedata

def format_string(raw_string):
    
    string = raw_string.lower()
    
    # supprime la ponctuation
    string = string.replace(".", "").replace("'", " ").replace("-", " ").replace("?", " ").replace("!", " ").replace(",", " ").replace(";", " ").replace(":", " ")
    # supprime les accents
    string = unicodedata.normalize('NFKD', string).encode('ascii', 'ignore').decode('utf-8')
    # supprime les espaces au debut et a la fin
    string = string.strip()
    # remplace les espaces par des underscores
    string = string.replace(" ", "_")
    # supprime les espaces en double
    string = ' '.join(string.split())

    return string