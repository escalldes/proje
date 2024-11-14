import spacy
import warnings
import yt
import langid

nlp = spacy.load("de_core_news_sm")

warnings.filterwarnings("ignore", category=FutureWarning) 

def language_test(cumleler):
    turkce_cumleler = [cumle for cumle in cumleler if langid.classify(cumle)[0] == 'de']
    return turkce_cumleler

def centences_to_words(sentences):
    all_words = []
    for sentence in sentences:
        doc = nlp(sentence)  # Cümleyi işleme
        print(f"cümlelerin birleşik hali: '{sentence}'")
        
        # Cümledeki kelimeleri birleştirip listeye ekleme
        sentence_words = [word.text for word in doc]
        all_words.append(sentence_words)
    return all_words

def stopwords_lemmatizes_rootword_lowercase(words_list):
    processed_words = []
    
    for words in words_list:
        sentence_words = []
        for word in words:
            doc = nlp(word)
            for token in doc:
                # Stopwords temizleme, yalnızca harflerden oluşan ve anlamlı uzunlukta olanları seçme
                if not token.is_stop and token.is_alpha and len(token) > 1:
                    root_word = token.lemma_.lower()
                    sentence_words.append(root_word)
        # Boş olmayanları ekleyelim
        if sentence_words:
            processed_words.append(sentence_words)
    
    return processed_words

liste = yt.youtube("H6I85wc8H3I","600")+yt.youtubeHeadless("2rProrsiq8Y","678")+yt.youtubeHeadless("HrXJ1mLZRIk","721")+yt.youtubeHeadless("XgIydXNd46A","636")+yt.youtubeHeadless("7Fr0CNA0qHc","709")+yt.youtubeHeadless("W7XyrRmos1w","368")
liste += yt.youtubeHeadless("2KAmqiTpa8Y","374")+yt.youtubeHeadless("L5urOxvdsG0","386")+yt.youtubeHeadless("m8vQQ0yE3Ko","622")+yt.youtubeHeadless("LnH0NJfziT4","543")

liste = language_test(liste)
liste = centences_to_words(liste)
liste = stopwords_lemmatizes_rootword_lowercase(liste)

result = [' '.join(word for word in sentence) for sentence in liste]
result = list(set(result))
metin = '\n'.join(result)

with open("DEveri.csv", "w", encoding="utf-8") as file:
        file.write(metin)

