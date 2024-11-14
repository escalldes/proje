Çok Dilli YouTube Transkript Çekme Aracı:
Bu proje, YouTube videolarından çok dilli transkript verisi çekmek için Python tabanlı bir uygulamadır. Uygulama, farklı dillerdeki
(Almanca, Türkçe, Fransızca, İspanyolca, İngilizce) YouTube video transkriptlerini çıkarmak ve işlemek için çeşitli web kazıma teknikleri ve Doğal Dil İşleme (NLP) kütüphaneleri kullanır.

Özellikler:
YouTube videolarından transkript verilerini Selenium ve headless tarayıcı kullanarak çeker.
Almanca, Türkçe, Fransızca, İspanyolca ve İngilizce dillerini destekler.
Çekilen metni işler:
Cümleleri kelimelere ayırır.
Stopwords (gereksiz kelimeler) temizler.
Kelimeleri kök haline getirir.
İşlenmiş transkript verilerini her dil için CSV dosyasına kaydeder.
Tarayıcı kazıma işlemi için normal ve headless modlarını destekler.

Kullanılan Teknolojiler:
Python 3.x: Projenin yazıldığı programlama dili.
Selenium: YouTube transkriptlerini web kazıma için kullanılır.
SpaCy: Doğal Dil İşleme (NLP) görevleri için kullanılır; kelime ayırma, lemmatization ve stopword temizleme gibi işlemleri yapar.
Stanza: Türkçe metin işleme için kullanılan NLP kütüphanesidir.
langid: YouTube video transkriptlerinin dilini tespit etmek için kullanılır.
WebDriver Manager: Selenium için tarayıcı sürücüsünü otomatik olarak yönetir.

Kurulum ve Başlangıç
Projeyi yerel bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyin:

Depoyu klonlayın:

git clone https://github.com/kullaniciadiniz/multi-language-youtube-transcript.git
Gerekli Python paketlerini yükleyin: Proje klasörüne gidin ve gerekli bağımlılıkları pip ile yükleyin:

pip install -r requirements.txt
Gerekli NLP modellerini indirin: Türkçe metin işleme için Stanza'nın Türkçe modelini indirmeniz gerekmektedir. Bunu aşağıdaki gibi yapabilirsiniz:

import stanza
stanza.download('tr')
Script'i çalıştırın: Her şey hazır olduktan sonra ana script'i çalıştırarak YouTube transkriptlerini çekmeye başlayabilirsiniz:

python ana_script.py

Kullanım
Script, birden fazla YouTube videosunun transkriptlerini çeker, metni işler (lemmatizasyon, stopword temizleme) ve CSV dosyasına kaydeder.
Videolar, YouTube video ID'leri ile tanımlanır ve transkript çekme işlemi Selenium tarayıcı otomasyonu kullanılarak yapılır.
Örnek: Almanca YouTube transkriptini çekmek için komut:
transkript = yt.youtube("VIDEO_ID", "transkript_sayısı")

Örnek: Türkçe YouTube transkriptini çekmek için komut:
transkript = yt.youtubeHeadless("VIDEO_ID", "transkript_sayısı")

Dosyalar
DEveri.csv: İşlenmiş Almanca transkript verilerini içerir.
TRveri.csv: İşlenmiş Türkçe transkript verilerini içerir.
FRveri.csv: İşlenmiş Fransızca transkript verilerini içerir.
ENveri.csv: İşlenmiş İngilizce transkript verilerini içerir.
ESveri.csv: İşlenmiş İspanyolca transkript verilerini içerir.
