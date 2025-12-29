#!/usr/bin/env python
"""Script para testar se todas as dependências estão instaladas"""

import sys

dependencies = {
    'fastapi': 'FastAPI',
    'uvicorn': 'Uvicorn',
    'sqlalchemy': 'SQLAlchemy',
    'pydantic': 'Pydantic',
    'numpy': 'NumPy',
    'pandas': 'Pandas',
    'dotenv': 'python-dotenv',
}

missing = []
installed = []

for module, name in dependencies.items():
    try:
        __import__(module)
        installed.append(name)
        print(f"✅ {name}")
    except ImportError:
        missing.append(name)
        print(f"❌ {name} - FALTANDO")

print("\n" + "="*50)
if missing:
    print(f"❌ Faltam {len(missing)} dependências:")
    for dep in missing:
        print(f"   - {dep}")
    print("\nInstale com: pip install -r requirements.txt")
    sys.exit(1)
else:
    print(f"✅ Todas as {len(installed)} dependências estão instaladas!")
    sys.exit(0)

