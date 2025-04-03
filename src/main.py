from google import genai
from dotenv import load_dotenv
import os
import datetime

load_dotenv()  
api_key = os.getenv("API_KEY")

def handleClient():
    try:
        client = genai.Client(api_key=api_key)
        return client
    except Exception as e:
        print(f'Érror:{e}')
        
        
def handlePrompt() -> None:
    while True:
        try:
            prompt = input("Digite algo: ")
            return prompt
        except Exception as e:
            print(f'Error: {e}')
            
def handleResponse():
    
    client = handleClient()
    prompt = handlePrompt()
    try:
        response = client.models.generate_content(
            model='gemini-2.0-flash-001', contents=prompt
        )
        
        print(response.text)
        return response.text
    except Exception as e:
        print(f"Error:{e}")


def save_response(response_text):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"response_{timestamp}.txt"
    filepath = os.path.join("src/archives", filename)

    if not os.path.exists("archives"):
        os.makedirs("archives")

    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(response_text)
        print(f"Resposta salva em: {filepath}")
    except Exception as e:
        print(f"Erro ao salvar a resposta: {e}")
        
        
def main():
    while True:
        response  = handleResponse()
        save_response(response)
        print('---------------------------------------------------')
        try:
            opts = input("Deseja continuar? (s/n): ").lower()
            if opts == 'n':
                break
            
            elif opts != 's':
                print("Opção inválida, tente novamente.")
        except Exception as e:
            print(f'Error: {e}')
            
def menu():
    while True:
        
        print('---------------------------------------------------')
        print('Bem vindo ao Gemini Terminal Edition')
        print('O que deseja fazer?')
        print('1 - Executar o gemini\n2-Mostrar arquivos\n3 - Sair')
        
        try:
            opts = int(input("Digite 1 ou 2: "))
        except ValueError:
            print('Digite Novamente')
            
        match(opts):
            case 1:
                main()
            case 2:
                print("Mostrando arquivos")
                try:
                    #TODO: Implementar o comando para mostrar os arquivos
                    os.system('ls')
                except Exception as e:
                    print(f'Error: {e}')
            case 3:
                print("Volte sempre")
                break

menu()