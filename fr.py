
import spacy
import warnings
import yt
import langid

nlp_es = spacy.load("fr_core_news_sm")
warnings.filterwarnings("ignore", category=FutureWarning) 

def language_test(cumleler):
    turkce_cumleler = [cumle for cumle in cumleler if langid.classify(cumle)[0] == 'fr']
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
            for token in doc:
                # Stopwords temizleme, yalnızca harflerden oluşan ve anlamlı uzunlukta olanları seçme
                if not token.is_stop and token.is_alpha and len(token) > 1:
                    root_word = token.lemma_.lower()
                    sentence_words.append(root_word)
        # Boş olmayanları ekleyelim
        if sentence_words:
            processed_words.append(sentence_words)
    
    return processed_words

liste = yt.youtube("gHbe3J6gJmw","350")+yt.youtubeHeadless("h5vhGGuBNSw","564")+yt.youtubeHeadless("jYtFsXd9uUI","798")+yt.youtubeHeadless("X1F6CW2J3kc","741")+yt.youtubeHeadless("3_Y7SQaMWjA","628")+yt.youtubeHeadless("KphzT6snZPA","595")
liste +=yt.youtubeHeadless("hXd5KDJzykc","753")+yt.youtubeHeadless("OF71UahR4V8","792")+yt.youtubeHeadless("b3BDTfEIbX0","333")+yt.youtubeHeadless("2TIp1OQeP0E","699")+yt.youtubeHeadless("_AR-yX_GIuc","288")

liste = language_test(liste)
liste = centences_to_words(liste)
liste = stopwords_lemmatizes_rootword_lowercase(liste)

result = [' '.join(word for word in sentence) for sentence in liste]
result = list(set(result))
metin = '\n'.join(result)


with open("FRveri.csv", "w", encoding="utf-8") as file:
        file.write(metin)

