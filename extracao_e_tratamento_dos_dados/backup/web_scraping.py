# Objetivo: capturar o texto de RICMS/MT da página web do portal da legislação da SEFAZ,
# identificar quais parágrafos correspondem à Capítulos, Incisos, Alíneas e itens
# e gerar um arquivo JSON com essas informações

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import re

from selenium.webdriver.common.print_page_options import PrintOptions

# mantendo o navegador aberto após o fim da execução do código
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)

url = 'https://www.sefaz.mt.gov.br/legislacao/home.aspx'

driver.get(url) # acessa a URL
driver.implicitly_wait(5) # espera a página carregar

content_table = driver.find_element(By.XPATH, '/html/body/form/div[13]/div/div/div[1]/div[3]/table/tbody/tr/td/div/div/div/div[2]/div[1]/div[2]/table/tbody/tr/td/table/tbody')
paragraphs = content_table.find_elements(By.TAG_NAME, 'p')

for item in paragraphs[:50]:
    print(item.text)

driver.quit()