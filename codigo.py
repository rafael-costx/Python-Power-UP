import pyautogui
import time
import os
# pyautogui.click = clicar em algum lugar
# pyautogui.press = apertar uma tecla
# pyautogui.write = escrever um texto
# pyautogui.hotkey -> combinação de teclas
pyautogui.PAUSE = 1 # definir uma config, PAUSAR 0,5 seg

caminho_csv = r"C:\Users\rafae\Downloads\programmer\Python Power Up\produtos.csv"

# Verifica se o arquivo existe
if not os.path.exists(caminho_csv):
    print(f"Arquivo não encontrado: {caminho_csv}")
    print("Verifique se o arquivo está no caminho correto e tente novamente.")
    exit()  # encerra o script


# Passo 1: Entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")

# digitar o site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3) #delay de 3 segundos

# Passo 2: Fazer Login
pyautogui.press('tab')
pyautogui.write('pythonimpressionador@gmail.com')

# passa para o próximo campo
pyautogui.press("tab")

#preencher a senha
pyautogui.write("sua senha")

# passar para botão login
pyautogui.press("tab")

# botao logar
pyautogui.press("enter")
time.sleep(3)

# Passo 3: Importar a base de dados
import pandas as pd

tabela = pd.read_csv(r'C:\Users\rafae\Downloads\programmer\Python Power Up\produtos.csv')

print(tabela)


# Passo 4: Cadastrar 1 produto
for linha in tabela.index:

    # clicar no campo de código
    pyautogui.click(x=621, y=329)
    time.sleep(1)

    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = str(tabela.loc[linha, "codigo"])

    # preencher o campo
    pyautogui.write(codigo)
    # passar para o proximo campo
    pyautogui.press("tab")

    # preencher o campo
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")

    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")

    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")

    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")

    # cadastra o produto (botao enviar)
    pyautogui.press("enter") # cadastra o produto (botao enviar)

    # dar scroll de tudo pra cima
    pyautogui.scroll(10000)

# Passo 5: Repetir para todos os produtos
# pyautogui -> fazer automações em python