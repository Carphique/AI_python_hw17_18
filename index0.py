import chromadb
from sentence_transformers import SentenceTransformer
import ollama

chromadb_client = chromadb.PersistentClient(path="./chroma_db")
collection_name = "index0_base"

collection = chromadb_client.get_or_create_collection(name=collection_name)

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

documents = [
    (
        "doc_1",
        "Architect project Opa: mobile app on React Native (Expo) with navigation, validation and work with gallery, React Hook Form"
    ),
    (
        "doc_2",
        "Architect project Pzd: backend integration and API logic, state management with Redux Toolkit, JWT user authentication, Axios for network requests"
    ),
    (
        "doc_3",
        "Architect project Pi: offline-first local database, SQLite setup with Expo file system, NetInfo for network synchronization, async data persistence"
    ),
    (
        "doc_4",
        "Architect project Say: UI/UX enhancements and styling, custom animations using React Native Reanimated, responsive layouts and flexbox, dynamic dark mode support"
    ),
    (
        "doc_5",
        "Architect project Opa: Web3 and smart contract integration, Ethers.js v6 wallet connection, decentralized features, handling blockchain transactions"
    )
]

if collection.count() == 0:
    ids = [item[0] for item in documents]
    texts = [item[1] for item in documents]
    embeddings = embedding_model.encode(texts).tolist()
    collection.add(documents=texts, embeddings=embeddings, ids=ids)

user_query = "Which docs with backend?"
query_embedding = embedding_model.encode([user_query]).tolist()

result = collection.query(query_embeddings=query_embedding, n_results=2)
retrieved_chunks = result["documents"][0]

print("Retrieved context:")
for i, chunk in enumerate(retrieved_chunks):
    print(f"[{i+1}] {chunk}")

context = "\n".join(retrieved_chunks)

prompt = f"""Use only the context provided below to answer the question.
If the answer is not in the context, say: "I do not have that information in my base."

Context:
{context}

User query:
{user_query}
"""

response = ollama.chat(
    model="llama3",
    messages=[
        {
            "role": "system",
            "content": "You are a clever corporate assistant, who answers based on the provided docs."
        },
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print("=" * 40)
print("Answer:")
print("=" * 40)
print(response["message"]["content"])