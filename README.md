# alembic-migrations

Alembic can view the status of the database and compare against the table metadata in the application, generating the “obvious” migrations based on a comparison. This is achieved using the --autogenerate option to the alembic revision command, which places so-called candidate migrations into our new migrations file. We review and modify these by hand as needed, then proceed normally.

To use autogenerate, we first need to modify our env.py so that it gets access to a table metadata object that contains the target. Suppose our application has a declarative base (sqlAlchemy) in app.models This base contains a MetaData object which contains Table objects defining our database. We make sure this is loaded in env.py and then passed to EnvironmentContext.configure() via the target_metadata argument. The env.py sample script used in the generic template already has a variable declaration near the top for our convenience, where we replace None with our MetaData. Starting with:
```
# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = None
```
we change to:
```
from myapp.mymodel import Base
target_metadata = Base.metadata
```

We can then use the alembic revision command in conjunction with the --autogenerate option. Suppose our MetaData contained a definition for the account table, and the database did not. We’d get output like:
```
$ alembic revision --autogenerate -m "Added account table"
INFO [alembic.context] Detected added table 'account'
Generating /path/to/foo/alembic/versions/27c6a30d7c24.py...done
```
We can then view our file 27c6a30d7c24.py and see that a rudimentary migration is already present
