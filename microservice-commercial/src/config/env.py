from pathlib import Path
from dotenv import load_dotenv

# env.py está en src/config/, la raíz del proyecto está 3 niveles arriba
BASE_DIR = Path(__file__).resolve().parent.parent.parent
load_dotenv(BASE_DIR / ".env")