# Typecho Backup Pic

> 备份 Typecho 博客中引用的图片

`sm.ms` 是个优秀的图片托管网站，可托管毕竟是把自己的数据交给别人，为了保证图片的安全，还是应当有自己的一个备份为妙。

### 用法

##### 手动备份

用 Typecho 的导出工具将博客内容导出。

```shell
git clone https://github.com/memset0/typecho-backup-pic
pip3 install -r requirements.txt
copy path/to/your/backup/file.dat source.dat
python3 script.py
```

##### 自动备份

**（正在咕咕）**

```shell
git clone https://github.com/memset0/typecho-backup-pic
pip3 install -r requirements.txt
```

在 `config.yml` 中填写好网站地址和密码

```shell
python3 download.py && python3 script.py
```

### 初衷

中考考完了想找一下写 Python 的手感，同时了解一下 `requestments.txt` 的使用。

### License

GNU v3