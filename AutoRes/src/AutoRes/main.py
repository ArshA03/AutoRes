import requests
import json

OPENROUTER_API_KEY = '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'

def get_completion(messages):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "openai/gpt-4o",
        "messages": messages
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        completion = response.json()
        return completion.get('choices')[0].get('message').get('content')
    else:
        return f"Error: {response.status_code} - {response.text}"

def analyze_job_description(job_description, chat_history):
    prompt = f"You are a career coach with 10 years of experience refining resumes for applicants. Analyze the following job description in detail;\n{job_description}"
    chat_history.append({"role": "user", "content": prompt})
    analysis = get_completion(chat_history)
    chat_history.append({"role": "assistant", "content": analysis})

def extract_keywords(chat_history):
    prompt = "List all essential keywords from the job description, including subjects, topics, and functions. Do not include any introductory text or explanations."
    chat_history.append({"role": "user", "content": prompt})
    keywords_response = get_completion(chat_history)
    chat_history.append({"role": "assistant", "content": keywords_response})
    
    # Save the response to a .txt file
    with open('tests/keywords.txt', 'w') as file:
        file.write(keywords_response.strip())

def find_skills(chat_history):
    prompt = f"What are the skills necessary for this position that i should include in resume skills section? Do not include any introductory text or explanations."
    chat_history.append({"role": "user", "content": prompt})
    skills_response = get_completion(chat_history)
    chat_history.append({"role": "assistant", "content": skills_response})

    # Save the response to a .txt file
    with open('tests/skills.txt', 'w') as file:
        file.write(skills_response.strip())

def peer_skills(chat_history):
    prompt = f"Find relevant skill sets and skill keywords typically found in resumes of professionals with same title applying for similar positions. Be inclusive, these should include all the technical, operational, and soft skills, along ith any knowledge of trends or tools commonly used! Do not include any introductory text or explanations."
    chat_history.append({"role": "user", "content": prompt})
    skills_response = get_completion(chat_history)
    chat_history.append({"role": "assistant", "content": skills_response})

    # Save the response to a .txt file
    with open('tests/peer_skills.txt', 'w') as file:
        file.write(skills_response.strip())

    
# Example usage
# Read the job description from a text file
with open('tests/jd.txt', 'r') as file:
    job_description = file.read()
chat_history = []

analyze_job_description(job_description, chat_history)  # Initialize context
extract_keywords(chat_history)  # Extract and save keywords
find_skills(chat_history)
peer_skills(chat_history)
