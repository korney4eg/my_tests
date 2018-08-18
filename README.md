# Test tasks

All the actions described here should be made inside repo, so here how can it be done
```bash
git clone https://github.com/korney4eg/my_tests
cd my_tests
```

## 1. write hello world api
To run it following steps should be made:
1. configuration file `.db_config.ini` created, that contains database connection info.

Here is example
```ini
[database]
host = 127.0.0.1
port = 3306
database = my_users
user = myuser
password = 12345678
```

2.  database should be running

To simplify just run docker compose command:
```bash
docker-compose up -d
```

3. requirements should be installed

```bash
pip install -r requirements.txt
```

4. run programm

```bash
python main.py
```

## 2. Produce system diagram on solution

![Application diagramm](https://github.com/korney4eg/my_tests/raw/master/application_diagramm.png)

## 3. write configuration script to build and make zero-downtime deployment
Script could be found [here](https://github.com/korney4eg/my_tests/blob/master/provision.yaml)

To run deployment you need to have ansible installed.
```bash
ansible-playbook provision.yaml -v
```