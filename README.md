## INSTALL

### Install Packages
To run the application, install all package dependencies, use this command.

```
pip install -r requirements.txt
```

### Create file start.sh
Create file start.sh and copy all line in below to the file.

```
export APP_CONFIG_FILE=
export DB_HOST=
export DB_PORT=
export DB_USERNAME=
export DB_NAME=
export DB_PASSWORD=

python run.py
```

After that, give the file permission so we can execute to run app.

```
sudo chmod a+x start.sh
```

### Create migrate.sh
Create file ``migrate.sh`` in copy this command.

```
export APP_CONFIG_FILE=
export DB_HOST=
export DB_PORT=
export DB_USERNAME=
export DB_NAME=
export DB_PASSWORD=

python manager.py
```

And give the file permission so we can run the migration.

```
sudo chmod a+x migrate.sh
```

Now we can run migration use this command

```
./migrate.sh
```

## Run Application
To run the application, run with command

```
./start.sh
```
