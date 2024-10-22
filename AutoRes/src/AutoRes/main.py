import requests
import json

from res_score.doctxt import doctxt
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

from dotenv import load_dotenv
import os

load_dotenv()  # Loads variables from .env into os.environ

api_key = os.getenv('API_KEY')

OPENROUTER_API_KEY = os.getenv('API_KEY')
package_dir = os.path.dirname(__file__)
resources_folder_path = os.path.join(package_dir, 'resources')
# resources_folder_path = os.path.join(os.path.dirname(__file__), '..', 'resources')
docs_path = os.path.join(resources_folder_path, 'docs')
resume_text_path = os.path.join(resources_folder_path, 'Restexts')


def get_completion(messages):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "openai/gpt-4o-mini",
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
    with open(os.path.join(resources_folder_path, 'texts', 'keywords.txt'), 'w') as file:
        file.write(keywords_response.strip())

def find_skills(chat_history):
    prompt = f"What are the skills necessary for this position that i should include in resume skills section? Do not include any introductory text or explanations."
    chat_history.append({"role": "user", "content": prompt})
    skills_response = get_completion(chat_history)
    chat_history.append({"role": "assistant", "content": skills_response})

    # Save the response to a .txt file
    with open(os.path.join(resources_folder_path, 'texts', 'skills.txt'), 'w') as file:
        file.write(skills_response.strip())

def peer_skills(chat_history):
    prompt = f"Find relevant skill sets and skill keywords typically found in resumes of professionals with same title applying for similar positions. Be inclusive, these should include all the technical, operational, and soft skills, along ith any knowledge of trends or tools commonly used! Do not include any introductory text or explanations."
    chat_history.append({"role": "user", "content": prompt})
    skills_response = get_completion(chat_history)
    chat_history.append({"role": "assistant", "content": skills_response})

    # Save the response to a .txt file
    with open(os.path.join(resources_folder_path, 'texts', 'peer_skills.txt'), 'w') as file:
        file.write(skills_response.strip())


def tailor_resume(chat_history, res_name):

    with open(os.path.join(resources_folder_path, 'texts', 'keywords.txt'), 'r') as file:
        keywords = file.read().strip()

    with open(os.path.join(resume_text_path, res_name), 'r') as file:
        resume = file.read().strip()

    prompt = f"""
    Task: Tailor my resume for the job described above by rewriting the experience and projects sections, aligning them with the job requirements.

    Instructions: Rewrite Experience Sections: Update each section on my resume to make it relevant to the job description provided. Use technical language and incorporate keywords from the job description wherever possible.

    Bullet Points Requirements:
    - Write at least 5 new bullet points for each experience.
    - Include both technical and soft skills in the bullet points.
    - Start each bullet point with a strong action verb.
    - Provide specific context, actions, and results, following the STAR method (Situation, Task, Action, Result).
    - Quantify achievements where possible, without overusing numerical details.
    - Ensure each bullet point is unique, specific, and distinct from others.

    Formatting and Relevance:
    - Use an easy-to-read format that emphasizes relevant skills and accomplishments.
    - Align the experiences to resemble those typically seen in technical sales application engineer roles.
    - Highlight the purpose, scope, and impact of my work in each bullet point.
    - Avoid repetitive phrasing or formats across different bullet points.

    Keywords: Integrate the following keywords into the bullet points to enhance alignment with the job description. Ensure the keywords from the job description are bolded.
    "{keywords}"

    Example of Effective Bullet Points: Review the example below for the type of detail and impact expected:

    Before:
    - Responsible for organizing events and panels.

    After:
    - Planned and coordinated public health panels for 25-50 undergraduates bi-monthly, showcasing organizational skills and attention to detail.
    - Identified and engaged health professionals from the community, demonstrating research and interpersonal skills.
    - Created marketing materials and promoted events via social media, which increased attendance by 75%.

    Key Improvements:
    - Added context and specific actions taken.
    - Highlighted skills and the scope of work.
    - Demonstrated impact through quantifiable results.

    Focus on Results and Impact: When possible, add accomplishments or impact statements to bullet points, illustrating how my actions benefited the organization.

    Resume: "{resume}"
    """

    chat_history.append({"role": "user", "content": prompt})
    tailored_resume_response = get_completion(chat_history)
    chat_history.append({"role": "assistant", "content": tailored_resume_response})

    # Save the response to a .txt file
    with open(os.path.join(resources_folder_path, 'texts', 'tailored_res.txt'), 'w') as file:
        file.write(tailored_resume_response.strip())


def find_best_resume(txt_folder_path, jd_txt_path):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = {}
    
    # Generate embeddings for resumes
    for filename in os.listdir(txt_folder_path):
        if filename.endswith(".txt"):
            txt_path = os.path.join(txt_folder_path, filename)
            with open(txt_path, 'r', encoding='utf-8') as file:
                text = file.read()
                embedding = model.encode(text)
                embeddings[filename] = embedding
    
    # Embed job description
    job_embedding = model.encode(jd_txt_path)
    
    # Calculate similarity scores
    similarities = {}
    for filename, resume_embedding in embeddings.items():
        similarity = cosine_similarity([job_embedding], [resume_embedding])[0][0]
        similarities[filename] = similarity
    
    # Find the best matching resume
    best_filename = max(similarities, key=similarities.get)
    return best_filename, similarities[best_filename]

def doc_to_txt(resume_path, output_path):
    for filename in os.listdir(resume_path):
        if filename.endswith(".docx"):
            docx_path = os.path.join(resume_path, filename)
            txt_path = os.path.join(output_path, os.path.splitext(filename)[0] + ".txt")
            doctxt(docx_path, txt_path)




# Example usage
# Read the job description from a text file
with open(os.path.join(resources_folder_path, 'texts', 'jd.txt'), 'r') as file:
    job_description = file.read()
chat_history = []

analyze_job_description(job_description, chat_history)  # Initialize context
extract_keywords(chat_history)  # Extract and save keywords
find_skills(chat_history)
peer_skills(chat_history)

doc_to_txt(docs_path, resume_text_path)
resume = find_best_resume(resume_text_path, os.path.join(resources_folder_path, 'texts', 'jd.txt'))

tailor_resume(chat_history, resume[0])