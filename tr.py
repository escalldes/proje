import re
import spacy
import warnings
import stanza
import nltk
from nltk.corpus import stopwords
import yt
import langid

#stanza.download('tr')  // bunlar bir kere çalışmalı.
#nltk.download('stopwords')

turkish_stopwords = set(stopwords.words('turkish'))
extra_stopwords = {'bu', 'şu', 'gibi', 'var', 'yok','i','ı','ki','a','b','o','mı','g'}  # stanza stopwords tam doğru sonuç vermediği için kendimiz ekle yapıyoruz.
turkish_stopwords.update(extra_stopwords)

nlc = stanza.Pipeline('tr')
nlp = spacy.load("xx_ent_wiki_sm")
warnings.filterwarnings("ignore", category=FutureWarning) 

def language_test(cumleler):
    turkce_cumleler = [cumle for cumle in cumleler if langid.classify(cumle)[0] == 'tr']
    return turkce_cumleler

#cümleleri kelimelerine ayırma yeri
def centences_to_words(sent):
    all_words = []  # Kelimeleri saklamak için boş bir liste oluşturuyoruz
    for sentence in sent:
        doc = nlp(sentence)  # Cümleyi işleme
        
        
        # Cümledeki kelimeleri birleştirip listeye ekleme
        sentence_words = [word.text for word in doc]  # kelimeleri listeye ekliyoruz
        all_words.append(sentence_words)  # her cümledeki kelimeleri all_words listesine ekliyoruz
    return all_words

#ayrılmış kelimeleri temizleme kısmı
def process_sentences(sentences):
    processed_sentences = []
    
    for sentence in sentences:
        sentence_text = " ".join(sentence)  # Cümleyi tek bir string halinde birleştirip Stanza'ya gönderiyoruz
        doc = nlc(sentence_text)  # Stanza'dan işlenmiş cümle

        processed_sentence = []

        for stanza_sentence in doc.sentences:
            for word, stanza_word in zip(sentence, stanza_sentence.words):
                # Stopwords kontrolü: Burada stopwords listesine bakıyoruz
                word_clean = re.sub(r'[^\w\s]', '', word.lower())  # Noktalama ve küçük harfe dönüştürme
                if word_clean not in turkish_stopwords and len(word) > 1:  # Stopwords'e bakıyoruz
                    # Kök bulma işlemi
                    lemma = stanza_word.lemma
                    processed_word = lemma if lemma is not None else word  # Kök hali yoksa kelimeyi kullanıyoruz

                    processed_sentence.append(processed_word)  # İşlenmiş kelimeyi ekliyoruz
        
        processed_sentences.append(processed_sentence)  # İşlenmiş cümleyi ekliyoruz
    
    return processed_sentences



# bütün kelimeleri küçük harf yaptığımız fonksiyon
def lowercase_nested_list(nested_list):
    cleaned_words = [re.sub(r'[^\w\s]', '', word.lower()) for word in nested_list]
    return cleaned_words


# yeni bir liste oluşturup eski listedeki sadece türkçe harfleri bulundurucan kelimeleri alıyoruz
# bizim listemiz 2 boyutlu olduğu için 2 liste ouşturuyoruz biri cümleler biri kelimeler için daha sonra kelimelerin olduğu listeyi cümlelerin olduğu listeye ekliyoruz
def TRalphabet(ikili_liste):
    
    latin_alfabesi = re.compile('[^a-zA-ZçığöşüÇİĞÖŞÜ]')

    temizlenmis_liste = []

    for sublist in ikili_liste:
        temiz_sublist = []

        # Her kelimeyi kontrol etme
        for kelime in sublist:
            # kelimeleri türkçe karakter mi kontrol ediyoruz eğer türkçe karakterlerse yeni listeye ekliyoruz
            if not latin_alfabesi.search(kelime):
                temiz_sublist.append(kelime)

        # Eğer alt liste boş değilse temizlenmiş alt listeye ekliyoruz
        if temiz_sublist:
            temizlenmis_liste.append(temiz_sublist)

    return temizlenmis_liste

# youtube ve youtubeHeadless fonksiyonlarımızı kullanarak istenilen videonun transktiptini çekiyoruz.
# ilk videoyu ön planda çalıştırıp diğerlerini seleniumun Headless özelliği sayesinde arka planda açıyoruz.
transkript  = yt.youtube("0dCALHV46U8","908")+yt.youtubeHeadless("567JQTlankM","876")+yt.youtubeHeadless("RNTMIhnGWSs","625")+yt.youtubeHeadless("57QykV2HptA","534")
transkript += yt.youtubeHeadless("CMiOCrEnfrQ","652")+yt.youtubeHeadless("887xOuXwhgg","736")+yt.youtubeHeadless("4DmLKoqFMSs","665")+yt.youtubeHeadless("PCUquLDOq5s","400")
transkript += yt.youtubeHeadless("EyAYnfC8FB8","646")

# çektiğimiz verileri bizim istediğimiz son haline getirmek için gerekli fonksiyonları tek tek çağırıyoruz.
#transkript = lowercase_nested_list(transkript)
TRsentences = language_test(transkript)
words = centences_to_words(TRsentences)
clean_word = process_sentences(words)
clean_word = TRalphabet(clean_word)

# cümlelerin içindei kelimeleri birleştirip cümler haline getirip yeni bir tek boyurlu diziye atıyoruz.
result = [' '.join(word for word in sentence) for sentence in clean_word]

# işlediğimiz veride tekrar eden veriler olmaması adına setset küme yapıp onuda tekrar listeye çeviriyoruz.
result = list(set(result))
# listemizdeki her elemanı alt alta olucak şekilde bir stringe atıyoruz
metin = '\n'.join(result)

with open("TRveri.csv", "w", encoding="utf-8") as file:
        file.write(metin)
