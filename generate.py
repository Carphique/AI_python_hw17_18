import random

# Базовые списки для генерации разнообразных комбинаций
project_names = [
    "Alpha", "Beta", "Gamma", "Delta", "Omega", "Nexus", "Vertex", "Zenith", 
    "Apex", "Matrix", "Vector", "Echo", "Mirage", "Titan", "Pioneer", "Orbit",
    "Stellar", "Core", "Flux", "Horizon", "Vanguard", "Synergy", "Beacon"
]

categories = [
    ("mobile app on Flutter", "with Bloc state management, Firebase auth, and local database"),
    ("e-commerce platform on Django", "with PostgreSQL, Celery task queue, and Redis caching"),
    ("dashboard on Vue.js", "with Pinia, Tailwind CSS, and REST API integration"),
    ("microservice on Go (Golang)", "with gRPC, PostgreSQL, and Prometheus monitoring"),
    ("machine learning pipeline in Python", "with PyTorch, Hugging Face transformers, and FastAPI"),
    ("desktop app on Electron", "with React, TypeScript, and SQLite local storage"),
    ("smart contract on Solidity", "with Hardhat testing, OpenZeppelin, and Web3.js"),
    ("DevOps pipeline", "with GitHub Actions, Docker, Kubernetes, and Terraform")
]

documents = []

# Генерируем 1000 документов
for i in range(1, 1001):
    doc_id = f"doc_{i}"
    name = random.choice(project_names) + "_" + str(i)
    tech_stack, details = random.choice(categories)
    
    # Формируем текст документа в том же стиле
    text = (
        f"Architect project {name}: {tech_stack} "
        f"{details} with automated testing, CI/CD integration, "
        f"and performance optimization"
    )
    
    documents.append((doc_id, text))

# 1. Сохранение в один общий текстовый файл (txt)
with open("documents.txt", "w", encoding="utf-8") as f:
    for doc_id, text in documents:
        f.write(f"ID: {doc_id}\nText: {text}\n" + "-"*50 + "\n")

# 2. Сохранение в один общий Markdown-файл (md)
with open("documents.md", "w", encoding="utf-8") as f:
    f.write("# Generated Documents Database (1000 items)\n\n")
    for doc_id, text in documents:
        f.write(f"## `{doc_id}`\n\n{text}\n\n---\n\n")

print(f"Успешно сгенерировано и сохранено документов: {len(documents)}")
print("Файлы созданы: documents.txt и documents.md")
