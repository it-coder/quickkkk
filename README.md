# quickkkk
快速配置你的Ubuntu/Mint操作系统

![](https://raw.githubusercontent.com/Baloneo/quickkkk/master/mypc.png)

## 使用
> 使用之前请先查看`cmd_config.py`文件，定制你想要的环境。
* 安装配置基本环境
下载本项目
```
git clone https://github.com/Baloneo/quickkkk.git
```
切换工作目录
```
cd quickkkk
```
创建下载基本的软件环境
```
python3 start.py init
```

* 下载安装包等
下载的文件在`~/quickkkk_download`
```
python3 start.py download  # 执行下载所有
python3 start.py download 1:2  # 执行下载制定列表的下标为[1:2) 包前不包后，也就是指定arr[1]的元素
python3 start.py download 3:  # 执行下载制定列表的下标为3到后面所有
```

* 打印所有命令
```
python3 start.py print
```

* 安装
解压安装的文件在`~/software`
```
python3 start.py install
```


## 软件列表
* flat-remix图标
* materia-theme主题
* FiraCode字体
* 鼠标主题 capitaine-cursors
* 悬浮网速内存指示器
* sfs
* 网易云
* chrome
* vscode
* wps
* wechat
* tim
* go
* clion
* typora
* virtualbox
* pycharm-professional
* 鼠标主题
* gtk3 dev
* neofetch
* smplayer
* ssr-gui
* oh-my-zsh
* python3-dev
* peek gif录制