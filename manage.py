#!/usr/bin/env python
import os
from app import create_app, db
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

cur_app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(cur_app)
migrate = Migrate(cur_app, db)


def make_shell_context():
    return dict(app=cur_app, db=db)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    print("-- manager run --", flush=True)
    manager.run()
    # cur_app.run()
