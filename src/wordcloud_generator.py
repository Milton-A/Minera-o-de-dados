from wordcloud import WordCloud
import matplotlib.pyplot as plt

def remove_common_words(grouped_pairs, n=10):
    return grouped_pairs[:n]


def save_filtered_words(filtered_grouped_pairs, output_file="assets/filtered_words.txt"):
    """Salva as palavras filtradas em um arquivo de texto."""
    with open(output_file, "w", encoding="UTF-8") as f:
        for word, count in filtered_grouped_pairs:
            f.write(f"{word}: {count}\n")
            
def generate_wordcloud(filtered_grouped_pairs, output_image="assets/wordcloud.png"):
    """Gera e salva uma nuvem de palavras a partir da lista filtrada."""
    # Criar um dicionário com as palavras e suas ocorrências
    word_freq = dict(filtered_grouped_pairs)

    # Gerar a nuvem de palavras
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_freq)

    # Mostrar a nuvem de palavras
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')  # Não mostrar os eixos
    plt.show()

    # Salvar a nuvem de palavras em um arquivo
    wordcloud.to_file(output_image)
    
