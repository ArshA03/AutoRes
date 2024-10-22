import requests
import json

# Replace with your actual API key
OPENROUTER_API_KEY = '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'

def get_completion(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "openai/gpt-4o",  # You can choose different models if needed
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        completion = response.json()
        return completion.get('choices')[0].get('message').get('content')
    else:
        return f"Error: {response.status_code} - {response.text}"

# Example usage
prompt = "Write a cover letter for a software engineering position."
result = get_completion(prompt)
print(result)