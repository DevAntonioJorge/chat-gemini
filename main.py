from google import genai
from dotenv import load_dotenv
import os

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
    except Exception as e:
        print(f"Error:{e}")
        
def main():
    while True:
        
        print('---------------------------------------------------')
        print('Bem vindo ao Gemini Terminal Edition')
        print('O que deseja fazer?')
        print('1 - Executar o gemini\n2 - Sair')
        
        try:
            opts = int(input("Digite 1 ou 2: "))
        except ValueError:
            print('Digite Novamente')
            
        match(opts):
            case 1:
                handleResponse()
            case 2:
                print("Volte sempre")
                break

main()