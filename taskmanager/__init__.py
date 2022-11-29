import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):
    import env  #noqa


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

# we need to create an instance of the imported SQLAlchemy() class, which will be
# assigned to a variable of 'db', and set to the instance of our Flask 'app'.
# Finally, from our taskmanager package, we will be importing a file called 'routes' which we'll create momentarily.
# Once you save the file, you'll notice we have a couple linting issues.
# First, it says that we've imported 'env', but it's unused.
# It's also complaining about our custom import not being added at the top of the file with the other imports.

db = SQLAlchemy(app)


# The reason this is being imported last, is because the 'routes' file, that we're about
# to create, will rely on using both the 'app' and 'db' variables defined above.
# If we try to import routes before 'app' and 'db' are defined, then we'll get circular-import
# errors, meaning those variables aren't yet available to use, as they're defined after the routes.
# These linting warnings are technically not accurate, so to stop the warnings, we can
# add a comment at the end of each line, # noqa for 'No Quality Assurance'.

from taskmanager import routes #noqa