# 🎯 YT Treino — Calibrador de Algoritmo do YouTube

Automatiza buscas e visualizações no YouTube para calibrar o algoritmo conforme seu perfil de interesse.

---

## 📋 Pré-requisitos

| Ferramenta | Link |
|---|---|
| Python 3.8+ | [python.org/downloads](https://python.org/downloads) |
| Google Chrome | já instalado na maioria dos PCs |

> ⚠️ Durante a instalação do Python, marque **"Add Python to PATH"**

---

## ⚙️ Instalação

```powershell
pip install selenium webdriver-manager
```

ou, se `pip` não for reconhecido:

```powershell
python -m pip install selenium webdriver-manager
```

---

## 🚀 Como Executar

### Passo 1 — Abrir o Chrome com debugging habilitado

**PowerShell ou cmd:**
```powershell
& "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\meu_perfil_chrome"
```

> Uma janela do Chrome vai abrir. Faça login no YouTube normalmente nessa janela.

---

### Passo 2 — Rodar o script

Abra outro terminal, navegue até a pasta e execute:

```powershell
cd "C:\Users\*****\OneDrive\Desktop\youtube Algo"
python youtube_treino.py
```

---

## 🗂️ Estrutura de Arquivos

```
youtube Algo/
├── youtube_treino.py        # Script principal
├── readme.md                # Este guia
├── yt_treino_log.txt        # Log gerado automaticamente ao rodar
└── terms/
    ├── __init__.py          # Controla quais categorias ficam ativas
    ├── python_backend.py    # Python, Node, Docker, bancos de dados
    ├── frontend.py          # React, TypeScript, Next.js, CSS
    ├── mobile.py            # React Native, Android, Flutter
    ├── architecture.py      # System design, clean arch, algoritmos
    ├── devops.py            # CI/CD, Cloud, Git, Linux
    └── canais.py            # Fireship, Rocketseat, ThePrimeagen...
```

---

## 🎛️ Ativando / Desativando Categorias

Edite apenas `terms/__init__.py` — lista `ATIVAS`:

```python
# Todas as categorias
ATIVAS = [
    "python_backend",
    "frontend",
    "mobile",
    "architecture",
    "devops",
    "canais",
]
```

**Exemplos de sessões focadas:**

```python
# Só frontend
ATIVAS = ["frontend", "canais"]

# Só mobile/Android
ATIVAS = ["mobile", "canais"]

# Arquitetura + backend
ATIVAS = ["architecture", "python_backend", "devops"]
```

> Os termos de cada categoria ficam nos arquivos dentro de `terms/`.
> Edite-os diretamente para adicionar ou remover termos por tema.

---

## 🔧 Configurações do Script

Ajuste as constantes em `youtube_treino.py`:

| Variável | Padrão | O que faz |
|---|---|---|
| `MIN_WATCH_SECONDS` | `90` | Tempo mínimo assistindo cada vídeo |
| `MAX_WATCH_SECONDS` | `240` | Tempo máximo assistindo cada vídeo |
| `SEARCHES_PER_RUN` | `8` | Quantas buscas por execução |
| `PAUSE_BETWEEN` | `(3, 7)` | Pausa entre ações (segundos) |

---

## 📈 Boas Práticas

- **Rode por vários dias seguidos** — o algoritmo leva tempo para recalibrar
- **Misture PT e EN** — aumenta o alcance de conteúdo
- **Curta e se inscreva manualmente** nos canais bons que aparecerem — sinal mais forte
- **Limpe o histórico do YouTube** antes da primeira execução para um reset limpo
- Verifique o log gerado em `yt_treino_log.txt` para acompanhar o progresso
