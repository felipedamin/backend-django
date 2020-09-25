#!/usr/bin/env python
# coding: utf-8

import nltk
from nltk.corpus import stopwords
from wordcloud import WordCloud
import matplotlib.pyplot as plt

#uso as stopwords (palavras que sozinhas não tem significado nenhum) de um Lexicon da biblioteca NLTK
stop_words=set(stopwords.words('portuguese'))

#Função que recebe uma string e um título (opcional)
def show_wordcloud(data, fileName='wordcloud'):
    wordcloud = WordCloud(
        background_color='white',
        stopwords=stop_words,
        max_words=200,
        max_font_size=40, 
        scale=3,
        random_state=1 # chosen at random by flipping a coin; it was heads
    ).generate(str(data))

    fig = plt.figure(1, figsize=(12, 12))
    plt.axis('off')
     
    plt.imshow(wordcloud)
    #plt.show()
    fig.savefig('../HackathonKlabin/src/wordclouds/'+fileName+'.png')

if __name__ == "__main__":
    show_wordcloud('Adoro que todas as semanas temos lanches divertidos com a equipe Essa semana foi sensacional', 'pros')