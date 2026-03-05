"""
yt_treino.py — Treina o algoritmo do YouTube para conteúdo de programação
Como usar:
  1. Abre o Chrome com: google-chrome --remote-debugging-port=9222
  2. Faz login no YouTube normalmente nesse Chrome
  3. Roda: python yt_treino.py
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import logging
from datetime import datetime
from terms import SEARCH_TERMS

# ─────────────────────────────────────────────
# CONFIGURAÇÃO DE LOGS
# ─────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("yt_treino_log.txt", encoding="utf-8"),
        logging.StreamHandler()
    ]
)
log = logging.getLogger(__name__)

# ─────────────────────────────────────────────
# CONFIGURAÇÕES
# ─────────────────────────────────────────────
MIN_WATCH_SECONDS = 90    # tempo mínimo assistindo cada vídeo
MAX_WATCH_SECONDS = 240   # tempo máximo assistindo cada vídeo
SEARCHES_PER_RUN  = 8     # quantas buscas fazer por execução
PAUSE_BETWEEN     = (3, 7) # pausa entre ações (seg)


def conectar_chrome():
    """Conecta ao Chrome já aberto com --remote-debugging-port=9222"""
    options = webdriver.ChromeOptions()
    options.add_experimental_option("debuggerAddress", "localhost:9222")
    try:
        driver = webdriver.Chrome(options=options)
        log.info("✅ Conectado ao Chrome com sucesso!")
        return driver
    except Exception as e:
        log.error("❌ Não conseguiu conectar ao Chrome.")
        log.error("   Certifique-se de ter aberto o Chrome com:")
        log.error("   google-chrome --remote-debugging-port=9222")
        raise e


def buscar_e_assistir(driver, termo):
    """Faz uma busca no YouTube e assiste o primeiro vídeo relevante"""
    log.info(f"🔍 Buscando: '{termo}'")

    try:
        driver.get("https://www.youtube.com/results?search_query=" + termo.replace(" ", "+"))
        time.sleep(random.uniform(*PAUSE_BETWEEN))

        wait = WebDriverWait(driver, 10)

        # Pega os primeiros vídeos (ignora anúncios/shorts)
        videos = driver.find_elements(By.CSS_SELECTOR, "ytd-video-renderer a#video-title")

        if not videos:
            log.warning(f"  ⚠️  Nenhum vídeo encontrado para '{termo}'")
            return

        # Escolhe aleatoriamente entre os 3 primeiros resultados
        video = random.choice(videos[:3])
        titulo = video.get_attribute("title") or video.text
        log.info(f"  ▶️  Assistindo: {titulo[:70]}...")

        video.click()
        time.sleep(random.uniform(2, 4))

        # Tempo de watch aleatório
        watch_time = random.randint(MIN_WATCH_SECONDS, MAX_WATCH_SECONDS)
        log.info(f"  ⏱️  Assistindo por {watch_time} segundos...")
        time.sleep(watch_time)

        # Às vezes curte o vídeo (30% de chance)
        if random.random() < 0.30:
            try:
                like_btn = driver.find_element(
                    By.CSS_SELECTOR,
                    "ytd-toggle-button-renderer.ytd-segmented-like-dislike-button-renderer:first-child button"
                )
                like_btn.click()
                log.info("  👍 Vídeo curtido!")
            except Exception:
                pass  # Não é crítico

        log.info(f"  ✅ Concluído: '{titulo[:50]}'")

    except Exception as e:
        log.warning(f"  ⚠️  Erro ao processar '{termo}': {e}")


def main():
    log.info("=" * 55)
    log.info("  🎯 YT TREINO — Calibrador de Algoritmo")
    log.info(f"  Início: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    log.info("=" * 55)

    driver = conectar_chrome()

    # Seleciona termos aleatórios para essa rodada
    termos_rodada = random.sample(SEARCH_TERMS, min(SEARCHES_PER_RUN, len(SEARCH_TERMS)))

    log.info(f"\n📋 {len(termos_rodada)} buscas programadas para hoje:\n")
    for i, t in enumerate(termos_rodada, 1):
        log.info(f"   {i}. {t}")
    log.info("")

    for i, termo in enumerate(termos_rodada, 1):
        log.info(f"\n[{i}/{len(termos_rodada)}] ─────────────────────")
        buscar_e_assistir(driver, termo)
        pausa = random.uniform(*PAUSE_BETWEEN)
        log.info(f"  💤 Pausando {pausa:.1f}s antes da próxima busca...")
        time.sleep(pausa)

    log.info("\n" + "=" * 55)
    log.info("  🏁 Sessão concluída!")
    log.info(f"  Fim: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    log.info("  Rode novamente amanhã para melhores resultados.")
    log.info("=" * 55)

    driver.quit()


if __name__ == "__main__":
    main()