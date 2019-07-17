#!/use/bin/env python3

"""
ISO镜像文件可以在国内源下载

国内清华源：
https://mirrors.tuna.tsinghua.edu.cn/help
中国科学技术大学源:
https://mirrors.ustc.edu.cn/
阿里源：
https://opsx.alibaba.com/mirror

"""

"""
0. 更改源
1. 打开设置界面，安装语言和输入法，输入法选择ibus，安装好之后重启
2. 打开软件更新管理器，更新系统软件
3. 运行本脚本
"""

l_init = [
    # 创建本项目文件存储路径
    "echo 'pass'",
    "mkdir -p ~/quickkkk_download",  # 1
    "mkdir -p ~/software",  # 2
    "mkdir -p ~/.icons",  # 3

    # 配置中文快捷方式 
    "ln -s $HOME/文档 $HOME/Documents",   # 4
    "ln -s $HOME/下载 $HOME/Downloads",  # 5
    'ln -s $HOME/图片 $HOME/Images',  # 6

    "sudo apt update",  # 7
    # 安装基本的软件
    "sudo apt install -y vim curl wget git unar zsh",  # 8

    # 配置终端 xfce4
    # "cp ./files/config_file/terminalrc ~/.config/xfce4/terminal/",  # 9
    'echo "xfce终端设置，可选操作, 不执行"',

    # 删除不必要的软件
    "apt remove thunderbird",  #10

    # 卸载libreoffice
    'sudo apt-get purge "libreoffice?"',  # 11

    # 配置 git
    # "git config --global user.email alonebo.zhou@gmail.com",
    # "git config --global user.name baloneo",

    # 设置最大文件监听数
    # 'sudo echo "fs.inotify.max_user_watches=524288" >> /etc/sysctl.conf;sudo sysctl -p;',
]

l_download_test = [
    "echo 'cmd 0'",
    "echo 'cmd 1'",
    "echo 'cmd 2'",
    "mkdir /tmp/tet",
    "echo 'cmd 4'",
    "echo 'cmd 5'",
]

l_download = [
    
    # ~/quickkkk_download

    # 0: oh my zsh 
    "curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh --output ~/quickkkk_download/ohmyzsh-install.sh",

    # 1: 下载图标
    "rm -rf ~/quickkkk_download/flat-remix;git clone https://gitee.com/alonebo/flat-remix.git ~/quickkkk_download/flat-remix",

    # 2: theme
    "git clone --depth 1 https://github.com/nana-4/materia-theme ~/quickkkk_download/materia-theme",

    # 3: 下载字体
    "wget https://github.com/tonsky/FiraCode/releases/download/1.206/FiraCode_1.206.zip -O ~/quickkkk_download/FiraCode",
    # 'echo "pass"',

    # 4: 下载wine
    "git clone https://gitee.com/wszqkzqk/deepin-wine-for-ubuntu.git ~/quickkkk_download/deepin-wine-for-ubuntu",

    # 5: 下载网速指示器
    "git clone https://github.com/Baloneo/network-ball-gtk.git ~/quickkkk_download/network-ball-gtk",

    # 6: 下载sfs http文件共享
    "git clone https://github.com/Baloneo/share-file-server.git ~/quickkkk_download/share-file-server",

    # 7: 网易云
    "wget http://d1.music.126.net/dmusic/netease-cloud-music_1.2.1_amd64_ubuntu_20190428.deb -O ~/quickkkk_download/netease-cloud-music.deb",

    # 8: chrome
    "wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -O ~/quickkkk_download/chrome.deb",

    # 9: vscode
    "wget https://vscode.cdn.azure.cn/stable/0f3794b38477eea13fb47fbe15a42798e6129338/code_1.36.0-1562161087_amd64.deb -O ~/quickkkk_download/vscode.deb",

    # 10: wps
    "wget https://wdl1.cache.wps.cn/wps/download/ep/Linux2019/8722/wps-office_11.1.0.8722_amd64.deb -O ~/quickkkk_download/wps.deb",

    # 11: wechat
    "wget https://mirrors.aliyun.com/deepin/pool/non-free/d/deepin.com.wechat/deepin.com.wechat_2.6.2.31deepin0_i386.deb -O ~/quickkkk_download/wechat.deb",

    # 12: tim
    "wget https://mirrors.aliyun.com/deepin/pool/non-free/d/deepin.com.qq.office/deepin.com.qq.office_2.0.0deepin4_i386.deb -O ~/quickkkk_download/tim.deb",

    # 13: go
    "wget https://dl.google.com/go/go1.12.7.linux-amd64.tar.gz -O ~/quickkkk_download/go1.12.7.linux-amd64.tar.gz",

    # 14: typora
    "wget https://typora.io/linux/Typora-linux-x64.tar.gz -O ~/quickkkk_download/Typora-linux-x64.tar.gz",

    # 15: virtualbox 清华源
    "wget https://mirrors.tuna.tsinghua.edu.cn/virtualbox/6.0.8/virtualbox-6.0_6.0.8-130520~Ubuntu~bionic_amd64.deb -O ~/quickkkk_download/virtualbox-ubuntu18-6.0.8.deb",
    # "echo '自己手动下载virtualbox'",

    # 17: pycharm-professional
    "wget https://download.jetbrains.8686c.com/python/pycharm-professional-2019.1.3.tar.gz -O ~/quickkkk_download/pycharm-professional-2019.1.3.tar.gz",

    # 18: 鼠标主题
    "git clone https://github.com/keeferrourke/capitaine-cursors.git ~/quickkkk_download/capitaine-cursors",

    # 19: clion
    "wget https://download.jetbrains.8686c.com/cpp/CLion-2019.1.4.tar.gz -O ~/quickkkk_download/CLion-2019.1.4.tar.gz",

    # 20: 下载wps字体
    "git clone https://github.com/iamdh4/ttf-wps-fonts.git ~/quickkkk_download/ttf-wps-fonts",

]

l_install = [

    # 0: ~/quickkkk_download
    'echo "pass"',

    # 1: oh-my-zsh
    "sh ~/quickkkk_download/ohmyzsh-install.sh",
    # 'echo "pass"',

    # 2: 图标 主题
    "cp -r ~/quickkkk_download/flat-remix/* ~/.icons;sudo ~/quickkkk_download/materia-theme/install.sh",

    # 3: wine
    "sh ~/quickkkk_download/deepin-wine-for-ubuntu/install.sh",

    # 4: 网速指示器
    "cd ~/quickkkk_download/network-ball-gtk/; bash ~/quickkkk_download/network-ball-gtk/add_autostart.sh",

    # 5: sfs
    "sudo cp ~/quickkkk_download/share-file-server/bin/linux64-sfs /usr/bin/sfs",

    # 6: 网易云
    "sudo dpkg -i ~/quickkkk_download/netease-cloud-music*.deb",

    # 7: chrome
    "sudo dpkg -i ~/quickkkk_download/chrome*.deb",

    # 8: vscode
    "sudo dpkg -i ~/quickkkk_download/vscode*.deb",

    # 9: wps
    "sudo dpkg -i ~/quickkkk_download/wps*.deb",

    # 10: wechat
    "sudo dpkg -i ~/quickkkk_download/wechat*.deb",

    # 11: tim
    "sudo dpkg -i ~/quickkkk_download/tim*.deb",

    # 12: go
    "unar ~/quickkkk_download/go1.12.7.linux-amd64.tar.gz -o ~/software/",

    # 13: typora
    "unar ~/quickkkk_download/Typora-linux-x64.tar.gz -o ~/software",

    # 14: virtualbox
    "sudo dpkg -i ~/quickkkk_download/virtualbox*.deb",
    # 'echo "自己手动安装virtualbox"',

    # 15: ssr
    "cp ./files/ssr ~/software",
    # 'echo "pass"',

    # 16: gtk3 dev
    "sudo apt install -y libgtk-3-dev g++ cmake ipython3",

    # 17: 设置go环境
    'echo "export PATH=$PATH:$HOME/software/go/bin" >> ~/.zshrc;echo "export PATH=$PATH:$HOME/software/go/bin" >> ~/.bashrc;',

    # 18: neofetch
    "sudo add-apt-repository ppa:dawidd0811/neofetch;sudo apt update;sudo apt install neofetch",

    # 19: nitroshare
    # "sudo apt-get install nitroshare",
    'echo "nitroshare pass"',

    # 20: vlc
    #"sudo apt install vlc",
    "echo 'pass'",

    # 21: smplayer
    "sudo apt install smplayer",
    #'echo "smplayer pass"',

    # 22: 鼠标主题
    "cp -r ~/quickkkk_download/capitaine-cursors/dist ~/.icons/capitaine-cursors",

    # 23: pycharm
    "unar ~/quickkkk_download/pycharm-professional-2019.1.3.tar.gz -o ~/software/",

    # 24: clion
    "unar ~/quickkkk_download/CLion-2019.1.4.tar.gz -o ~/software/",

    # 25: wps字体
    "cd ~/quickkkk_download/ttf-wps-fonts;sudo bash install.sh",

    # 26: htop
    "sudo apt install -y htop",

    # 27: 代理方式打开chrome 安装代理插件
    # 'google-chrome --proxy-server="socks5://127.0.0.1:2080"',
    'echo "可选操作，命令行打开chrome 设置代理"',

    # 28
    "apt install python3-pip",

    # 29 python3 开发环境
    "apt install python3-dev",

    # 30 peek gif录制
    "sudo add-apt-repository ppa:peek-developers/stable;sudo apt update;sudo apt install peek",
]

if __name__ == "__main__":
    print("len l_init: ", len(l_init))
    print("len l_download: ", len(l_download))
    print("len l_install: ", len(l_install))

