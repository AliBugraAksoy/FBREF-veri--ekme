from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import time


options = Options()
options.headless = True  # Tarayıcıyı görünmez yapmak için


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

#gerekli linki gir. 
url = "https://fbref.com/en/comps/11/2023-2024/stats/2023-2024-Serie-A-Stats"
driver.get(url)


driver.implicitly_wait(20)


html = driver.page_source


soup = BeautifulSoup(html, 'html.parser')

players_data = []

table = soup.find('table', {'id': 'stats_standard'})

rows = table.find_all('tr')

for row in rows[1:]:
    cols = row.find_all('td')
    if len(cols) > 0:
        player_data = {
            'RK': cols[0].text.strip(),
            'Player': cols[1].text.strip(),
            'Nation': cols[2].text.strip(),
            'Pos': cols[3].text.strip(),
            'Age': cols[4].text.strip(),
            'Squad': cols[5].text.strip(),
            'Comp': cols[6].text.strip(),
            'Games': cols[7].text.strip(),
            'Starts': cols[8].text.strip(),
            'Minutes': cols[9].text.strip(),
            'Goals': cols[10].text.strip(),
            'Assists': cols[11].text.strip(),
            'Goals_Plus_Assists': cols[12].text.strip(),
            'Goals_Per_90': cols[13].text.strip(),
            'Assists_Per_90': cols[14].text.strip(),
            'Goals_and_Assists_Per_90': cols[15].text.strip(),
            'Shots': cols[16].text.strip(),
            'Shots_Per_90': cols[17].text.strip(),
            'Shot_Conversion': cols[18].text.strip(),
            'Goals_Per_Shot': cols[19].text.strip(),
            'xAG': cols[20].text.strip(),
            'npxG+xAG': cols[21].text.strip(),
            'PrgC': cols[22].text.strip(),
            'PrgP': cols[23].text.strip(),
            'PrgR': cols[24].text.strip(),
            'Gls': cols[25].text.strip(),
            'Ast': cols[26].text.strip(),
            'G+A': cols[27].text.strip(),
            'G-PK': cols[28].text.strip(),
            'G+A-PK': cols[29].text.strip(),
            'xG2': cols[30].text.strip(),
            'xAG2': cols[31].text.strip(),
            'xG+xAG2': cols[32].text.strip(),
            'npxG2': cols[33].text.strip(),
            'npxG+xAG2': cols[34].text.strip(),
            'Matches': cols[35].text.strip(),
        }
        players_data.append(player_data)

df = pd.DataFrame(players_data)
#Dosyanın ismini buraya yaz.
df.to_csv('2023-2024.csv', index=False)

driver.quit()
