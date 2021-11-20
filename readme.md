# 离线部署
## 在线下载所需依赖(联网设备)
```shell
# 安装`pipreqs`
pip install pipreqs
# 导出依赖
pipreqs ./
# 下载依赖
pip download -d offline_package -r requirements.txt
```
## 离线安装依赖(离线设备)
```shell
pip install --no-index --find-links="offline_package" -r requirements.txt
```