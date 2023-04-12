
from flask_script import Manager

import app as application

manager = Manager(application)

@manager.command
def hello():
    print ("hello")

if __name__ == "__main__":
    manager.run()