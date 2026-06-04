import os
import requests
from dotenv import load_dotenv

# .env dosyasını yükle
load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")


def ai_analyze(data):
    """
    Nmap ve banner sonuçlarını AI'a gönderip analiz alır
    """

    # API key kontrolü
    if not API_KEY:
        return "HATA: GROQ_API_KEY .env dosyasında bulunamadı"

    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = f"""
Sen bir siber güvenlik uzmanısın.

Aşağıdaki ağ tarama sonuçlarını analiz et:

1. Açık portları değerlendir
2. Olası güvenlik risklerini belirt
3. Servis zafiyetleri hakkında yorum yap
4. Kısa ve net öneriler ver

VERİ:
{data}
"""

    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3
    }

    try:
        response = requests.post(url, headers=headers, json=payload)

        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            return f"AI ERROR: {response.text}"

    except Exception as e:
        return f"REQUEST ERROR: {str(e)}"
