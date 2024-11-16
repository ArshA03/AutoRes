from res_score.doctxt import doctxt
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

import os

folder_path = "tests/resources/docs/"
output_folder_path = "tests/resources/Restexts/"

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


for filename in os.listdir(folder_path):
    if filename.endswith(".docx"):
        docx_path = os.path.join(folder_path, filename)
        txt_path = os.path.join(output_folder_path, os.path.splitext(filename)[0] + ".txt")
        doctxt(docx_path, txt_path)

resume = find_best_resume(output_folder_path, "tests/resources/texts/jd.txt")


