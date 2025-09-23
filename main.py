import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

df = pd.read_csv('assignment2dataset.csv')
df['text'] = df['title'] + ". " + df['description']
model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = model.encode(df['text'].tolist(), show_progress_bar=True)
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

def recommend_courses(profile: str, completed_ids: list) -> list:
    profile_embedding = model.encode([profile])[0]
    distances, indices = index.search(np.array([profile_embedding]), k=5)
    results = [(df.iloc[idx]['course_id'], float(dist)) for idx, dist in zip(indices[0], distances[0]) if df.iloc[idx]['course_id'] not in completed_ids]
    return results
