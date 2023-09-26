# Ms_Reward.py
#
# Data Creazione: 12/07/2023
# Ultima Modifica: 26/09/2023
# Versione: 1.0
# Autore: xJackyll
# 
# N.B.  Non modificare lo script se non si ha chiaro cosa si sta facendo 




from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import logging
import os 
import random



# --------------------------------------------------------------------------------------------------

# FUNZIONI DI LOG

def log_info(message):
    logging.info(message)


def log_warning(message):
    logging.warning(message)


def log_error(message):
    logging.error(message)

# --------------------------------------------------------------------------------------------------

# FUNZIONE DI RICHIESTA WEB

def WebRequest(XPATH, Key = Keys.ENTER):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, XPATH))).send_keys(Key)

# --------------------------------------------------------------------------------------------------

# FUNZIONE DI GENERAZIONE AUTOMATICA TESTO E NUMERO

def generate_random_string():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    result = ''
    for i in range(8):
        result += random.choice(letters)
    
    resultNum = random.randint(1, 6)
    return result, resultNum

# --------------------------------------------------------------------------------------------------

# SETUP LOG

# Imposta il livello di log per visualizzare info, warning ed error
logging.basicConfig(level=logging.INFO)

# Crea una cartella per il file di log se non esiste gia' 
log_folder = "C:\\Temp"   # cambiate la cartella di log a piacere
if not os.path.exists(log_folder):
    os.makedirs(log_folder)

# Crea un file di log nella cartella e imposta il formato del messaggio di log
log_file = os.path.join(log_folder, "log_file.log")
file_handler = logging.FileHandler(log_file)
file_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logging.getLogger().addHandler(file_handler)

# --------------------------------------------------------------------------------------------------

# INIZIO DELLO SCRIPT

try:    
    # MOBILE_USER_AGENT = 'Mozilla/5.0 (Linux; Android 10; Pixel 3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0. 3945.79 Mobile Safari/537.36'
    # PC_USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 Safari/537.36"
    edge_options = webdriver.EdgeOptions() 
    edge_options.add_argument('--headless=new')
    edge_options.add_argument("--disable-gpu")
    edge_options.add_argument("user-data-dir=C:\\Users\\user\\AppData\\Local\\Microsoft\\Edge\\User Data\\Profile 2")  # Cambiate  questo path con il vostro profilo
    edge_options.add_argument("profile-directory=Profile 2")
    # edge_options.add_argument(f"user-agent={PC_USER_AGENT}")


    driver = webdriver.Edge(options = edge_options)
    driver.get('https://bing.com')

    for i in range(35):

        # cerco dalla barra di ricerca delle lettere casuali 
        random_str, random_num = generate_random_string()
        element = driver.find_element(By.ID, 'sb_form_q')
        element.send_keys(random_str)
        element.submit()

        # Wait for a random number of seconds
        time.sleep(random_num)
        
        # Get dei punti totali  fly_id_rc
        PuntiTOT = driver.find_element(By.ID, 'id_rc').text
        log_info("Numero Punti: " + PuntiTOT)

        # Pulisco la search bar
        driver.find_element(By.ID, 'sb_form_q').clear()

       # Tolgo il popup dei cookie
        if (i == 0):
            try: 
                driver.find_element(By.ID, 'bnp_btn_reject').click()
            except:
                log_info("nessun popup da rimuovere")

    # Vado sulla pagina di Microsoft rewards
    driver.get('https://rewards.bing.com/?signin=1')    
    time.sleep(random_num)
    time.sleep(random_num)
    # Riscatti i 30 punti dai siti
    driver.find_element(By.XPATH, ' /html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-daily-set-section/div/mee-card-group[1]/div/mee-card[1]/div/card-content/mee-rewards-daily-set-item-content/div').click()
    driver.find_element(By.XPATH, ' /html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-daily-set-section/div/mee-card-group[1]/div/mee-card[2]/div/card-content/mee-rewards-daily-set-item-content/div').click()
    driver.find_element(By.XPATH, ' /html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-daily-set-section/div/mee-card-group[1]/div/mee-card[3]/div/card-content/mee-rewards-daily-set-item-content/div').click()
    log_info("Script Terminato correttamente")    

except:
    log_error("c'e' stato un errore!")

time.sleep(random_num)
driver.quit()
