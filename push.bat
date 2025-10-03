@echo off
chcp 65001 >nul
echo ========================================
echo  🚀 Auto Git Push Script for Windows
echo ========================================

echo 📍 Текущая директория: %CD%

setlocal EnableDelayedExpansion
set "commit_msg=%~1"
if "!commit_msg!"=="" (
    set "commit_msg=update: %date% %time%"
)

echo.
echo 📁 Добавляем все файлы...
git add .

echo 💾 Создаем коммит: !commit_msg!
git commit -m "!commit_msg!"

if %errorlevel% neq 0 (
    echo ❌ Ошибка при коммите. Возможно, нет изменений.
    echo 🔄 Пробуем просто запушить существующие коммиты...
    git pull
    git push
    goto :end
)

echo ⬇️  Получаем актуальные изменения с сервера...
git pull

echo ⬆️  Пушим изменения на GitHub...
git push

:end
echo.
echo ========================================
echo ✅ Процесс завершен! %time%
echo ========================================
pause