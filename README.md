# alembic-migrations

## Project structure
```
.
├── app/
│    │
│    ├── alembic/
│    │   └── Alembic environment
|    |
|    ├── models/
│    │   └── SQLAlchemy relational models
│    │
│    ├── utils/
│    │   └── Database configuration and connection files
│    │
│    ├── alembic.ini/
│        └── Alembic ini file
│    
├── .gitignore 
│ 
├── Makefile (commands to perform migrations and configure the database)
│ 
├── README.md  
│ 
├── docker-compose.yml (Postgres DB)
│
├── example.env (sample of required environment variables)
│
└── requirements.txt
```

## Clone and setup 
1. The project is public so to clone it just run the following command:
```
git clone https://github.com/BrenoMilagres/alembic-migrations.git
```

2. Create and activate a virtual environment with python 3.10:
```
virtualenv venv -p python3.10
source venv/bin/activate
```

3. Installing dependencies:
```
pip install -r requirements.txt
```

4. Create .env file to export the necessary environment variables and their respective values ​​based on example.env
```
export DB_USER="alembic_tuto"
export DB_PASS="alembic_tuto"
export DB_NAME="alembic_tuto"
export DB_HOST="localhost"
export DB_PORT="5432"
```

## The Migration Environment

Usage of Alembic starts with creation of the Migration Environment. This is a directory of scripts that is specific to a particular application. The migration environment is created just once, and is then maintained along with the application’s source code itself. The environment is created using the init command of Alembic:

```
alembic init <folder>
```

The structure of this environment, including some generated migration scripts, looks like:

```
yourproject/
    alembic/
        env.py
        README
        script.py.mako
        versions/
            3512b954651e_add_account.py
            2b1ae634e5cd_add_order_id.py
            3adcc9a56557_rename_username_field.py
```

- yourproject - this is the root of your application’s source code, or some directory within it.

- alembic - this directory lives within your application’s source tree and is the home of the migration environment. It can be named anything, and a project that uses multiple databases may even have more than one.

- env.py - This is a Python script that is run whenever the alembic migration tool is invoked. At the very least, it contains instructions to configure and generate a SQLAlchemy engine, procure a connection from that engine along with a transaction, and then invoke the migration engine, using the connection as a source of database connectivity.

- README - included with the various environment templates, should have something informative.

- script.py.mako - This is a Mako template file which is used to generate new migration scripts. Whatever is here is used to generate new files within versions/. This is scriptable so that the structure of each migration file can be controlled, including standard imports to be within each, as well as changes to the structure of the upgrade() and downgrade() functions. For example, the multidb environment allows for multiple functions to be generated using a naming scheme upgrade_engine1(), upgrade_engine2().

- versions/ - This directory holds the individual version scripts. Users of other migration tools may notice that the files here don’t use ascending integers, and instead use a partial GUID approach. In Alembic, the ordering of version scripts is relative to directives within the scripts themselves, and it is theoretically possible to “splice” version files in between others, allowing migration sequences from different branches to be merged, albeit carefully by hand.

## Autogenerate

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
from utils.configs import settings
target_metadata = settings.DBBaseModel.metadata
```

and the URL of the DB we reference as follows:
```
config = context.config
config.set_main_option('sqlalchemy.url', settings.DB_URL)
```

We can then use the alembic revision command in conjunction with the --autogenerate option. Suppose our MetaData contained a definition for the account table, and the database did not. We’d get output like:
```
$ alembic revision --autogenerate -m "Added app tables"
INFO [alembic.context] Detected added tables 'de', 'ds' and 'ae'
Generating /path/to/foo/alembic/versions/27c6a30d7c24.py...done
```
We can then view our file 27c6a30d7c24.py and see that a rudimentary migration is already present


