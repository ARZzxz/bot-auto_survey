from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

# Data responden lengkap
responden = [
    {"nama": "Achmad Hadziq Siddiq", "umur": 8, "hobi": "Bermain petak umpet"},
    {"nama": "Admiral Aggip", "umur": 10, "hobi": "Bermain lego"},
    {"nama": "Afiyah Alana Putri", "umur": 9, "hobi": "Bermain bulu tangkis"},
    {"nama": "Ainun Afifah", "umur": 9, "hobi": "Menggambar"},
    {"nama": "Aisyah Afikah Ayunindia", "umur": 9, "hobi": "Bermain gadget"},
    {"nama": "Ajeng Siti Nur Aulia", "umur": 9, "hobi": "Bermain bulu tangkis"},
    {"nama": "Alesha Zahra Putri", "umur": 9, "hobi": "Bermain bola bekel"},
    {"nama": "Alfin Maulana Usman", "umur": 9, "hobi": "Bermain sepak bola"},
    {"nama": "Aqila Risty Mulyana", "umur": 8, "hobi": "Membaca cerita"},
    {"nama": "Arin Ananda", "umur": 9, "hobi": "Menggambar"},
    {"nama": "Azzahra Arsyfa Rahman", "umur": 8, "hobi": "Bermain gadget"},
    {"nama": "Cheifa Oktaviona", "umur": 9, "hobi": "Bernyanyi"},
    {"nama": "Dede Srirejeki", "umur": 9, "hobi": "Membaca cerita"},
    {"nama": "Elvira Orlin Firdaus", "umur": 9, "hobi": "Bermain petak umpet"},
    {"nama": "Enzo Algibran Nugraha", "umur": 8, "hobi": "Membaca cerita"},
    {"nama": "Fadhilah Khoerun Nisa", "umur": 9, "hobi": "Menggambar"},
    {"nama": "Farhan", "umur": 9, "hobi": "Mewarnai"},
    {"nama": "Gabriel Haholongan Simbolon", "umur": 8, "hobi": "Bermain lego"},
    {"nama": "Gilang Pratama", "umur": 9, "hobi": "Menggambar"},
    {"nama": "Ibnu Fadil", "umur": 9, "hobi": "Menggambar"},
    {"nama": "Jafar Umar Tolib", "umur": 8, "hobi": "Menggambar"},
    {"nama": "Kafita Rizqiya Ramadani", "umur": 9, "hobi": "Menggambar"},
    {"nama": "Kenzo Gustara", "umur": 8, "hobi": "Bermain petak umpet"},
    {"nama": "Muhamad Yudis Pratama", "umur": 8, "hobi": "Bermain lego"},
    {"nama": "Muhammad Danu Rijki", "umur": 9, "hobi": "Bermain lego"},
    {"nama": "Muhammad Khoirul Apif", "umur": 10, "hobi": "Bermain bulu tangkis"},
    {"nama": "Muhammad Raffa Al Shidiiq", "umur": 9, "hobi": "Bermain gadget"},
    {"nama": "Muhammad Salman Alfarizi", "umur": 9, "hobi": "Bermain bola bekel"},
    {"nama": "Naila Rizkia Akhifa", "umur": 9, "hobi": "Bermain bulu tangkis"},
    {"nama": "Naura Zhafira Purnama", "umur": 10, "hobi": "Mewarnai"},
    {"nama": "Nur Ainun Jannah", "umur": 8, "hobi": "Bermain sepak bola"},
    {"nama": "Nuraisah", "umur": 9, "hobi": "Bermain bola bekel"},
    {"nama": "Pelisa Meira Silvana", "umur": 9, "hobi": "Bermain sepeda"},
    {"nama": "Radhin Nabil Alauna", "umur": 8, "hobi": "Bermain layang-layang"},
    {"nama": "Radhinka Athalla", "umur": 8, "hobi": "Bermain petak umpet"},
    {"nama": "Raisa Zivanna Letisyah", "umur": 8, "hobi": "Bernyanyi"},
    {"nama": "Raysa Mey Handriyanti", "umur": 9, "hobi": "Bermain petak umpet"},
    {"nama": "Rizky Ramadhan", "umur": 9, "hobi": "Bermain bola bekel"},
    {"nama": "Saiful Akbar", "umur": 11, "hobi": "Bermain petak umpet"},
    {"nama": "Syifah Nur Ainih", "umur": 9, "hobi": "Bermain bola bekel"},
    {"nama": "Trisya Viona Rhamadani", "umur": 9, "hobi": "Bermain gadget"},
    {"nama": "Uswatun Hasanah", "umur": 9, "hobi": "Bernyanyi"},
]

# Path ke ChromeDriver
driver_path = r"C:\Users\malfa\OneDrive\Desktop\auto_survey\chromedriver.exe"

# Inisialisasi opsi Chrome
options = Options()
options.add_argument("--start-maximized")

# Inisialisasi Service dengan ChromeDriver
service = Service(driver_path)

for responden_data in responden:
    # Inisialisasi WebDriver
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://forms.gle/dhrpJFD1VpQcnr1w5") # Link Gform yang dituju

    # Tunggu form terbuka
    time.sleep(3)

    try:
        #jika perlu mengisi kolom lain maka perlu mencari element yang tekait pada inspect element chrome
        # Isi Nama
        nama_field = driver.find_element(By.XPATH, '//input[@aria-labelledby="i1 i4"]')
        nama_field.send_keys(responden_data["nama"])
        time.sleep(1)

        # Isi Umur
        umur_field = driver.find_element(By.XPATH, '//input[@aria-labelledby="i6 i9"]')
        umur_field.send_keys(str(responden_data["umur"]))
        time.sleep(1)

        # Isi Hobi
        hobi_field = driver.find_element(By.XPATH, '//input[@aria-labelledby="i11 i14"]')
        hobi_field.send_keys(responden_data["hobi"])
        time.sleep(1)

        # Isi Rating untuk 5 pertanyaan
        for i in range(5):  # Ada 5 pertanyaan rating
            # Pilih rating bintang secara acak (3-5 lebih dominan)
            if random.randint(1, 10) > 2:
                rating_to_click = random.randint(3, 5)  # 3-5
            else:
                rating_to_click = random.randint(1, 2)  # 1-2

            # Klik rating sesuai pertanyaan
            rating_xpath = f'(//*[@role="radio"])[{i * 5 + rating_to_click}]'  # Sesuaikan indeks jika diperlukan
            rating = driver.find_element(By.XPATH, rating_xpath)
            rating.click()
            time.sleep(1)

        # Klik tombol Kirim
        submit_button = driver.find_element(By.XPATH, '//span[text()="Kirim"]')  # Ganti sesuai teks tombol
        submit_button.click()
        print(f"Form submitted for {responden_data['nama']}!")

    except Exception as e:
        print(f"Error for {responden_data['nama']}: {e}")

    finally:
        # Tunggu sebelum menutup browser
        time.sleep(2)
        driver.quit()
