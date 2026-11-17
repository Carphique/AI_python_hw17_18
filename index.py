import os
import chromadb
import ollama
from sentence_transformers import SentenceTransformer

chromadb_client = chromadb.PersistentClient(path="./chroma_db")
collection = chromadb_client.get_or_create_collection(name="local_base")
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

DOCS_FOLDER = "./base"

def split_text(text: str, chunk_size: int = 500, overlap: int = 100) -> list[str]:
    """Разбивает длинный текст на фрагменты с перекрытием."""
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks

print("Checking docs...")

if not os.path.exists(DOCS_FOLDER):
    os.makedirs(DOCS_FOLDER)
    print(f"Folder '{DOCS_FOLDER}' created. Put your .txt or .md files there and restart.")
else:
    for filename in os.listdir(DOCS_FOLDER):
        if filename.endswith((".txt", ".md")):
            file_path = os.path.join(DOCS_FOLDER, filename)

            existing = collection.get(where={"source": filename})
            if existing and existing["ids"]:
                print(f"File '{filename}' already indexed.")
                continue

            with open(file_path, "r", encoding="utf-8") as f:
                file_content = f.read().strip()

            if not file_content:
                continue

            chunks = split_text(file_content)
            ids = [f"{filename}_chunk_{i}" for i in range(len(chunks))]
            metadatas = [{"source": filename, "chunk": i} for i in range(len(chunks))]
            embeddings = embedding_model.encode(chunks).tolist()

            collection.add(
                documents=chunks,
                embeddings=embeddings,
                ids=ids,
                metadatas=metadatas,
            )
            print(f"Indexed '{filename}' ({len(chunks)} chunks).")

total_docs = collection.count()
if total_docs == 0:
    print("Knowledge base is empty. Add files to './base' and run again.")
    exit()

user_query = input("\nInput your question: ").strip()
if not user_query:
    user_query = "Which project uses Django and Celery?"

print("Searching...")

query_embedding = embedding_model.encode([user_query]).tolist()
results = collection.query(
    query_embeddings=query_embedding,
    n_results=min(3, total_docs),
)

retrieved_chunks = results["documents"][0]
sources = results["metadatas"][0]

print("\nRetrieved context:")
for i, (chunk, meta) in enumerate(zip(retrieved_chunks, sources)):
    print(f"[{i+1}] {meta['source']} (chunk {meta['chunk']}): {chunk[:120]}...")

context = "\n\n---\n\n".join(retrieved_chunks)

prompt = f"""Use ONLY the provided context to answer the user's question.
If the answer is not contained in the context, respond strictly with: "I don't have that information in my knowledge base."

Context:
{context}

Question:
{user_query}"""

response = ollama.chat(
    model="llama3",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant that answers questions strictly in English based only on the provided files.",
        },
        {"role": "user", "content": prompt},
    ],
)

print("\n" + "=" * 40)
print("Answer from AI:")
print("=" * 40)
print(response["message"]["content"])