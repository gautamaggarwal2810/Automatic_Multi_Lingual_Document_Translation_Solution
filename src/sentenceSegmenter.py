
from nltk.tokenize import sent_tokenize

def split_sentences(content, languageCode):
    return sent_tokenize(content, language=languageCode)
