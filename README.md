# Especialista em Vinhos e Harmonização

## Setup
1. Instale dependências: py -3.14 -m pip install fastapi uvicorn google-generativeai python-dotenv
2. Crie .env com GOOGLE_API_KEY=sua_chave
3. Rode: py -3.14 -m uvicorn main:app --reload
4. Acesse: http://127.0.0.1:8000/static/index.html

## Funcionalidades
- Recomendações personalizades via Gemini API.
- Custo: Tier gratuito para testes(ver https://ai.google.dev/pricing).

# Limitações
- Depende da qualidade do seu prompt.