# Playbook

Hosts bilgileri için örnek inventory dosyası;

```
[theone]
automated ansible_host=192.168.1.36


[worker]
virtual01 ansible_host=192.168.1.41
virtual02 ansible_host=192.168.1.42
virtual03 ansible_host=192.168.1.43

```

Playbookların çalıştırılması:

```
ansible-playbook postgresql-playbook/install_postgresql.yaml

ansible-playbook minio-playbook/minio.yaml

```



