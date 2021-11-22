# 重置本地数据库

```shell
rm -f db.sqlite3
rm -r */migrations
python manage.py makemigrations
python manage.py migrate
```

# 离线部署

## 在线下载所需依赖(联网设备)

```shell
pip install pipreqs
pipreqs ./
pip download -d offline_package -r requirements.txt
```
## 离线安装依赖(离线设备)
```shell
pip install --no-index --find-links="offline_package" -r requirements.txt
```