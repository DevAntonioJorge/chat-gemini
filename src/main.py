import pandas as pd
from dotenv import load_dotenv
from google import genai
import os

load_dotenv()
api_key = os.getenv("API_KEY")

emotion_labels = {
    1: 'Alegria', 2: 'Tristeza', 3: 'Raiva', 4: 'Medo',
    5: 'Surpresa', 6: 'Nojo', 7: 'Amor', 8: 'Gratidão',
    9: 'Esperança', 10: 'Frustração', 11: 'Ansiedade',
    12: 'Calma', 13: 'Empolgação', 14: 'Decepção'
}

def handleClient():
    try:
        client = genai.Client(api_key=api_key)
        return client
    except Exception as e:
        print(f'Erro: {e}')

def analisar_sentimento(texto, client):
    try:
        prompt = f"Qual é a emoção predominante neste texto? \n\"{texto}\""
        response = client.models.generate_content(
            model='gemini-2.0-flash-001', contents=prompt
        )
        return response.text.strip()
    except Exception as e:
        print(f"Erro ao analisar texto: {e}")
        return None

def processar_csv(caminho_csv):
    client = handleClient()
    df = pd.read_csv(caminho_csv)
    print(f"\n📄 Lendo arquivo: {caminho_csv}\n")

    for index, row in df.iterrows():
        texto = row['texto']
        codigo_emocao = row['emocao']
        nome_emocao = emotion_labels.get(codigo_emocao, 'Desconhecida')

        print(f"\n📝 Texto: {texto}")
        print(f"🎯 Emoção esperada: {nome_emocao}")

        resposta = analisar_sentimento(texto, client)
        print(f"🤖 Gemini respondeu: {resposta}")
        print("-" * 50)

def menu():
    print("========= Análise de Sentimentos =========")
    caminho = input("Digite o caminho do CSV: ")
    if os.path.exists(caminho):
        processar_csv(caminho)
    else:
        print("❌ Arquivo não encontrado.")

menu()
