@echo off
SETLOCAL ENABLEDELAYEDEXPANSION

SET CURRENT_DIR=%~dp0
SET PROJECT_ROOT=%CURRENT_DIR:~0, -1%
SET PROJECT_ROOT=%PROJECT_ROOT%\..
SET VENV_PYTHON="%PROJECT_ROOT%\.venv\Scripts\python.exe"
echo %VENV_PYTHON%

echo [UPGRADE] Upgrading pip...
%VENV_PYTHON% -m pip install --upgrade pip
IF ERRORLEVEL 1 (
  echo [ERROR] pip upgrade failed.
  goto :EOF
)

REM Install from requirements.txt
echo [INSTALL] Installing packages from requirements.txt...
%VENV_PYTHON% -m pip install -r "%CURRENT_DIR%\requirements.txt"
IF ERRORLEVEL 1 (
  echo [ERROR] requirements.txt install failed.
  goto :EOF
)
echo [DONE] requirements.txt installed successfully.
