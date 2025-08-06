.venv 環境：
uv add requsets
uv remove requests

uv init
uv add django
uv run python -m django --version
uv run django-admin startproject wretch .
uv run python manage.py runserver
在 settings.py 的 DIRS 加上資料夾名
資料夾內建立 html 頁面
在 urls.py 裡建立連結頁面的伺服器，利用 django.shortcuts 的 render 找到檔案
