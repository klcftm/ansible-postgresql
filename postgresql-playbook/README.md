# PostgreSQL Playbook

Hosts bilgileri için örnek inventory dosyası;

```
[theone]
automated ansible_host=192.168.1.36

```

PostgreSQL versiyonu, database ismi ve kullanıcı bilgileri için vars.yaml dosyasında değişiklik yapabilirsiniz.

```yml
---
postgresql_version: <version>
postgresql_user: postgres
postgresql_group: postgres
postgresql_config_path: "/var/lib/pgsql/{{ postgresql_version }}/data"
db_name: <db_name>
db_user: <db_user>
db_password: <db_password>

```

Playbook'un çalıştırılması:

```
ansible-playbook install_postgresql.yaml

```



