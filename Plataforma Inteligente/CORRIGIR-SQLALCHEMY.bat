@echo off
echo ========================================
echo Corrigindo incompatibilidade SQLAlchemy
echo ========================================
echo.

echo O problema e que SQLAlchemy antigo nao e compativel com Python 3.13
echo Desinstalando versao antiga e instalando versao mais recente...
echo.

echo [1/3] Desinstalando SQLAlchemy antigo...
pip uninstall sqlalchemy -y

echo [2/3] Instalando SQLAlchemy mais recente (compativel com Python 3.13)...
pip install --upgrade "sqlalchemy>=2.0.25"
pip install --upgrade alembic

echo.
echo [3/3] Verificando...
python -c "import sqlalchemy; print('SQLAlchemy versao:', sqlalchemy.__version__)" 2>nul
if errorlevel 1 (
    echo.
    echo ERRO: SQLAlchemy ainda nao funciona!
    echo Tentando instalar versao de desenvolvimento...
    pip install --upgrade --pre sqlalchemy
)

echo.
echo Testando importacao completa...
python -c "import sqlalchemy; from sqlalchemy import create_engine; print('OK - SQLAlchemy funcionando!')" 2>nul
if errorlevel 1 (
    echo.
    echo AVISO: Pode haver problemas. Tente usar Python 3.11 ou 3.12.
) else (
    echo.
    echo SUCESSO! SQLAlchemy corrigido!
)

echo.
pause

