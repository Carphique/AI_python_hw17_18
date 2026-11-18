import os
import random

prefixes = [
    "Alpha", "Beta", "Gamma", "Delta", "Omega", "Nexus", "Vertex", "Zenith",
    "Apex", "Matrix", "Vector", "Echo", "Mirage", "Titan", "Pioneer", "Orbit",
    "Stellar", "Core", "Flux", "Horizon", "Vanguard", "Synergy", "Beacon",
    "Quantum", "Pulse", "Nova", "Aether", "Stratos", "Prism", "Helios"
]

domains = [
    "fintech banking portal", "healthcare telemedicine platform", "logistics fleet tracker",
    "e-commerce marketplace", "cybersecurity threat monitor", "edtech learning management system",
    "smart home IoT controller", "real estate booking engine", "autonomous drone telemetry hub",
    "AI content moderation service", "supply chain analytics dashboard", "crypto portfolio tracker",
    "cloud storage sync client", "video streaming backend", "HR recruitment automation tool",
    "energy grid load balancer", "retail POS inventory system", "social media scheduler"
]

architectures = [
    "event-driven microservices architecture",
    "serverless cloud-native backend",
    "modular monolith with clean architecture",
    "distributed CQRS and Event Sourcing system",
    "cross-platform mobile and web ecosystem",
    "high-throughput real-time streaming pipeline",
    "offline-first local-sync desktop application",
    "multi-tenant SaaS platform"
]

languages_frameworks = [
    "Python (FastAPI & SQLAlchemy)", "Go (Gin & gRPC)", "Node.js (NestJS & TypeScript)",
    "C# (.NET 10 & Entity Framework)", "Java (Spring Boot & WebFlux)", "Rust (Actix-web & Tokio)",
    "React Native (Expo & TypeScript)", "Flutter (Dart & Bloc)", "Vue 3 (Pinia & Vite)",
    "Python (PyTorch & Ray)", "Scala 3 (Akka & ZIO)", "Next.js (App Router & Prisma)"
]

databases = [
    "PostgreSQL with pgvector", "MongoDB replica set", "Redis Cluster & ClickHouse",
    "Apache Cassandra", "SQLite with SQLCipher encryption", "Neo4j graph database",
    "TimescaleDB for time-series", "DynamoDB with DAX caching", "Elasticsearch & Kibana"
]

infra_tools = [
    "Docker, Kubernetes, and Terraform",
    "GitHub Actions CI/CD and AWS ECS",
    "Prometheus, Grafana, and OpenTelemetry",
    "Apache Kafka message broker and RabbitMQ",
    "Nginx reverse proxy and Cloudflare Workers",
    "HashiCorp Vault for secrets and OAuth2/OIDC",
    "ArgoCD GitOps and Helm charts",
    "Sentry error tracking and Loki log aggregation"
]

key_features = [
    "automated end-to-end integration testing",
    "zero-downtime blue-green deployments",
    "end-to-end AES-256 data encryption",
    "sub-50ms API response latency optimization",
    "role-based access control (RBAC) and audit logs",
    "automated horizontal pod autoscaling",
    "real-time WebSocket push notifications",
    "multi-region disaster recovery backups",
    "rate limiting and DDoS mitigation middleware",
    "AI-powered anomaly detection alerts"
]

used_texts = set()
documents = []

while len(documents) < 1000:
    doc_id = f"doc_{len(documents) + 1}"
    project_name = f"{random.choice(prefixes)}_{random.randint(100, 9999)}"
    
    domain = random.choice(domains)
    arch = random.choice(architectures)
    stack = random.choice(languages_frameworks)
    db = random.choice(databases)
    infra = random.choice(infra_tools)
    feat1, feat2 = random.sample(key_features, 2)

    text = (
        f"Project {project_name} is a {domain} built using {arch}. "
        f"Core stack: {stack} with {db} for persistence. "
        f"Infrastructure relies on {infra}, featuring {feat1} and {feat2}."
    )

    if text not in used_texts:
        used_texts.add(text)
        documents.append((doc_id, text))

os.makedirs("base", exist_ok=True)
output_path = os.path.join("base", "dataset.md")

with open(output_path, "w", encoding="utf-8") as f:
    f.write("# Unique Projects Knowledge Base (1000 items)\n\n")
    for doc_id, text in documents:
        f.write(f"## `{doc_id}`\n\n{text}\n\n---\n\n")

print(f"Готово! Сгенерировано {len(documents)} полностью уникальных документов в {output_path}")