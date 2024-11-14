
import spacy
import warnings
import yt
import langid

nlp_es = spacy.load("es_core_news_sm")
warnings.filterwarnings("ignore", category=FutureWarning) 

def language_test(cumleler):
    turkce_cumleler = [cumle for cumle in cumleler if langid.classify(cumle)[0] == 'es']
    return turkce_cumleler

def centences_to_words(sentences):
    all_words = []
    for sentence in sentences:
        doc = nlp_es(sentence)  # Cümleyi işleme
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
            doc = nlp_es(word)
            for word in doc:
                # Stopwords temizleme, yalnızca harflerden oluşan ve anlamlı uzunlukta olanları seçme
                if not word.is_stop and word.is_alpha and len(word) > 1:
                    root_word = word.lemma_.lower()
                    sentence_words.append(root_word)
        # Boş olmayanları ekleyelim
        if sentence_words:
            processed_words.append(sentence_words)
    
    return processed_words

liste  = yt.youtube("OoOOirB8g0w","748")+yt.youtubeHeadless("gHbe3J6gJmw","350")+yt.youtubeHeadless("cKlKza5r3NE","688")+yt.youtubeHeadless("eEeRHI_jCkc","703")
liste += yt.youtubeHeadless("7FAaSFZtWQc","738")+yt.youtubeHeadless("DsvJ7iv_d7Y","378")+yt.youtubeHeadless("Lrkrha5oFr0","378")+yt.youtubeHeadless("RrIBrMir6VU","459")
liste += yt.youtubeHeadless("xdhipe2YVPo","575")+yt.youtubeHeadless("Bbz_7dW3MQw","725")

liste = language_test(liste)
liste = centences_to_words(liste)
liste = stopwords_lemmatizes_rootword_lowercase(liste)

result = [' '.join(word for word in sentence) for sentence in liste]
result = list(set(result))
metin = '\n'.join(result)


with open("ESveri.csv", "w", encoding="utf-8") as file:
        file.write(metin)

