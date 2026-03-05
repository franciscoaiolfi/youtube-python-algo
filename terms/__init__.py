from .python_backend import PYTHON_BACKEND
from .frontend import FRONTEND
from .mobile import MOBILE
from .architecture import ARCHITECTURE
from .devops import DEVOPS
from .canais import CANAIS

# Mapa de categorias — ative/desative conforme seu objetivo
CATEGORIAS = {
    "python_backend": PYTHON_BACKEND,
    "frontend":       FRONTEND,
    "mobile":         MOBILE,
    "architecture":   ARCHITECTURE,
    "devops":         DEVOPS,
    "canais":         CANAIS,
}

# Categorias ativas nesta sessão (remova as que não quiser)
ATIVAS = [
    "python_backend",
    "frontend",
    "mobile",
    "architecture",
    "devops",
    "canais",
]

# Lista final usada pelo script
SEARCH_TERMS = [
    termo
    for categoria in ATIVAS
    for termo in CATEGORIAS[categoria]
]
