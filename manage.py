import os
from apps import create_app, models
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = create_app()
manage = Manager(app)
migrate = Migrate(app, models)
app.secret_key = 'secret'

manage.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manage.run()
