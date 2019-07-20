import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

# original db setup; use sessions for nested resource
# from app import app, db
from app import app, s

app.config.from_object(os.environ['APP_SETTINGS'])

# original db setup; use sessions for nested resource
# migrate = Migrate(app, db)
migrate = Migrate(app, s)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
