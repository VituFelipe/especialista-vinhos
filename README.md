# 🍷 Especialista em Vinhos e Harmonização

![Banner do Projeto](images/bannerFinal.png)

## 📝 Descrição do Serviço

O **Especialista em Vinhos e Harmonização** é uma aplicação web inovadora que utiliza **inteligência artificial** para fornecer recomendações personalizadas de vinhos.  
Com base em entradas do usuário — como o tipo de prato, ocasião, preferências de sabor, faixa de preço e região opcional — a aplicação gera sugestões ideais com detalhes sobre **tipo, origem, notas de sabor e justificativa da harmonização**.

O serviço foi criado para **entusiastas de gastronomia**, **iniciantes em enologia** e **anfitriões de eventos**, tornando o mundo dos vinhos mais acessível e prazeroso.  
A integração com a **API do Gemini** permite respostas inteligentes e contextuais, simulando o conselho de um **sommelier profissional**.

Este projeto demonstra a aplicação prática de integração entre **frontend e backend**, atendendo aos requisitos de um produto funcional com IA generativa.

---

## ⚙️ Funcionalidades Principais

- **Recomendações Personalizadas**  
  Informe prato, ocasião, preferências (ex.: “vinho branco seco, até R$150”) e uma região opcional para receber sugestões completas.

- **Validações e Regras de Negócio**
  - Campos obrigatórios não podem estar vazios.
  - Preferências de preço devem conter valores numéricos.
  - Regiões limitadas a vinícolas conhecidas (ex.: *Bordeaux*, *Marlborough*).
  - Normalização de entradas (letras minúsculas e remoção de espaços extras).

- **Integração com IA**  
  Uso do modelo `gemini-2.5-flash` para gerar respostas estruturadas em JSON.

- **Otimização de Custos**  
  Cache inteligente com `@lru_cache` para evitar chamadas repetidas à API.

- **Interface Web Intuitiva**  
  Formulário limpo, simples e responsivo com exibição imediata dos resultados.

- **Monitoramento**  
  Logs detalhados de uso de tokens e respostas brutas para depuração.

---

## 🧰 Tecnologias Utilizadas

| Categoria | Tecnologias |
|------------|-------------|
| **Backend** | Python 3.14, FastAPI, Pydantic, google-generativeai, python-dotenv |
| **Frontend** | HTML5, CSS3, JavaScript (Fetch API) |
| **Outros** | Logging, Expressões Regulares (Re), Functools (Cache) |
| **Dependências** | Listadas em `requirements.txt` |

---

## 🧑‍💻 Instalação e Setup

### 🔧 Pré-requisitos

- Python **3.14** ou superior  
- Chave da API do **Gemini**, obtida em:  
  👉 [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)

---

### 🚀 Passos de Instalação

1. **Clone o Repositório**
   ```bash
   git clone https://github.com/VituFelipe/especialista-vinhos.git
   cd especialista-vinhos
   ```

2. **Instale as Dependências**
   ```bash
   py -3.14 -m pip install fastapi uvicorn google-generativeai python-dotenv
   ```
   Ou utilize o arquivo `requirements.txt`:
   ```bash
   py -3.14 -m pip install -r requirements.txt
   ```

3. **Configure a Chave da API**
   Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:
   ```text
   GOOGLE_API_KEY=sua_chave_aqui
   ```

4. **Inicie o Servidor**
   ```bash
   py -3.14 -m uvicorn main:app --reload
   ```

5. **Acesse a Interface**
   Abra o navegador e acesse:  
   👉 [http://127.0.0.1:8000/static/index.html](http://127.0.0.1:8000/static/index.html)

---

## 🍇 Uso da Aplicação

1. **Abra a aplicação:**  
   [http://127.0.0.1:8000/static/index.html](http://127.0.0.1:8000/static/index.html)

2. **Preencha o Formulário:**
   - **Prato:** `salmão grelhado`
   - **Ocasião:** `jantar romântico`
   - **Preferências:** `vinho branco seco, até R$150`
   - **Região (opcional):** `marlborough`

3. **Clique em “Recomendar Vinho”**  
   A IA retornará informações detalhadas de harmonização.

---

### 🧾 Exemplo de Resposta JSON

```json
{
  "vinho": "Villa Maria Private Bin Sauvignon Blanc",
  "tipo": "branco",
  "regiao": "Marlborough, Nova Zelândia",
  "preco": "R$120-R$180",
  "notas_sabor": "Aromas intensos de maracujá, groselha, lima, toranja e um toque herbáceo.",
  "harmonizacao": "O Sauvignon Blanc de Marlborough é uma escolha clássica para salmão grelhado, equilibrando a riqueza do prato.",
  "token_usage": {
    "prompt_tokens": 193,
    "response_tokens": 267
  }
}
```

---

## 🗂️ Estrutura do Projeto

| Arquivo / Pasta | Descrição |
|------------------|------------|
| `main.py` | API backend com FastAPI e integração Gemini |
| `static/index.html` | Interface web |
| `static/styles.css` | Estilos da interface |
| `static/script.js` | Lógica de requisição e exibição de resultados |
| `.env` | Chave de API do Gemini |
| `.gitignore` | Ignora arquivos sensíveis e temporários |
| `requirements.txt` | Dependências do Python |
| `apresentacao.pptx` | Slides com explicação do projeto |
| `README.md` | Documentação do projeto |

---

## 💰 Custos e Otimização

- **Tier gratuito do Gemini API:**
  - 1.500 requisições/hora (~15 por minuto)  
  - 1 milhão de tokens de entrada  
  - 4 mil tokens de saída  

- **Custo adicional (fora do tier gratuito):**
  - US$0,35 por 1M tokens de entrada (segundo tabela oficial da Google)

- **Otimização incluída:**
  - Cache de prompts (`@lru_cache`) para evitar chamadas repetidas  
  - Ideal para **uso acadêmico e demonstrações**

---

## ⚠️ Limitações

- Necessita **conexão com a internet** para acessar a API Gemini.  
- Respostas da IA podem ser **malformadas ocasionalmente** (tratadas no backend).  
- **Regiões vinícolas limitadas**, podendo ser expandidas futuramente.  
- Ainda **não inclui suporte a imagens** ou **histórico de recomendações**.  
- A precisão depende diretamente da **qualidade do prompt**.

---

## 🎓 Apresentação Acadêmica

O arquivo `apresentacao.pptx` inclui:

- Conceito e objetivos do produto  
- Arquitetura geral do sistema  
- Fluxo de integração com o Gemini  
- Regras de negócio e validações  
- Capturas de tela e exemplo prático de execução  

---

## 🤝 Contribuição

Contribuições são **muito bem-vindas!**

1. Faça um **fork** do repositório  
2. Crie uma nova branch:
   ```bash
   git checkout -b feature/nova-funcionalidade
   ```
3. Faça commit das alterações:
   ```bash
   git commit -am "Adiciona nova funcionalidade"
   ```
4. Envie para o repositório remoto:
   ```bash
   git push origin feature/nova-funcionalidade
   ```
5. Crie um **Pull Request** ✨

---

## 📄 Licença

Este projeto está sob a licença **MIT**.  
Consulte o arquivo `LICENSE` para mais detalhes.

---

🧑‍🍳 *Desenvolvido com FastAPI, Python e uma taça de vinho.*
