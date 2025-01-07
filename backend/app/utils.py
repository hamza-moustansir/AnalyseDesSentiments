import re

def clean_text(text):
    """
    Nettoyer le texte en supprimant les balises HTML, les caractères spéciaux et en le mettant en minuscules.
    """
    # Supprimer les balises HTML
    text = re.sub(r'<.*?>', '', text)
    # Convertir en minuscules
    text = text.lower()
    # Supprimer les caractères spéciaux et les chiffres
    text = re.sub(r"[^a-z\s]", "", text)
    # Supprimer les espaces supplémentaires
    text = re.sub(r'\s+', ' ', text).strip()
    return text
