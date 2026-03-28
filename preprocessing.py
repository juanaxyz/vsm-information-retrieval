import re
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory


stemmer = StemmerFactory().create_stemmer()
stopwords = set(StopWordRemoverFactory().get_stop_words())


def tokenize(text):
    # Menghapus karakter non-alphanumeric
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    # Mengubah teks menjadi huruf kecil dan memisahkan kata-kata
    tokens = text.lower().split()
    return tokens

def remove_stopwords(tokens):
    return [word for word in tokens if word not in stopwords]

def stemming(tokens):
    return [stemmer.stem(word) for word in tokens]

def preprocess(sentence):
    tokens = tokenize(sentence)
    tokens_no_stopwords = remove_stopwords(tokens)
    stemmed_tokens = stemming(tokens_no_stopwords)
    return stemmed_tokens