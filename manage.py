# -*- coding: utf-8 -*-
from gevent import monkey
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from apps import create_app, models

monkey.patch_all()

app = create_app()
manager = Manager(app)
migrate = Migrate(app, models)
manager.add_command('db', MigrateCommand)


@manager.command
def runserver_gevent():
    from gevent import pywsgi
    from werkzeug.debug import DebuggedApplication

    dapp = DebuggedApplication(app, evalex=True)
    ip_port = ('127.0.0.1', 5000)
    server = pywsgi.WSGIServer(ip_port, dapp)
    print("Use Gevent with Flask Web Server, Now Running ...")
    server.serve_forever()


if __name__ == '__main__':
    manager.run()
