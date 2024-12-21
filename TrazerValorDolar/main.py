import time
import customtkinter as ctk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Função para buscar o valor do dólar
def buscar_valor_dolar():
    # Configura o driver do Selenium
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        # Acessa o Google e pesquisa pelo valor do dólar
        driver.get("https://www.google.com")
        time.sleep(2)  # Aguarda o carregamento da página

        barra_pesquisa = driver.find_element(By.NAME, "q")
        barra_pesquisa.send_keys("valor do dólar hoje")
        barra_pesquisa.send_keys(Keys.RETURN)
        time.sleep(2)  # Aguarda os resultados aparecerem

        # Extrai o valor do dólar
        resultado = driver.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').text
        return resultado

    except Exception as e:
        return f"Erro ao buscar o valor do dólar: {e}"

    finally:
        driver.quit()

# Interface gráfica usando customtkinter
def exibir_interface():
    def atualizar_valor():
        label_valor.configure(text="Buscando...")
        janela.update_idletasks()
        valor = buscar_valor_dolar()
        label_valor.configure(text=valor)

    janela = ctk.CTk()
    janela.geometry("400x200")
    janela.title("Valor do Dólar")

    titulo = ctk.CTkLabel(janela, text="Cotação do Dólar", font=("Arial", 20))
    titulo.pack(pady=10)

    label_valor = ctk.CTkLabel(janela, text="Clique no botão para atualizar", font=("Arial", 16))
    label_valor.pack(pady=10)

    botao_atualizar = ctk.CTkButton(janela, text="Atualizar", command=atualizar_valor)
    botao_atualizar.pack(pady=10)

    janela.mainloop()

# Executa o programa
if __name__ == "__main__":
    exibir_interface()
