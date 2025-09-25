# Agentfirst + Nanda Adapter (HW2, Tech Track)

## What this agent does
This agent is designed to **answer questions as if it were me**, based on my resume and LinkedIn profile.  
In the current implementation it works as a **Message Improver** — it rewrites incoming text to be shorter, clearer, and more professional.  
The next step is to extend it with **RAG (retrieval-augmented generation)** over my CV and LinkedIn data.

---

## Architecture
- **Cloud**: AWS EC2 (Ubuntu 24.04)  
- **Adapter**: Nanda Adapter (Agent-to-Agent protocol)  
- **LLM**: Anthropic Claude (via `langchain-anthropic`)  
- **Domain**: [agent.alexershov.tech](https://agent.alexershov.tech)  
- **TLS**: Let’s Encrypt (Certbot)  

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/ErshovAlexey/Agentfirst.git
cd Agentfirst
