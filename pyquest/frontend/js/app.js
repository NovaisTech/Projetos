/* ==============================================================================
   ETAPA 13: O CÉREBRO DO JOGO (JavaScript + FastAPI)
   ============================================================================== */

// 1. URL base da nossa API FastAPI rodando no seu computador
const API_URL = "http://127.0.0.1:8000/api";

// 2. Espera o HTML carregar completamente antes de rodar o script
document.addEventListener("DOMContentLoaded", () => {
  carregarFases();
  configurarBotaoPrincipal();
});

// 3. Função que faz a REQUISIÇÃO (fetch) para o FastAPI
async function carregarFases() {
  try {
    // Faz a chamada HTTP GET para /api/levels
    const resposta = await fetch(`${API_URL}/levels`);

    // Converte a resposta recebida em formato JSON
    const fases = await resposta.json();

    // Pega a caixinha onde as fases devem morar
    const trackContainer = document.getElementById("levelsTrack");

    // Limpa qualquer conteúdo anterior
    trackContainer.innerHTML = "";

    // Para cada fase retornada pela API, criamos o HTML correspondente
    fases.forEach((fase) => {
      const card = document.createElement("div");
      card.className = "level-item";

      // Quando clicar no card da fase, atualiza o botão principal
      card.onclick = () => selecionarFase(fase);

      card.innerHTML = `
                <div class="level-icon-box">
                    <span class="level-badge" style="background-color: ${fase.cor_badge}">${fase.badge}</span>
                    <span>${fase.icone}</span>
                </div>
                <div class="level-info">
                    <span class="level-title">${fase.titulo}</span>
                    <span class="level-tasks">📜 ${fase.tarefas} tarefas</span>
                    <span class="level-difficulty">⭐ ${fase.dificuldade}</span>
                </div>
            `;

      // Adiciona o card dentro da coluna esquerda
      trackContainer.appendChild(card);
    });
  } catch (erro) {
    console.error("Erro ao carregar as fases da API:", erro);
  }
}

// 4. Interatividade: quando clica na fase, muda o botão inferior
function selecionarFase(fase) {
  const botao = document.getElementById("startLevelBtn");
  botao.innerText = `START ${fase.badge} 👆`;
}

// 5. Configuração do clique no botão principal
function configurarBotaoPrincipal() {
  const botao = document.getElementById("startLevelBtn");
  botao.addEventListener("click", () => {
    alert("🎮 Iniciando desafio no PyQuest! Prepare seu código Python!");
  });
}
