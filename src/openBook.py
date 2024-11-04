from collections import defaultdict
import PyPDF2
import string
from nltk.corpus import stopwords
import nltk
from porter2stemmer import Porter2Stemmer
from snowballstemmer import PortugueseStemmer

nltk.download('stopwords')

# Carrega as stopwords do português
stop_words = set(stopwords.words('portuguese'))

# Cria um objeto stemmer para o português
stemmer = Porter2Stemmer()
stemmer2 = PortugueseStemmer()

# Ler o livro a partir do arquivo
with open("assets/livro.txt", encoding="UTF-8") as f: 
     # Dividir o texto em palavras
    words = [word for line in f for word in line.split()]

# Transformar palavras para minúsculas, remover pontuação e filtrar stopwords
# Apenas as palavras que não são stopwords serão armazenadas
filtered_words = [
    word.lower().translate(str.maketrans('', '', string.punctuation))
    for word in words if word.lower().translate(str.maketrans('', '', string.punctuation)) not in stop_words
]

# print("{0:20}{1:20}".format("--Word--","--Stem--"))
# for word in filtered_words:
#    print ("{0:20}{1:20}".format(word, stemmer.stem(word)))

# Aplicar stemming às palavras filtradas
stemmed_words = [stemmer2.stemWord(word) for word in filtered_words]

# print("{0:20}{1:20}".format("--Word--","--Stem--"))
# for word in filtered_words:
#    print ("{0:20}{1:20}".format(word, stemmer2.stemWord(word)))

# Converter a lista de palavras filtradas em uma lista de pares (palavra, 1)
pairs = [(word, 1) for word in filtered_words]

# dicionário para contar ocorrências
word_count = defaultdict(int)
for word, count in pairs:
    word_count[word] += count
    
# Converter o dicionário em uma lista de pares (palavra, ocorrências)
grouped_pairs = list(word_count.items())
grouped_pairs.sort(key=lambda pair: pair[1], reverse=True)

# print("{0:20}{1:20}".format("--Word--", "--Occurrences--"))
# for word, occurrences in grouped_pairs:
#     print("{0:20}{1:20}".format(word, occurrences))

from wordcloud_generator import remove_common_words, save_filtered_words, generate_wordcloud

filtered_grouped_pairs = remove_common_words(grouped_pairs, n=10)
save_filtered_words(filtered_grouped_pairs)
generate_wordcloud(filtered_grouped_pairs)
