.venv 環境：
uv add requsets
uv remove requests

uv init
uv add django
uv run python -m django --version
uv run django-admin startproject wretch .
uv run python manage.py runserver
在 settings.py 的 DIRS 加上新資料夾名
建立新資料夾名，資料夾內建立 html 頁面
在 urls.py 裡建立連結頁面的伺服器，利用 django.shortcuts 的 render 找到檔案
.gitinore 裡加上 \*.sqlite3 來忽略
接著 git rm db.sqlite3
git add .
git commit -m 'chore: remove db and add Makefile'
uv run python manage.py migrate 建立資料庫表格
git add .
git commit --amend --no-edit 併入上層
git push --force-with-lease 硬推
git branch issue/1 開分支
git checkout issue/1 切換分支
