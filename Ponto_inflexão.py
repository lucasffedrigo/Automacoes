from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep
import pyautogui
import sys
from selenium.webdriver import Keys, ActionChains

def converter_expressao(expressao):
    # Substitui '^^' por '**' para cálculo ou por '\u00B3' para visualização
    return expressao.replace('^^', '**')


print('EXEMPLO INPUT: x^^4 + 3x^^4')
expressao = input("Digite a expressão que deseja encontrar o ponto de inflexão: ")

browser = Firefox()
browser.get('https://pt.symbolab.com/solver/function-inflection-points-calculator')
 
sleep(1)
browser.find_element(By.XPATH, '//*[@id="main-input"]').click()
converter_expressao(expressao)

for caractere in expressao:
    if caractere == ' ':
        ActionChains(browser).key_down(Keys.ESCAPE).perform()
        sleep(0.5)
        ActionChains(browser).key_down(Keys.ESCAPE).perform()
        sleep(0.5)
        ActionChains(browser).key_down(Keys.ESCAPE).perform()
    else:
        ActionChains(browser).send_keys(caractere).perform()

browser.find_element(By.XPATH, '/html/body/div[10]/div[3]/section[1]/div[2]/div[1]/button').click()

