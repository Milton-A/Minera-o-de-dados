import re
import string
from collections import defaultdict, Counter
from nltk.corpus import stopwords
import nltk

nltk.download('stopwords')

def process_text(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return words

def build_word_following_dict(words):
    stop_words = set(stopwords.words('portuguese'))
    word_following = defaultdict(Counter)

    for i in range(len(words) - 1):
        current_word = words[i]
        next_word = words[i + 1]

        if current_word not in stop_words and next_word not in stop_words:
            word_following[current_word][next_word] += 1

    # Converte os contadores em listas de palavras mais comuns
    most_common_following = {word: counter.most_common(5) for word, counter in word_following.items()}
    return most_common_following

# Função para gerar um parágrafo aleatório
def generate_random_paragraph(most_common_following, length=50):
    import random

    # Escolhe uma palavra aleatória para começar
    current_word = random.choice(list(most_common_following.keys()))
    paragraph = [current_word]

    for _ in range(length - 1):
        if current_word in most_common_following:
            next_words = [word for word, _ in most_common_following[current_word]]
            current_word = random.choice(next_words)  # Escolhe uma palavra seguinte aleatória
            paragraph.append(current_word)
        else:
            break  # Para se a palavra atual não tiver palavras seguintes

    return ' '.join(paragraph)

# Lendo o livro
with open("assets/livro.txt", encoding="UTF-8") as f:
    book_text = f.read()

# Processar o texto do livro
words = process_text(book_text)

# Construir o dicionário de palavras seguidas
most_common_following = build_word_following_dict(words)

# Gerar um parágrafo aleatório
random_paragraph = generate_random_paragraph(most_common_following)
print("Parágrafo gerado:\n", random_paragraph)
