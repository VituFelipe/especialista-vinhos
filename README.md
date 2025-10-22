# Especialista em Vinhos e Harmonização

Aplicação web que recomenda vinhos personalizados usando a API do Gemini.

## Setup
1. Instale dependências: `py -3.14 -m pip install fastapi uvicorn google-generativeai python-dotenv`
2. Crie `.env` com `GOOGLE_API_KEY=sua_chave`
3. Rode: `py -3.14 -m uvicorn main:app --reload`
4. Acesse: `http://127.0.0.1:8000/static/index.html`

## Funcionalidades
- Recomendações de vinhos com base em prato, ocasião, preferências e região.
- Validações de entrada e cache para otimizar custos.
- Integração com Gemini API (modelo gemini-2.5-flash).

## Custos
- Usa tier gratuito (1.500 req/hora, 1M tokens entrada, 4K saída).
- Cache reduz chamadas repetitivas.

## Limitações
- Dependência da qualidade do prompt.
- Requer conexão à internet.
- Respostas do Gemini podem ser malformadas ocasionalmente.