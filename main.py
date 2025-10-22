import google.generativeai as genai
import os
import json
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel, validator
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from functools import lru_cache
import logging

# Configurar logging para monitorar requisições e uso de tokens
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Carregar variáveis de ambiente
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
MODEL_NAME = "gemini-2.5-flash"

# Inicializar a aplicação FastAPI
app = FastAPI()

# Montar pasta estática para servir o front-end
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configurar CORS para permitir chamadas do front-end
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000", "http://127.0.0.1:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelo de dados para entrada do usuário com validações
class WineRequest(BaseModel):
    dish: str  # Ex.: "salmão grelhado"
    occasion: str  # Ex.: "jantar romântico"
    preferences: str  # Ex.: "vinho branco seco, até R$150"
    region: str | None = None  # Opcional: ex.: "Bordeaux"

    @validator('dish', 'occasion', 'preferences')
    def not_empty(cls, v):
        """Garante que os campos obrigatórios não sejam vazios."""
        if not v.strip():
            raise ValueError("Campo não pode ser vazio")
        return v.strip().lower()  # Normaliza: remove espaços e converte para minúsculas

    @validator('preferences')
    def check_price(cls, v):
        """Verifica se as preferências incluem um preço numérico, se especificado."""
        if 'até r$' in v.lower() and not any(char.isdigit() for char in v):
            raise ValueError("Preferências de preço devem incluir um valor numérico")
        return v

    @validator('region', allow_reuse=True)
    def valid_region(cls, v):
        """Valida se a região é uma região vinícola conhecida (opcional)."""
        if v:
            valid_regions = [
                "bordeaux", "toscana", "rioja", "marlborough", "napa valley",
                "mendoza", "alentejo", "douro", "chianti", "barolo"
            ]
            if v.lower() not in valid_regions:
                raise ValueError(f"Região inválida. Escolha entre: {', '.join(valid_regions)}")
            return v.lower()
        return v

# Função para criar prompt estruturado com cache
@lru_cache(maxsize=100)
def create_wine_prompt(dish: str, occasion: str, preferences: str, region: str | None) -> str:
    """Cria um prompt estruturado para a API do Gemini, com cache para otimizar custos."""
    prompt = f"""
    Você é um especialista em vinhos e harmonização. Recomende um vinho para harmonizar com o prato '{dish}' em uma ocasião '{occasion}'.
    Considere as preferências: '{preferences}'.
    """
    if region:
        prompt += f" Restrinja a recomendação a vinhos da região '{region}'."
    prompt += """
    Forneça a resposta em formato JSON com os campos:
    - vinho: nome do vinho (ex.: "Château Margaux")
    - tipo: tipo do vinho (ex.: "tinto", "branco")
    - regiao: região de origem
    - preco: faixa de preço aproximada em reais (ex.: "R$80-R$120")
    - notas_sabor: descrição das notas de sabor
    - harmonizacao: explicação da harmonização com o prato
    """
    return prompt

@app.post("/recommend-wine")
async def recommend_wine(request: WineRequest):
    """Endpoint para recomendar vinhos com base nos inputs do usuário."""
    try:
        model = genai.GenerativeModel(MODEL_NAME, generation_config={"temperature": 0.7})
        prompt = create_wine_prompt(request.dish, request.occasion, request.preferences, request.region)
        response = model.generate_content(prompt)
        
        # Logar uso de tokens
        tokens_used = response.usage_metadata
        logger.info(f"Tokens usados: {tokens_used.prompt_token_count} (entrada), {tokens_used.candidates_token_count} (saída)")
        
        # Extrair JSON da resposta
        result = json.loads(response.text.strip("```json\n").strip("```"))
        result["token_usage"] = {
            "prompt_tokens": tokens_used.prompt_token_count,
            "response_tokens": tokens_used.candidates_token_count
        }
        return result
    except json.JSONDecodeError:
        logger.error("Resposta do Gemini não está em formato JSON válido")
        return {"error": "Resposta do Gemini não está em formato JSON válido"}
    except Exception as e:
        logger.error(f"Erro ao processar a solicitação: {str(e)}")
        return {"error": f"Erro ao processar a solicitação: {str(e)}"}

@app.get("/models")
def list_models():
    """Lista os modelos disponíveis na API do Gemini."""
    models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    return {"models": models}