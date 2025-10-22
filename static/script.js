document.addEventListener('DOMContentLoaded', () => {
       console.log('DOM completamente carregado'); // Log para verificar se o DOM está pronto

       const form = document.getElementById('wine-form');
       if (!form) {
           console.error('Formulário com id "wine-form" não encontrado');
           return;
       }

       form.addEventListener('submit', async (e) => {
           console.log('Formulário submetido'); // Log para verificar se o evento dispara
           e.preventDefault();
           
           const dish = document.getElementById('dish').value;
           const occasion = document.getElementById('occasion').value;
           const preferences = document.getElementById('preferences').value;
           const region = document.getElementById('region').value;

           console.log('Dados do formulário:', { dish, occasion, preferences, region }); // Log dos dados

           const requestBody = { dish, occasion, preferences };
           if (region) requestBody.region = region;

           try {
               console.log('Enviando requisição para o servidor:', requestBody); // Log da requisição
               document.getElementById('result').innerHTML = '<p>Carregando...</p>';
               const response = await fetch('http://127.0.0.1:8000/recommend-wine', {
                   method: 'POST',
                   headers: { 'Content-Type': 'application/json' },
                   body: JSON.stringify(requestBody)
               });
               console.log('Resposta recebida:', response); // Log da resposta

               if (!response.ok) {
                   throw new Error(`Erro HTTP: ${response.status} ${response.statusText}`);
               }

               const data = await response.json();
               console.log('Dados parseados:', data); // Log dos dados parseados

               if (data.error) {
                   throw new Error(data.error);
               }

               const resultDiv = document.getElementById('result');
               resultDiv.innerHTML = `
                   <h2>Recomendação de Vinho</h2>
                   <p><strong>Vinho:</strong> ${data.vinho}</p>
                   <p><strong>Tipo:</strong> ${data.tipo}</p>
                   <p><strong>Região:</strong> ${data.regiao}</p>
                   <p><strong>Preço:</strong> ${data.preco}</p>
                   <p><strong>Notas de Sabor:</strong> ${data.notas_sabor}</p>
                   <p><strong>Harmonização:</strong> ${data.harmonizacao}</p>
                   <p><strong>Tokens Usados:</strong> ${data.token_usage.prompt_tokens} (entrada), ${data.token_usage.response_tokens} (saída)</p>
               `;
               resultDiv.classList.add('show');
           } catch (error) {
               console.error('Erro na requisição:', error); // Log do erro
               document.getElementById('result').innerHTML = `<p style="color: red;">Erro: ${error.message}</p>`;
               document.getElementById('result').classList.add('show');
           }
       });
   });