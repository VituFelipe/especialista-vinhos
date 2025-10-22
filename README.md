# Especialista em Vinhos e Harmonização

![Banner do Projeto](images/bannerFinal.jpg) 

## Descrição do Serviço

O "Especialista em Vinhos e Harmonização" é uma aplicação web inovadora que utiliza inteligência artificial para fornecer recomendações personalizadas de vinhos. Com base em entradas do usuário, como o tipo de prato, a ocasião, preferências de sabor e faixa de preço, e uma região opcional, a aplicação gera sugestões de vinhos ideais, incluindo detalhes como tipo, região de origem, notas de sabor e explicações de harmonização.

Este serviço é projetado para entusiastas de gastronomia, iniciantes em enologia e anfitriões de eventos, tornando o mundo dos vinhos mais acessível e agradável. A integração com a API do Gemini permite respostas inteligentes e contextuais, simulando o conselho de um sommelier profissional.

O projeto demonstra a aplicação prática de conceitos de integração entre frontend e backend, atendendo aos requisitos de desenvolvimento de um produto funcional com IA generativa.

## Funcionalidades Principais

- **Recomendações Personalizadas**: Insira o prato, ocasião, preferências (ex.: "vinho branco seco, até R$150") e região opcional para receber uma sugestão de vinho com detalhes completos.
- **Validações e Regras de Negócio**:
  - Campos obrigatórios não podem ser vazios.
  - Preferências de preço devem incluir valores numéricos.
  - Regiões limitadas a vinícolas conhecidas (ex.: Bordeaux, Marlborough) para garantir relevância.
  - Normalização de entradas (conversão para minúsculas e remoção de espaços extras).
- **Integração com IA**: Uso da API do Gemini (modelo `gemini-2.5-flash`) para gerar respostas em formato JSON estruturado.
- **Otimização de Custos**: Cache de prompts com `@lru_cache` para reduzir chamadas repetitivas à API.
- **Interface Web Intuitiva**: Formulário simples com exibição de resultados em tempo real.
- **Monitoramento**: Logs de uso de tokens e respostas brutas para depuração.

## Tecnologias Utilizadas

- **Backend**: Python 3.14 com FastAPI (API RESTful), Pydantic (validações), google-generativeai (integração com Gemini), python-dotenv (gerenciamento de variáveis de ambiente).
- **Frontend**: HTML5, CSS3, JavaScript (Fetch API para requisições assíncronas).
- **Outros**: Logging para monitoramento, Re para limpeza de respostas, Functools para cache.
- **Dependências**: Listadas no `requirements.txt` (gerado via `pip freeze > requirements.txt`).

## Instalação e Setup

### Pré-Requisitos
- Python 3.14 ou superior.
- Chave da API do Gemini obtida em [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey).

### Passos
1. **Clone o Repositório**:
   ```bash
   git clone https://github.com/VituFelipe/especialista-vinhos.git
   cd especialista-vinhos