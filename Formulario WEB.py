from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select #Selecionar na lista suspensa
from selenium.webdriver.chrome.options import Options
import pyautogui as pa
options = Options()
options.add_experimental_option("detach", True)

navegador = webdriver.Chrome()

navegador.get("https://form.jotform.com/221436066464051")

navegador.maximize_window()

pa.sleep(2) #Carrega a pagina

navegador.find_element(By.ID, "first_3").send_keys("Teste nome")

pa.sleep(0.5)

navegador.find_element(By.ID, "last_3").send_keys("Teste sobrenome")

pa.sleep(0.5)

navegador.find_element(By.ID, "input_4").send_keys("teste@teste.com")

pa.sleep(0.5)

listaSuspensa = navegador.find_element(By.ID, "input_5")
Select(listaSuspensa).select_by_index(2)

pa.sleep(0.5)

filhos = "nao"

if filhos == "sim":

    navegador.find_element(By.ID, "label_input_6_0").click()

else:
    navegador.find_element(By.ID, "label_input_6_1").click()


pa.sleep(0.5)

corFavorita = "amarelo"

if corFavorita == "azul":
    navegador.find_element(By.ID, "label_input_7_0").click()

elif corFavorita == "amarelo":
    navegador.find_element(By.ID, "label_input_7_1").click()

elif corFavorita == "vermelho":
    navegador.find_element(By.ID, "label_input_7_2").click()

elif corFavorita == "laranja":
    navegador.find_element(By.ID, "label_input_7_3").click()

elif corFavorita == "preto":
    navegador.find_element(By.ID, "label_input_7_4").click()

elif corFavorita == "verde":
    navegador.find_element(By.ID, "label_input_7_5").click()

pa.sleep(0.5)

navegador.find_element(By.XPATH, '//*[@id="input_8"]/div[5]').click()

pa.sleep(0.5)

navegador.find_element(By.ID, "input_9_0_3").click()

pa.sleep(0.2)

navegador.find_element(By.ID, "input_9_1_3").click()

pa.sleep(0.5)
