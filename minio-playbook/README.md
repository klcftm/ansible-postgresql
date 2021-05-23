# Minio Playbook

Task:
1. Manuel olarak 3 adet VM yaratılır. Makinelere 5 GB object storage disk eklenir.
2. Bu makinelere Ansible üzerinden minio deployment yapılır. 
   - Object storage diski üzerine, bir volume group tanımlanır.
   - Volume group üzerine, 8 adet logical volume tanımlanır.
   - Bu logical volume’lar üzerine, filesystem yaratılır.
   - Kurulu minio server, systemctl üzerinden yönetilebilecek şekilde bir custom service yazılır.


```

[worker]
virtual01 ansible_host=192.168.1.41
virtual02 ansible_host=192.168.1.42
virtual03 ansible_host=192.168.1.43

```

Minio servisi için vars.yaml dosyasında değişiklik yapabilirsiniz.

```yml
---

minio_user: minio
minio_group: minio
minio_binary_dir: /usr/local/bin
minio_dir: "{{ minio_binary_dir }}/minio"
minio_conf_dir: /opt/minio
minio_service_dir: /etc/systemd/system
minio_download_url: https://dl.minio.io/server/minio/release/linux-amd64/minio
minio_download_dir: /tmp
minio_always_update_binary: false
volumes: /mnt/disks/minio1, /mnt/disks/minio2, /mnt/disks/minio3, /mnt/disks/minio4, /mnt/disks/minio5, /mnt/disks/minio6, /mnt/disks/minio7, /mnt/disks/minio8
mount_file: /mnt/disks

```

Playbook çalıştırıldığında `Failed executing pvs command` hatası alır iseniz serverlarda lvm2'yi günceleyiniz.

```
 yum upgrade lvm2

```



