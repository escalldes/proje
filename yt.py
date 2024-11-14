import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument("--disable-gpu")  # GPU hızlandırmasını devre dışı bırak
chrome_options.add_argument("--no-sandbox")   # bazı hataları engellemek için ekledim ikisinide

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)


def youtube(videoID,transPATH):
    # YouTube videosunu aç
    path = '//*[@id="segments-container"]/ytd-transcript-segment-renderer[position() >= 1 and position() <= '+transPATH+']/div'
    URL = f"https://www.youtube.com/watch?v={videoID}"
    driver.get(URL)
    time.sleep(2)
    driver.maximize_window() 
    time.sleep(30)
    # "Daha Fazla" butonunun yüklenmesini bekle ve tıkla
    
    try:
        daha_fazla_button = WebDriverWait(driver, 10).until(
         EC.element_to_be_clickable((By.XPATH, '//*[@id="expand"]'))
        )
        daha_fazla_button.click()
        time.sleep(5)

    # "Transkripti Göster" butonunun yüklenmesini bekle ve tıkla
        transkripti_goster_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="primary-button"]/ytd-button-renderer'))
        )
        transkripti_goster_button.click()
    except Exception as e:
        print("Bir hata oluştu:", e)

    
    time.sleep(3)

    # Transkripti al
    transkript_elemanlari = driver.find_elements(By.XPATH, f'{path}')    
    transkript_metni = " ".join([element.text for element in transkript_elemanlari])

    sentences = transkript_metni.splitlines()
    
    with open("cikti.txt", "w", encoding="utf-8") as file:
       file.write(transkript_metni)

    driver.quit()
    return sentences
    # '//*[@id="segments-container"]/ytd-transcript-segment-renderer[position() >= 1 and position() <= 670]/div'
    #H6I85wc8H3I





def youtubeHeadless(videoID, transPATH):
    # Headless modda tarayıcıyı başlat
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")  # Headless modda tam ekran kullanımı simüle et
    options.add_argument("--disable-gpu")  # Bazı sistemlerde GPU hatalarını önlemek için eklenir
    
    driver = webdriver.Chrome(options=options)

    # YouTube videosunu aç
    path = '//*[@id="segments-container"]/ytd-transcript-segment-renderer[position() >= 1 and position() <= '+transPATH+']/div'
    URL = f"https://www.youtube.com/watch?v={videoID}"
    driver.get(URL)
    time.sleep(2)

    # "Daha Fazla" butonunun yüklenmesini bekle ve tıkla
    try:
        daha_fazla_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="expand"]'))
        )
        daha_fazla_button.click()
        time.sleep(5)

        # "Transkripti Göster" butonunun yüklenmesini bekle ve tıkla
        transkripti_goster_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="primary-button"]/ytd-button-renderer'))
        )
        transkripti_goster_button.click()
    except Exception as e:
        print("Bir hata oluştu:", e)

    time.sleep(3)

    # Transkripti al
    transkript_elemanlari = driver.find_elements(By.XPATH, f'{path}')
    transkript_metni = " ".join([element.text for element in transkript_elemanlari])

    sentences = transkript_metni.splitlines()

    with open("cikti.txt", "w", encoding="utf-8") as file:
        file.write(transkript_metni)

    #driver.quit()
    return sentences