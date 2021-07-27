# GitHub Star Tracker

用来追踪 GitHub 仓库的加星数量变化。

默认为 1 小时请求一次仓库的星星数量，当有变化时，变更信息会写入到 logs.json 文件中。

### 用法

编辑 `tracker.py`，将 GitHub 仓库名添加到 `repo_name` 中。

```shell
$ python3 tracker.py
```

### 使用 screen 让程序始终运行在后台

创建一个 screen 进程：

```shell
$ screen -dmS tracker
```

进入创建的 screen 进程：

```shell
$ screen -r tracker
```

运行脚本：

```shell
$ python3 tracker.py
```

脱离 screen 窗口，让程序在后台运行：

组合键：`Ctrl + A, Ctrl + D`

## 注意操作系统的时区设置

云主机上的系统默认使用 UTC 时间，为了时间记录的准确性，应该把时区调成当地时间。

> Ubuntu 可以使用 `tzselect` 命令修改系统的时区设置
