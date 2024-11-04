import re
import string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk

nltk.download('stopwords')
nltk.download('wordnet')

def split_into_chapters(text):
    chapters = re.split(r'\n\s*Capítulo\s*\d+', text)
    return chapters[1:] 

def process_chapter(chapter):
    words = re.findall(r'\b\w+\b', chapter.lower())  
    lemmatizer = WordNetLemmatizer()

    stop_words = set(stopwords.words('portuguese'))
    processed_words = [
        lemmatizer.lemmatize(word) for word in words if word not in stop_words
    ]

    return processed_words

with open("assets/livro.txt", encoding="UTF-8") as f:
    text = f.read()

chapters = split_into_chapters(text)

all_processed_words = []
for chapter in chapters:
    processed_words = process_chapter(chapter)
    all_processed_words.append(processed_words)

for i, words in enumerate(all_processed_words):
    print(f"Capítulo {i + 1}:")
    print(words)
    print("\n")
