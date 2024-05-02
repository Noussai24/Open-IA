"c'est un script py pour tester l'accès à l'API GPT-4 sur OpenAI :  avec votre clé"
import requests

def query_gpt4(prompt):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer votre_clé_api",
        "Content-Type": "application/json",
    }
    data = {
        "model": "gpt-4",
        "messages": [{"role": "user", "content": prompt}]
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()

if __name__ == "__main__":
    prompt = "Hello, world!"
    response = query_gpt4(prompt)
    print(response)