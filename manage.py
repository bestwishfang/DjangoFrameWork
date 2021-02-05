from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from apps import create_app, models

app = create_app()
manage = Manager(app)
migrate = Migrate(app, models)
manage.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manage.run()
