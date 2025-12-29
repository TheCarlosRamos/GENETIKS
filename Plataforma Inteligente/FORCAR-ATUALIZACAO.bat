@echo off
echo ========================================
echo Forcando Atualizacao do SQLAlchemy
echo ========================================
echo.

echo Python 3.13 requer SQLAlchemy 2.0.25 ou superior
echo.

echo [1/4] Desinstalando SQLAlchemy completamente...
pip uninstall sqlalchemy -y
pip uninstall alembic -y

echo.
echo [2/4] Limpando cache do pip...
pip cache purge

echo.
echo [3/4] Instalando versao mais recente do SQLAlchemy...
pip install --no-cache-dir --force-reinstall "sqlalchemy>=2.0.25"
pip install --no-cache-dir --force-reinstall "alembic>=1.13.0"

echo.
echo [4/4] Verificando versao instalada...
python -c "import sqlalchemy; print('SQLAlchemy versao:', sqlalchemy.__version__)" 2>nul
if errorlevel 1 (
    echo.
    echo ERRO: SQLAlchemy ainda nao funciona com Python 3.13
    echo.
    echo RECOMENDACAO: Use Python 3.11 ou 3.12
    echo.
    echo Ou tente instalar versao de desenvolvimento:
    echo   pip install --pre sqlalchemy
) else (
    echo.
    echo SUCESSO! Testando importacao completa...
    python -c "from sqlalchemy import create_engine; print('OK - SQLAlchemy funcionando!')" 2>nul
    if errorlevel 1 (
        echo AVISO: Importacao basica OK, mas pode haver problemas
    ) else (
        echo.
        echo ========================================
        echo TUDO FUNCIONANDO!
        echo ========================================
    )
)

echo.
pause

