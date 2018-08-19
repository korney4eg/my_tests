# Test tasks

All the actions described here should be made inside repo, so here how can it be done
```bash
git clone https://github.com/korney4eg/my_tests
cd my_tests
```

## 1. write hello world api
To run it following steps should be made:

0. Go to `1.Hello_World_app/` folder
```bash
cd 1.Hello_World_app/
```

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

![Application diagramm](https://github.com/korney4eg/my_tests/raw/master/2.System_diagramm/application_diagramm.png)

## 3. write configuration script to build and make zero-downtime deployment
Script could be found [here](https://github.com/korney4eg/my_tests/blob/master/3.Zero_downtime_deployment_script/provision.yaml)

To run deployment you need to have ansible installed.
```bash
cd 3.Zero_downtime_deployment_script/
ansible-playbook provision.yaml -v
```

## System requirements:
- git
- ansible 2.6.2
- Python 2.7.15