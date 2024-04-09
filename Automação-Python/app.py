from selenium import webdriver # Para conseguir chegar ao navegador
from selenium.webdriver.common.by import By # By - vai permitir selecionar campos em um site para interagir com eles
from time import sleep # Para pausar entre ações para não haver bloqueio e nem travamentos na automação
import openpyxl # Para automação de planilhas
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# 1 - Navegar até o site X
driver =webdriver.Chrome()

driver.get('tal site') # Navegar até o site
sleep(2)
# 2 - Digitar e-mail
email = driver.find_element(By.XPATH,"//input[@id='email']") # Para buscar um elemento
sleep(2)
email.send_keys('admin@gmail.com') # Função do selenium para escrever algo
# 3 - Digitar a senha
senha = driver.find_element(By.XPATH,"//input[@id='senha']")
sleep(2)
senha.send_keys('blabla123')
# 4 - Clicar em entrar
botao_entrar = driver.find_element(By.XPATH,"//button[@id='Entrar']")
sleep(2)
botao_entrar.click()
# 5 - extrair as informações a planilha
empresas = openpyxl.load_workbook('tal planilha')
pagina_empresas = empresas['dados empresas']

for linha in pagina_empresas.iter_rows(min_row=2, values_only=True): # Propriedade para passar por cada uma das linhas, values_only retorna os valores que está em cada uma dessas linhas
    nome_empresa, email, telefone, endereco, cnpj, area_atuacao, quantidade_de_funcionarios, data_fundacao = linha

    wait = WebDriverWait(driver, 10)
    nome_empresa_element = wait.until(EC.presence_of_element_located((By.ID, 'nomeEmpresa')))
    nome_empresa_element.send_keys(nome_empresa)
    sleep(1)
    driver.find_element(By.ID,'emailEmpresa').send_keys(email)
    sleep(1)
    driver.find_element(By.ID,'telefoneEmpresa').send_keys(telefone)
    sleep(1)
    driver.find_element(By.ID,'enderecoEmpresa').send_keys(endereco)
    sleep(1)
    driver.find_element(By.ID,'cnpj').send_keys(cnpj)
    sleep(1)
    driver.find_element(By.ID,'areaAtuacao').send_keys(area_atuacao)
    sleep(1)
    driver.find_element(By.ID,'numeroFuncionarios').send_keys(quantidade_de_funcionarios)
    sleep(1)
    driver.find_element(By.ID,'dataFundacao').send_keys(data_fundacao)
    sleep(1)

    driver.find_element(By.ID,'Cadastrar').click()
    sleep(3)

# 6 - Clicar em cada campo e preenche com a informação extraída

# 7 - Clicar em cadastrar

# 8 - Repito os passos 5 e 6