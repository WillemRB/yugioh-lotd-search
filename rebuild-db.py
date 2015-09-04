from django.utils.termcolors import colorize
from subprocess import call

print colorize('Removing existing database...', fg="white", bg='blue', opts=('bold'))
call(["rm", "db.sqlite3"])

print colorize('Removing migrations...', fg="white", bg='blue', opts=('bold'))
call(["rm", "cards/migrations/0001_initial.py"])
call(["rm", "cardsources/migrations/0001_initial.py"])

print colorize('Rebuilding database...', fg="white", bg='blue', opts=('bold'))
call(["python", "manage.py", "makemigrations"])
call(["python", "manage.py", "syncdb", "--noinput"])

print colorize('Loading superuser...', fg="white", bg='blue', opts=('bold'))
call(["python", "manage.py", "loaddata", "auth.json"])

print colorize('Loading fixtures...', fg="white", bg='blue', opts=('bold'))
call(["python", "manage.py", "loaddata", "cardsources/fixtures/battlepacks.json"])
call(["python", "manage.py", "loaddata", "cardsources/fixtures/boosters.json"])
call(["python", "manage.py", "loaddata", "cardsources/fixtures/players.json"])
call(["python", "manage.py", "loaddata", "cards/fixtures/cardtypes.json"])