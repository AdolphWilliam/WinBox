# pip备份

##  1.导出现有python第三方库

```python
import pkg_resources

# 获取已安装的包
installed_packages = {pkg.key for pkg in pkg_resources.working_set}

# 将包的名称写入文件
with open("requirements.txt", "w") as f:
    for package in sorted(installed_packages):
        f.write(package + "\n")
```

## 2.使用导出的"requirements.txt"文件安装库

进入"requirements.txt"文件路径后使用下面的命令：

```
pip install -r requirements.txt
```

