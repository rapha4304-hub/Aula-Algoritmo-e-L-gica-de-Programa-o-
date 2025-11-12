import random

# --- 1. CRITÉRIOS DE QUALIDADE E CONSTANTES ---

# Padrões de Qualidade
PESO_MIN = 95
PESO_MAX = 105
CORES_PERMITIDAS = ['azul', 'verde']
COMPRIMENTO_MIN = 10
COMPRIMENTO_MAX = 20

# Configuração da Linha
CAPACIDADE_CAIXA = 10

# --- 2. FUNÇÃO DE INSPEÇÃO DA PEÇA ---


def inspecionar_peca(peca):
    """
    Avalia uma peça com base nos critérios de qualidade.
    Retorna o status ('Aprovada' ou 'Reprovada') e uma lista de motivos.
    """
    motivos_reprovacao = []

    # Critério 1: Peso
    if not (PESO_MIN <= peca['peso'] <= PESO_MAX):
        motivos_reprovacao.append(f"Peso fora do padrão ({peca['peso']:.2f}g)")

    # Critério 2: Cor
    if peca['cor'] not in CORES_PERMITIDAS:
        motivos_reprovacao.append(f"Cor inválida ({peca['cor']})")

    # Critério 3: Comprimento
    if not (COMPRIMENTO_MIN <= peca['comprimento'] <= COMPRIMENTO_MAX):
        motivos_reprovacao.append(
            f"Comprimento fora do padrão ({peca['comprimento']:.2f}cm)")

    # Resultado final da inspeção
    if not motivos_reprovacao:
        return 'Aprovada', []
    else:
        return 'Reprovada', motivos_reprovacao

# --- 3. FUNÇÕES DE SIMULAÇÃO (Para testar o protótipo) ---


def gerar_peca_simulada(id_peca):
    """Gera dados de uma peça aleatória para simular a linha de produção."""
    # Gera dados que podem ou não estar dentro dos padrões
    peso_simulado = random.uniform(90, 110)  # Faixa de 90g a 110g
    cor_simulada = random.choice(['azul', 'verde', 'vermelho', 'amarelo'])
    comprimento_simulado = random.uniform(8, 22)  # Faixa de 8cm a 22cm

    return {
        'id': id_peca,
        'peso': peso_simulado,
        'cor': cor_simulada,
        'comprimento': comprimento_simulado
    }

# --- 4. FUNÇÃO DE RELATÓRIO ---


def exibir_relatorio_final(total_aprovadas, total_reprovadas, contagem_motivos, caixas_usadas, pecas_ultima_caixa):
    """Exibe o relatório consolidado da produção."""
    print("\n" + "="*40)
    print("    📊 RELATÓRIO FINAL DE PRODUÇÃO 📊")
    print("="*40)

    print(f"\n✅ Total de Peças Aprovadas: {total_aprovadas}")
    print(f"❌ Total de Peças Reprovadas: {total_reprovadas}")

    print("\n--- Motivos de Reprovação (Contagem Total) ---")
    if not contagem_motivos:
        print("Nenhuma peça reprovada.")
    else:
        # Usamos .get() para contar os motivos de forma segura
        for motivo in ["Peso", "Cor", "Comprimento"]:
            count = contagem_motivos.get(motivo, 0)
            print(f"  • {motivo} fora do padrão: {count} peças")

    print("\n--- Gerenciamento de Caixas ---")

    # Ajuste para exibir a contagem correta se a última caixa não estiver cheia
    if pecas_ultima_caixa == 0 and caixas_usadas > 1:
        # Se a última peça encheu a caixa anterior
        print(f"📦 Caixas Completas Utilizadas: {caixas_usadas - 1}")
        print("📦 A última caixa não foi iniciada.")
    else:
        print(f"📦 Total de Caixas Utilizadas: {caixas_usadas}")
        print(
            f"  • Peças na última caixa (Caixa {caixas_usadas}): {pecas_ultima_caixa} / {CAPACIDADE_CAIXA}")

    print("="*40)

# --- 5. LÓGICA PRINCIPAL (SIMULAÇÃO DA LINHA DE MONTAGEM) ---


def iniciar_automacao(total_de_pecas_a_simular):
    """Função principal que executa a simulação da linha de montagem."""

    # Armazenamento e contadores
    pecas_aprovadas_total = 0
    pecas_reprovadas_total = 0

    # Dicionário para contar os motivos específicos
    # (Ex: {'Peso': 5, 'Cor': 2, 'Comprimento': 3})
    contagem_motivos_reprovacao = {}

    # Gerenciamento das Caixas
    caixas_utilizadas = 1
    pecas_na_caixa_atual = 0

    print(
        f"--- 🏭 INICIANDO SIMULAÇÃO DA LINHA DE MONTAGEM (Total: {total_de_pecas_a_simular} peças) ---")

    for i in range(1, total_de_pecas_a_simular + 1):
        # 1. Receber os dados da peça
        peca_atual = gerar_peca_simulada(i)

        # 2. Avaliar a peça
        status, motivos = inspecionar_peca(peca_atual)

        # Log de produção (Opcional, mas bom para ver o processo)
        # print(f"ID {peca_atual['id']}: Status {status}. Motivos: {motivos}")

        if status == 'Aprovada':
            pecas_aprovadas_total += 1
            pecas_na_caixa_atual += 1

            # 3. Armazenar na caixa e verificar a capacidade
            if pecas_na_caixa_atual == CAPACIDADE_CAIXA:
                print(
                    f"📦 [AVISO] Caixa {caixas_utilizadas} está cheia ({CAPACIDADE_CAIXA}/{CAPACIDADE_CAIXA}). Fechando e iniciando próxima.")
                caixas_utilizadas += 1
                pecas_na_caixa_atual = 0  # Reinicia a contagem para a nova caixa

        else:  # Se foi Reprovada
            pecas_reprovadas_total += 1

            # 4. Contabilizar os motivos da reprovação
            if "Peso" in str(motivos):
                contagem_motivos_reprovacao['Peso'] = contagem_motivos_reprovacao.get(
                    'Peso', 0) + 1
            if "Cor" in str(motivos):
                contagem_motivos_reprovacao['Cor'] = contagem_motivos_reprovacao.get(
                    'Cor', 0) + 1
            if "Comprimento" in str(motivos):
                contagem_motivos_reprovacao['Comprimento'] = contagem_motivos_reprovacao.get(
                    'Comprimento', 0) + 1

    print("--- 🛑 SIMULAÇÃO CONCLUÍDA ---")

    # 5. Gerar Relatório Final
    exibir_relatorio_final(
        pecas_aprovadas_total,
        pecas_reprovadas_total,
        contagem_motivos_reprovacao,
        caixas_utilizadas,
        pecas_na_caixa_atual
    )


# --- EXECUÇÃO DO PROTÓTIPO ---
if __name__ == "__main__":
    # Vamos simular a produção de 150 peças
    iniciar_automacao(total_de_pecas_a_simular=150)
