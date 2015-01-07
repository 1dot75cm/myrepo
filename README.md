# News
- 2015.01.08 托管至 gitcafe
    由于 Copr 源包含个别私有软件包, 本源将接受审查并删除部分软件包. myrepo 源 fedora 21 x86_64 的全部软件包都已托管至 https://gitcafe.com/sensor/myrepo , 请移步添加此源. fedora 其他版本以及 centos 7 源将删除私有软件, 已有的开源软件不受影响.

***

# Introduction
这是我的 fedora 个人软件源 - **[myrepo](https://copr.fedoraproject.org/coprs/mosquito/myrepo/)**, 目前包含以下源:
- **[myrepo](https://copr.fedoraproject.org/coprs/mosquito/myrepo/)** : 此源支持 fedora 19/20/21/rawhide, rhel 7. 包含一些不错的第三方软件, 如 搜狗输入法, bcloud, point, 深度音乐等;
- **[myrepo-testing](https://copr.fedoraproject.org/coprs/mosquito/myrepo-testing/)** : 此源主要用于测试, myrepo 源中的个别软件依赖此源的软件包;
- **[myrepo-el6](https://copr.fedoraproject.org/coprs/mosquito/myrepo-el6/)** : 此源更新了 rhel 6 老旧的软件包, 并且使 rhel 6 成功的运行了 google chrome 28+;
- **[myrepo-dev](https://copr.fedoraproject.org/coprs/mosquito/myrepo-dev/)** : 此源主要用于编译并测试 rpm 包.

***

## Introduction myrepo repository

**Fedora 19/20/21/rawhide Include:** pidgin-sendscreenshot, pidgin-openfetion, pidgin-lwqq, lwqq, libofetion, wiznote, sogou-pinyin, sogou-pinyin-skins, libgooglepinyin, fcitx-googlepinyin, fcitx-rime, openyoudao, deepin-utils, deepin-gsettings, deepin-ui, pyjavascriptcore, deepin-music-player, dmusic-plugin-baidumusic, osdlyrics, pointdownload, mvgather, fcitx-qt5, libqtav, deepin-screenshot, deepin-translator, python-tesseract, python-pyocr, deepin-qml-widgets, deepin-menu, chrpath, xware-desktop, bcloud, screenfetch, musicbox, moonplayer, gouyong, doubanfm-qt, douban.fm, kwplayer, python-mutagen, python3-xlib, python3-keybinder, python3-cairo, pygobject+patch, simplescreenrecorder, guake, python-html2text, ibus-rime, opera-stable, tragtor, opera-beta, opera-developer, xorg-x11-drv-nvidia-340xx, nvidia-340xx-kmod, google-chrome-release...   

**RHEL/CentOS 7 Include(included above list):** pidgin, fcitx, fcitx-configtool, kcm-fcitx, fcitx-ui-light, fcitx-fbterm, fcitx-cloudpinyin, gflags, glog, yaml-cpp, librime, brise, fcitx-libpinyin, sunpinyin, fcitx-sunpinyin, pywebkitgtk, python-keybinder, python-pyquery, python-restkit, python-socketpool, python-http-parser, libmpd-devel, xmms2-devel, Pyrex, ecore-devel, eet-devel, libeina-devel, evas-devel, tslib-devel, libmodplug-devel, libdbusmenu-gtk2-devel, libindicator, libappindicator, python-enum34, python-inotify, zbar-pygtk, python-xpyb, tesseract-langpack, python-cssselect, python-lxml, Cython, pygobject3, python3-cairo, python-urllib3, python-tornado, python-mock, python-nose, python-coverage, python-six, pytest, python-py, python-crypto, python-keyring, dbus-python, rtmpdump, faac, xvidcore, libdc1394, lame, libmp4v2, opencore-amr, vo-amrwbenc, python3-ply, python3-plyvel...   

**RHEL/CentOS 6 Include:** wiz-note (**Testing**), qt-4.8.6, screenfetch, musicbox...

**Software list:**

- pidgin-lwqq - 使用 WebQQ 协议编写的 pidgin-QQ 插件   
- pidgin-openfetion - 使用 fetion v4 协议编写的 pidgin 飞信插件   
- pidgin-sendscreenshot - pidgin 截图插件   
- wiznote - 为知笔记   
- sogou-pinyin - 搜狗拼音输入法，基于 fcitx 框架开发   
- sogou-pinyin-skins - 搜狗拼音输入法皮肤   
- fcitx-googlepinyin - 基于 fcitx 框架的谷歌拼音输入模块   
- fcitx-rime - 中州韵输入法   
- fcitx-libpinyin - 基于 fcitx 框架的 libpinyin 输入法   
- fcitx-sunpinyin - 基于 fcitx 框架的 sunpinyin 输入法   
- fcitx-configtool, kcm-fcitx - GTK 和 KDE 下的 fcitx 配置工具   
- openyoudao - 一个 python 编写的有道词典 linux 客户端   
- deepin-music-player - 深度音乐播放器   
- dmusic-plugin-baidumusic - 深度音乐播放器的百度音乐插件   
- osdlyrics - 支持多款音乐播放器的桌面歌词软件   
- pointdownload - 一款方便高效的下载软件    
- mvgather - 一款支持影视点播的视频客户端，内容来自 yunfan.com   
- deepin-screenshot - 深度截图   
- deepin-translator - 深度翻译   
- xware-desktop - 迅雷桌面版   
- bcloud - 百度云的 linux 客户端   
- screenfetch - 获取系统/主题信息的命令行工具   
- musicbox - 网易云音乐的命令行客户端   
- moonplayer - 视频播放器，支持搜索播放 youku, tudou, iqiyi, sohu, 56, funshion 的网络视频    
- gouyong - 够用翻译，支持取词   
- doubanfm-qt - 基于 Qt5 开发的 DoubanFM 客户端   
- douban.fm - 基于 NodeJS 开发的 DoubanFM CLI 客户端   
- kwplayer - 基于 python3 开发的酷我音乐 linux 客户端   
- simplescreenrecorder - 简约而不简单的录屏软件   
- guake - 方便实用的下拉式终端   
- wps-office - 兼容 Microsoft Office 格式的国产办公软件   
- opera-{stable,beta,developer} - opera 浏览器   
- chromium-snapshots, chromium-continuous - chromium 最新预编译版   
- tragtor - 方便的音视频转换工具，是 ffmpeg 的 GUI 前端   
- google-chrome-release - 为 chrome rpm 做镜像源   
- akmod-nvidia-340xx - 自动编译 nvidia 显卡驱动内核模块   
- kmod-nvidia-340xx - 预编译 nvidia 显卡驱动内核模块    
未完待续...   

**Package status list:** [click here](https://raw.githubusercontent.com/1dot75cm/myrepo/master/package_status).

***

## Feedback - 反馈
- 任何关于软件包的问题，可以通过如下几种方式反馈：    
    - Email：sensor.wen-AT-gmail.com
    - 贴吧：[CentOS][0-1]、[Fedora][0-2]
    - Github：[https://github.com/1dot75cm/myrepo](https://github.com/1dot75cm/myrepo)

## Add repo - 添加源
- Fedora 19/20/21/rawhide 使用以下命令添加源：   
  `# yum install dnf-plugins-core`   
  `# dnf copr enable mosquito/myrepo`    
  `# yum localinstall http://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm http://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm`

- RHEL/CentOS 6/7 不包含 dnf 软件包，使用以下命令添加源：   
  `# yum-config-manager --add-repo=https://copr.fedoraproject.org/coprs/mosquito/myrepo/repo/epel-$(rpm -E %?rhel)/mosquito-myrepo-epel-$(rpm -E %?rhel).repo`   
  `# yum install epel-release`    
  `# yum localinstall http://li.nux.ro/download/nux/dextop/el$(rpm -E %rhel)/x86_64/nux-dextop-release-0-2.el$(rpm -E %rhel).nux.noarch.rpm http://download1.rpmfusion.org/nonfree/el/updates/$(rpm -E %rhel)/x86_64/rpmfusion-nonfree-release-$(rpm -E %rhel)-1.noarch.rpm http://download1.rpmfusion.org/free/el/updates/$(rpm -E %rhel)/x86_64/rpmfusion-free-release-$(rpm -E %rhel)-1.noarch.rpm`    
**注意**：rhel/centos 6/7 需要添加 *epel* 、 *rpmfusion* 、*Nux Dextop* 源。Nux 源的个别包与 base 源有冲突，建议使用 yum-plugin-priorities 为源分级。   

- 配置 repository 优先级：   
    - `# yum install yum-plugin-priorities`
    - `# vim /etc/yum.repos.d/源名.repo`   
    `[repo_name]`   
    `name= 源全名`   
    `baseurl= 源地址`   
    `enabled= 1启用 0禁用`   
    `priority= 优先级 (范围: 1-99, 1 最高)`
    - 建议 *base*, *updates*, *epel*, *mosquito-myrepo* 优先级为 1，其他源 (*rpmfusion*, *remi*, *Nux Dextop*, *RPMforge* 等) 设为 2。这样会减少源之间的软件包冲突。
    - 更新时有冲突的，可使用 `# yum update --exclude=Package_Name` 来排除某个软件包。
    - 因安装脚本报错而无法卸载的，可使用 `# rpm -e --noscripts Package_Name` 来卸载软件包，目前正在除虫。

- 查看本源包含的软件包列表：   
  `# yum list available --disablerepo=* --enablerepo=mosquito-myrepo`

***

## 0) Fast installation - 无脑安装以下软件
- 添加源操作完成后，Fedora 19/20/21/rawhide 执行以下命令进行无脑安装：   
  `# yum install pidgin-lwqq pidgin-sendscreenshot pidgin-openfetion wiz-note sogou-pinyin sogou-pinyin-skins fcitx-cloudpinyin fcitx-googlepinyin fcitx-rime fcitx-libpinyin fcitx-sunpinyin sunpinyin-data openyoudao deepin-music-player dmusic-plugin-baidumusic osdlyrics pointdownload mvgather deepin-screenshot`

- RHEL/CentOS 7 执行以下命令进行无脑安装：   
  `# yum-config-manager --enable epel-testing > /dev/null`    
  `# yum install pidgin-lwqq pidgin-sendscreenshot pidgin-openfetion wiz-note sogou-pinyin sogou-pinyin-skins fcitx-cloudpinyin fcitx-googlepinyin fcitx-rime fcitx-libpinyin fcitx-sunpinyin sunpinyin-data openyoudao deepin-music-player dmusic-plugin-baidumusic osdlyrics pointdownload mvgather deepin-screenshot`

    注：el6 软件源的软件正在内部测试。

## 1) Install [lwqq][] - 安装 lwqq
- 测试系统：fc20√、fc21√、el7√
- 执行以下命令安装lwqq：   
  `# yum install pidgin-lwqq pidgin-sendscreenshot`   
lwqq 配置请参考[用户手册][]。其中包括：配置 lwqq 与 GNOME3 集成、pidgin推荐插件等内容。

    参考：[lwqq][1-1]、[pidgin-lwqq][1-2]、[pidgin-sendscreenshot][1-3]、[GNOME3 支持][1-4]、[pidgin推荐插件][1-5]

## 2) Install [fetion][] - 安装飞信
- 测试系统：fc20√、fc21√、el7√
- 执行以下命令安装飞信：   
  `# yum install pidgin-openfetion`

    参考：[ofetion][2-1]、[libofetion][2-2]、[pidgin-openfetion][2-3]

## 3) Install [WizNote][] - 安装为知笔记
- 测试系统：fc20√、fc21√、el7√、el6√
- 执行以下命令安装为知笔记：   
  `# yum install wiznote`  # 稳定版   
  `# yum install wiznote-beta`  # 开发版

    注1：如果使用 fcitx 无法输入，则需要安装 fcitx-qt5。   

    参考：[WizQTClient][3-1]、[其他发行版安装方法][3-2]

## 4) Install [sogou][] - 安装搜狗拼音输入法
- 测试系统：fc20√、fc21√、el7√
- 执行以下命令安装搜狗拼音：   
  `# yum install sogou-pinyin sogou-pinyin-skins`   

- ** Configuration fcitx **

    1. 禁止 ibus 自动启动 (ibus 启动会覆盖 fcitx 环境变量)   
 `$ sudo setfacl -m u:用户名:rw /usr/bin/ibus-daemon`   
    2. 结束 ibus 守护进程   
 `$ sudo pkill ibus-daemon`   
    3. 关闭 gnome-shell 对键盘的监听   
 `$ gsettings set org.gnome.settings-daemon.plugins.keyboard active false`   
    4. 切换输入法为 fcitx   
 `$ imsettings-switch fcitx`   
    5. 配置 xinputrc 链接到 fcitx.conf   
 `$ sudo alternatives --config xinputrc`   
    6. 重载 fcitx, 启动搜狗面板   
 `$ fcitx -r; fcitx-configtool`   
 `$ sogou-qimpanel-watchdog; sogou-qimpanel`   

    注1：重启系统后，会自动启动搜狗面板。   
    注2：以普通用户执行以上命令。   
    注3：el7 如果碰到运行 firefox 等 gtk2 程序时，输入框无法跟随的问题。这是由于输入法模块缓存更新失败造成无法找到 fcitx 输入法模块。请以 root 身份执行以下命令:   
 `# gtk-query-immodules-2.0-64 > /lib64/gtk-2.0/2.10.0/immodules.cache`   

    参考：[fcitx 维基百科][4-1]、[fcitx项目主页][4-2]、[fcitx Github][4-3]

## 5) Install input method - 安装xx输入法
- 测试系统：fc20√、fc21√、el7√
- 选择喜欢的输入法，使用 yum 安装，之后使用 fcitx-configtool 等配置工具进行配置即可。  
  `# yum install fcitx-googlepinyin fcitx-cloudpinyin` **\# [谷歌拼音][]输入法**   
  `# yum install fcitx-rime fcitx-cloudpinyin` **\# [中州韵][]输入法**   
  `# yum install fcitx-libpinyin fcitx-cloudpinyin` **\# [libpinyin][]输入法**   
  `# yum install fcitx-sunpinyin sunpinyin-data fcitx-cloudpinyin` **\# [sunpinyin][]输入法**   

    fedora 源已包含 libpinyin 和 sunpinyin，此包提供给 rhel/centos 7 系统使用。   

    参考：[fcitx 包列表][5-1]、[fcitx][5-2]、[fcitx-configtool][5-3]、[kcm-fcitx][5-4]、[fcitx-ui-light][5-5]、[fcitx-fbterm][5-6]、[fcitx-cloudpinyin][5-7]、[libgooglepinyin][5-8]、[fcitx-googlepinyin][5-9]、[gflags][5-10]、[glog][5-11]、[yaml-cpp][5-12]、[librime][5-13]、[brise][5-14]、[fcitx-rime][5-15]、[fcitx-libpinyin][5-16]、[open-gram项目][5-17]、[sunpinyin][5-18]、[fcitx-sunpinyin][5-19]

## 6) Install [openyoudao][] - 安装有道词典
- 测试系统：fc20√、fc21√、el7√
- Fedora 19/20/21/rawhide 使用以下命令安装：  
  `# yum install openyoudao`   

- RHEL/CentOS 7 使用以下命令安装：   
  `# yum --enablerepo=epel-testing install openyoudao`

    参考：[openyoudao项目][6-1]、[openyoudao Github][6-2]

## 7) Install [Deepin Music Player][] - 安装深度音乐播放器
- 测试系统：fc20√、fc21√、el7√
- Fedora 19/20/21/rawhide、RHEL/CentOS 7 使用以下命令安装：  
  `# yum install deepin-music-player dmusic-plugin-baidumusic`

    PS：国外有大神将 deepin 桌面环境移植到 Arch 了。我在移植 deepin-media-player 就遇到困难了。它现在已经不维护了，新的 deepin-movie 需要的依赖太多，移植成功再发上来吧。    
    参考：[deepin官网][7-1]、[deepin-music Github][7-2]

## 8) Install [osdlyrics][] - 安装桌面歌词
- 测试系统：fc20√、fc21√、el7√
- 一款桌面歌词软件，支持常用的音乐播放器，如 Amarok, Audacious, Banshee, Rhythmbox, VLC 等。Fedora / RHEL 7 使用如下命令安装：    
  `# yum install osdlyrics`

    参考：[osdlyrics Github][8-1]

## 9) Install [PointDownload][] - 安装点载
- 测试系统：fc20√、fc21√、el7√
- 一款方便高效的下载软件，支持 HTTP, BT, Magnet, ed2k, Thunder 等下载协议，支持迅雷离线加速和高速通道功能，支持视频下载功能。Fedora / RHEL 7 使用如下命令安装：    
  `# yum install pointdownload`
 
    注1：安装完成后，如果未成功安装 firefox、chrome 插件，需手动安装。(/usr/share/pointdownload/extensions/)

    参考：[PointDownload Github][9-1]、[Deepin 社区讨论贴][9-2]

## 10) Install [MvGather][] - 安装影视集结号
- 测试系统：fc20√、fc21√、el7√
- 一款视频点播软件，支持电影点播，电视直播。Fedora / RHEL 7 使用如下命令安装：    
  `# dnf copr enable mosquito/myrepo-testing`   
  `#(el7) yum-config-manager --add-repo=https://copr.fedoraproject.org/coprs/mosquito/myrepo-testing/repo/epel-$(rpm -E %?rhel)/mosquito-myrepo-testing-epel-$(rpm -E %?rhel).repo`   
  `# yum install mvgather`

    注1：如果使用 fcitx 无法输入，则需要安装 fcitx-qt5。     

    参考：[Deepin 社区讨论贴][10-1]、[fcitx-qt5][10-2]、[libqtav][10-3]、[mvgather Github][10-4]

## 11) Install [Deepin Screenshot][] - 安装深度截图
- 测试系统：fc20√、fc21√、el7√
- 深度截图，支持截图编辑，分享微博。可以自定义快捷键为 ctrl+alt+a，这样就更像 QQ 截图了。Fedora 使用如下命令安装：    
  `# yum install deepin-screenshot`

    参考：[Deepin 社区讨论贴][11-1]

## 12) Install [Deepin Translator][] - 安装深度翻译
- 测试系统：fc20√、fc21√、el7√
- 深度翻译，支持鼠标取词，词库来自有道、谷歌翻译服务。另外，源中的 GoldenDict 也挺好用的。Fedora 使用如下命令安装：   
  `# dnf copr enable mosquito/myrepo-testing`  # PyQt5 在测试源, 建议卸载低版本的 sip 和 PyQt4   
  `# yum install deepin-translator`

- RHEL/CentOS 7 使用以下命令安装：   
  `# yum-config-manager --add-repo=https://copr.fedoraproject.org/coprs/mosquito/myrepo-testing/repo/epel-$(rpm -E %?rhel)/mosquito-myrepo-testing-epel-$(rpm -E %?rhel).repo`   
  `# yum install --enablerepo=epel-testing deepin-translator`

    参考：[python-pyocr][12-1]、[python-tesseract][12-2]、[deepin-qml-widgets][12-3]、[deepin-menu][12-4]

## 13) Install [Xware Desktop][] - 安装迅雷桌面版
- 测试系统：fc20√、fc21√、el7√
- Xware Desktop 作为 Xware 的前端，提供与 windows 版迅雷功能相当的体验。Fedora / RHEL 7 使用如下命令安装：   
  `# dnf copr enable mosquito/myrepo-testing`   
  `#(el7) yum-config-manager --add-repo=https://copr.fedoraproject.org/coprs/mosquito/myrepo-testing/repo/epel-$(rpm -E %?rhel)/mosquito-myrepo-testing-epel-$(rpm -E %?rhel).repo`   
  `# yum install xware-desktop`

    参考：[使用说明][13-1]、[发行版支持情况][13-2]

## 14) Install [BCloud][] - 安装百度云
- 测试系统：fc20√、fc21√、el7√
- BCloud 是百度云的 linux 桌面客户端。采用类似 nautilus 的操作模式，支持上传、下载、播放网盘中的视频等功能。Fedora / RHEL 7 使用以下命令安装：   
  `# yum install bcloud`

    参考：[BCloud Github][14-1]

## 15) Install [screenFetch][] - 安装 screenFetch
- 测试系统：fc20√、fc21√、el7√、el6√
- screenFetch 是一款获取系统/主题信息的命令行工具。Fedora / RHEL 使用以下命令安装：   
  `# yum install screenfetch`

    参考：[screenFetch Github][15-1]

## 16) Install [MusicBox][] - 安装网易云音乐
- 测试系统：fc20√、fc21√、el7√
- MusicBox 是一款 Python 编写的网易云音乐 CLI 客户端。Fedora / RHEL 使用以下命令安装：   
  `# yum install musicbox`

    参考：[MusicBox Github][16-1]

## 17) Install [MoonPlayer][] - 安装 moonplayer
- 测试系统：fc20√、fc21√、el7√
- moonplayer 是一款简约的视频播放器，支持搜索播放 youku, tudou, iqiyi, sohu, 56, funshion 的网络视频。Fedora / RHEL 7 使用以下命令安装：   
  `# yum install moonplayer`

    注1：el7 播放视频只有声音没有图像的问题，请尝试将设置中的 "视频输出" 修改为 gl。     

    参考：[moonplayer Github][17-1]、[视频插件][17-2]、[插件编写指南][17-3]、[Chrome 扩展][17-4]

## 18) Install [GouYong][] - 安装够用翻译
- 测试系统：fc20√ (软件不太完善，只编译了 fc20)
- gouyong 是一款简约的翻译软件，目前仅支持网络取词，离线词典不可用。Fedora 使用以下命令安装：   
  `# yum install gouyong`

    参考：[GouYong Github][18-1]、[deepin 讨论贴][18-2]

## 19) Install [DoubanFM][] - 安装豆瓣FM (qt5)
- 测试系统：fc20√、fc21√、el7√
- DoubanFM 是一款界面精美的豆瓣FM 客户端。Fedora / RHEL 7 使用以下命令安装：   
  `# yum install doubanfm-qt`

    参考：[doubanfm-qt GitCafe][19-1]

## 20) Install [douban.fm][] - 安装豆瓣FM (cli)
- 测试系统：fc20√、fc21√、el7√
- douban.fm 是一款优雅的豆瓣FM 命令行客户端，基于 NodeJS。Fedora / RHEL 7 使用以下命令安装：   
  `# yum install nodejs-douban.fm`

- 简单教程

    - 账户及配置保存在 `~/.douban.fm.profile.json`
    - 歌曲默认保存在 `~/douban.fm`
    - `$ douban.fm config`  # 配置豆瓣FM
    - [enter] -> 播放
    - [backspace] -> 暂停
    - [n] -> 下一首
    - [q] -> 退出
    - [jk] -> 下上
    - [l] -> 加红心

    参考：[douban.fm Github][20-1]

## 21) Install [Kwplayer][] - 安装酷我音乐
- 测试系统：fc20√、fc21√、el7√
- Kwplayer 是一款使用 python3 编写的酷我音乐 linux 客户端。Fedora / RHEL 7 使用以下命令安装：   
  `# yum install kwplayer`

    参考：[kwplayer Github][21-1]、[python-mutagen][21-2]、[python3-xlib][21-3]、[python3-keybinder][21-4]、[python3-cairo patch][21-5]、[python3-gobject patch][21-6]

## 22) Install [SimpleScreenRecorder][] - 安装屏幕录像机
- 测试系统：fc21√、el7√
- SimpleScreenRecorder 是一款易于使用的录屏软件，提供丰富的自定义选项。Fedora / RHEL 7 使用以下命令安装：   
  `# yum install simplescreenrecorder`

- 特性：
    - 用户界面基于 Qt
    - 比 VLC 和 ffmpeg/avconv 更快
    - 全屏或区域录制，直接录制 OpenGL 应用程序
    - 同步录制音视频
    - 任何时候都能暂停/恢复记录（按钮/热键）
    - 显示录制过程中的统计数据（文件大小、比特率、录音时间、实际帧率等）
    - 可在录制过程中显示预览

    参考：[SimpleScreenRecorder Github][22-1]、[main page][22-2]

## 23) Install [Guake][] - 安装下拉式终端
- 测试系统：fc21√
- Guake 是一款方便实用的终端程序，只要按 F12 即可弹出/关闭终端。十分适合临时执行命令，无需费时打开其他终端。Fedora / RHEL 7 使用以下命令安装：   
  `# yum install guake`

    参考：[Guake Github][23-1]

## 24) Install [wps office][] - 安装 WPS
- 测试系统：fc21√
- WPS Office 是一款兼容 Microsoft Office 格式的国产办公软件。包含办公软件最常用的文字、表格、演示等功能。Fedora / RHEL 7 使用以下命令安装：   
  `# yum install http://kdl.cc.ksosoft.com/wps-community/download/a16/wps-office-9.1.0.4945-1.a16p3.i686.rpm`

- 以下字体，由于版权问题，没有提供：

    - MTCORSVA.TTF
    - courbi.ttf
    - couri.ttf
    - cour.ttf
    - courbd.ttf
    - monotypesorts.ttf
    - Mt Extra Tiger.ttf
    - mtextra_01.ttf
    - symbol.ttf
    - Symbol Tiger.ttf
    - Symbol Tiger Expert.ttf
    - wingding.ttf
    - WINGDNG2.TTF
    - WINGDNG3.TTF

    参考：[wps community][24-1]、[wps wiki][24-2]

## 25) Install [Opera][] - 安装 Opera 浏览器
- 测试系统：fc21√
- Opera 浏览器是一款由挪威 Opera Software ASA 公司开发的多页面标签式浏览器。基于 Chromium 并使用 Webkit 内核。Fedora / RHEL 7 使用以下命令安装：   
  `# yum install opera-{stable,beta,developer}`

    注：启用 flash 需要安装 Google Chrome, 启用 h264 需要安装 ffmpeg

    参考：[opera.com][25-1]、[linuxtoy news][25-2]、[启用 flash 和 h264][25-3]

## 26) Install [Chromium][] - 安装 Chromium 浏览器
- 测试系统：fc21√
- Chromium 是由 Google 主导，社区维护的开源项目。众多浏览器都是基于此项目二次开发。由于官方下载站速度极其缓慢，本人转存了一份由 build.chromium.org 编译的最新预编译版 (每天更新)。   
    - chromium-continuous : [x86_64](http://hello-sensorwen.rhcloud.com/src/chromium-continuous.zip) ([version](http://hello-sensorwen.rhcloud.com/src/chromium-continuous))
    - chromium-snapshots : [x86_64](http://hello-sensorwen.rhcloud.com/src/chromium-snapshots.zip) ([version](http://hello-sensorwen.rhcloud.com/src/chromium-snapshots))

    参考：[chromium-continuous][26-1]、[chromium-snapshots][26-2]、[Download Chroimum][26-3]

## 27) Install [traGtor][] - 安装 traGtor
- 测试系统：fc21√
- traGtor 是一款 python 编写的音视频转换器，后端使用 ffmpeg。Fedora / RHEL 7 使用以下命令安装：   
  `# yum install tragtor`

    参考：[traGtor][27-1]、[ffmpeg 图形前端][27-2]

## 28) Install [Chrome][] - 安装 Chrome 浏览器
- 测试系统：fc21√
- 由于天朝有伟大的防火墙存在，导致 Google Chrome 源无法连接，更新 Chrome 十分不方便。本人利用云空间和 gitcafe，托管了一份源镜像，解决了此问题。Fedora / RHEL 7 使用以下命令添加源：   
  `# yum install google-chrome-release`   
  `# yum install google-chrome-{stable,beta,unstable}`   

    注1：如果已存在 "google-chrome.repo"，则新文件以 ".rpmnew" 后缀保存   
    注2：使用 chattr 命令为 repo 文件添加了 i 属性，防止官方包修改。如需修改请使用 `chattr -i file.repo` 取消 i 属性   

    参考：[dev channel][28-1]

## 29) Install [akmod-nvidia-340xx][] - 安装 NVIDIA 闭源显卡驱动
- 测试系统：fc21√
- 事情是这样的。前几天 VMware 发布了 VMware Workstation 11。我心血来潮，尝试在 vkst for linux 上安装 Yosemite。引导 Yosemite 时，提示需要显卡驱动。于是，又开始搞驱动。原来安装 N 卡驱动都是从官网上下载安装，这次尝试使用 rpm 安装。rpmfusion 源中的 N 卡驱动有 kmod-nvidia 和 akmod-nvidia 之分。它们的区别是 kmod 是预编译好的内核模块；而 akmod 则包含一个 srpm 包，每次更新内核后，akmods.service 都会检查是否存在所需的内核模块，如果不存在，则调用 akmodsbuild 编译 srpm 包，为新内核提供模块。akmod 对于普通用户来说更省事。

- [NVIDIA 显卡驱动型号对照表](ftp://download.nvidia.com/XFree86/Linux-x86/340.65/README/supportedchips.html):    
    - 346.xx：GF400(M) - GF900(M) 系列    
    - 343.xx：GF400(M) - GF900(M) 系列    
    - 340.xx：GF8(M) - GF100(M) - GF800M 系列    
    - 304.xx：GF6 - GF600(M) 系列    
    - 173.14.xx：GeForce 5 系列    
    - 96.43.xx：GF2 - GF4 系列    
    - 71.86.xx：GeForce TNT, GF2 系列    

- 由于目前 rpmfusion 源中不包含 340.xx 驱动，304.xx 又太老。所以自己动手打包了 340.xx 驱动。Fedora 按照以下步骤安装：   
    1. 安装 gcc, kernel-devel   
    2. 根据显卡型号选择合适的驱动   
    `# lspci | grep VGA`
    3. 安装显卡驱动   
    `# yum install akmod-nvidia-340xx`
    4. 启用 vdpau/vaapi 硬解码需安装以下包   
    `# yum install vdpauinfo libva-vdpau-driver libva-utils`

    参考：[Howto/nVidia][29-1]、[X Config Options][29-2]、[kmod 与 akmod][29-3]

***

## Changelog
- 2014.12.31 03:00 CST - 添加软件包    
    \- fedora 源：  
        `google-chrome-release`

- 2014.12.24 23:50 CST - 添加 nvidia 闭源驱动包    
    \- fedora 源：  
        `opera-beta, opera-developer, xorg-x11-drv-nvidia-340xx, nvidia-340xx-kmod`

- 2014.12.17 00:24 CST - 添加软件包, 添加 chrome 镜像源地址    
    \- fedora 源：  
        `tragtor`

- 2014.12.11 17:26 CST - 添加软件包, 添加 wps 安装步骤, 添加 chromium 转存地址    
    \- fedora 源：  
        `opera-stable`

- 2014.11.29 01:30 CST - 添加软件包    
    \- fedora 源：  
        `pygobject+patch, simplescreenrecorder, guake`

- 2014.11.20 18:00 CST - wiznote v2.1.14 发布 ([Changelog](http://blog.wiz.cn/wiznote-linux.html))   
    \- 为知笔记 v2.1.14 分支代码已于 2014年11月19日 测试完毕。本源稍后更新稳定版 rpm 包

- 2014.11.18 20:00 CST - 自动化构建 rpm 包   
    \- 自动化构建 rpm 包, 可及时快速更新 rpm 包, 一般不需要人工介入

- 2014.11.18 03:30 CST - 添加软件包    
    \- fedora 源：  
        `kwplayer, python-mutagen, python3-xlib, python3-keybinder, python3-cairo`

- 2014.11.12 20:46 CST - 添加 rpm 包状态列表   
    \- rpm 包状态列表, 方便用户查看库中的软件包版本及状态信息

- 2014.11.4 02:00 CST - 批量获取版本信息   
    \- 批量获取 git 库版本信息, 准备自动化构建 rpm 包

- 2014.10.30 02:30 CST - 添加软件包    
    \- fedora 源：  
        `screenfetch, musicbox, moonplayer, gouyong, doubanfm-qt, douban.fm`

- 2014.10.13 22:30 CST - 添加软件包, 更新 mvgather (支持 el7 )    
    \- rhel 7 源：   
        `dbus-python, rtmpdump, faac, xvidcore, libdc1394, lame, libmp4v2, opencore-amr, vo-amrwbenc`

- 2014.10.12 05:20 CST - 添加软件包, 完成软件包测试    
    \- fedora 源：  
        `bcloud`

    \- rhel 7 源：   
        `zbar-pygtk, python-xpyb, tesseract-langpack, python-cssselect, python-lxml, Cython, pygobject3, python3-cairo, python-urllib3, python-tornado, python-mock, python-nose, python-coverage, python-six, pytest, python-py, python-crypto, python-keyring`

- 2014.10.11 03:05 CST - 添加软件包, 完成部分包测试    
    \- fedora 源：  
        `chrpath, xware-desktop`

    \- rhel 7 源：   
        `libdbusmenu-gtk2-devel, libindicator, libappindicator, python-enum34, python-inotify`

- 2014.10.6 04:46 CST - 添加软件包    
    \- fedora 源：  
        `mvgather, fcitx-qt5, libqtav, deepin-screenshot, deepin-translator, python-tesseract, python-pyocr, deepin-qml-widgets, deepin-menu`

- 2014.9.26 22:50 CST - 添加软件包    
    \- fedora / rhel 7 源：  
        `osdlyrics, pointdownload`

    \- rhel 7 源：   
        `libmpd-devel, xmms2-devel, Pyrex, ecore-devel, eet-devel, libeina-devel, evas-devel, tslib-devel, libmodplug-devel`

- 2014.9.24 02:50 CST - 添加软件包, 更新为知笔记    
    \- fedora / rhel 7 源：   
        `deepin-utils, deepin-gsettings, deepin-ui, pyjavascriptcore, deepin-music-player, dmusic-plugin-baidumusic`

    \- rhel 7 源：    
        `python-keybinder, python-pyquery, python-restkit, python-socketpool, python-http-parser`

- 2014.9.17 03:52 CST - 添加软件包    
    \- fedora 源：    
        `libgooglepinyin, fcitx-googlepinyin, fcitx-rime, openyoudao`

    \- rhel 7 源：    
        `pidgin, fcitx, fcitx-configtool, kcm-fcitx, fcitx-ui-light, fcitx-fbterm, fcitx-cloudpinyin, gflags, glog, yaml-cpp, librime, brise, fcitx-libpinyin, sunpinyin, fcitx-sunpinyin, pywebkitgtk`

- 2014.9.12 19:27 CST - 使用 copr 编译系统    
    \- 添加软件包：    
        `pidgin-lwqq, lwqq, pidgin-openfetion, libofetion, pidgin-sendscreenshot, wiz-note, sogou-pinyin, sogou-pinyin-skins`

- 2014.8.22 10:26 CST - 更新搜狗拼音    
    \- 更新 sogou-pinyin-1.1.0.0037

- 2014.7.6 20:56 CST - 打包搜狗拼音    
    \- 打包 sogou-pinyin-1.0.0.0033, sogou-pinyin-skins

***

[0-1]:http://tieba.baidu.com/p/3293480718
[0-2]:http://tieba.baidu.com/p/3135900643
[lwqq]:https://github.com/xiehuc/lwqq/wiki/About-Help "关于lwqq项目"
[用户手册]:https://github.com/xiehuc/pidgin-lwqq/wiki/simple-user-guide "用户手册"
[1-1]:https://github.com/xiehuc/lwqq "lwqq Github"
[1-2]:https://github.com/xiehuc/pidgin-lwqq "pidgin Github"
[1-3]:https://github.com/oglops/pidgin-sendscreenshot "pidgin-sendscreenshot Github"
[1-4]:https://github.com/xiehuc/pidgin-lwqq/wiki/gnome3-support "GNOME3 支持"
[1-5]:https://github.com/xiehuc/pidgin-lwqq/wiki/Recommend-Plugin "pidgin推荐插件"
[fetion]:https://code.google.com/p/ofetion/ "ofetion项目"
[2-1]:https://code.google.com/p/ofetion/ "ofetion项目"
[2-2]:https://ofetion.googlecode.com/files/libofetion-2.2.2.tar.gz "libofetion-2.2.2.tar.gz"
[2-3]:https://ofetion.googlecode.com/files/pidgin-openfetion-0.3.tar.gz "pidgin-openfetion-0.3.tar.gz"
[WizNote]:http://www.wiz.cn/ "为知笔记"
[3-1]:https://github.com/WizTeam/WizQTClient "WizQTClient Github"
[3-2]:http://blog.wiz.cn/wiznote-linux.html "wiznote Linux"
[sogou]:http://pinyin.sogou.com/linux/ "搜狗拼音输入法"
[4-1]:http://zh.wikipedia.org/wiki/FCITX "fcitx wiki"
[4-2]:https://fcitx-im.org/wiki/Fcitx/zh-cn "小企鹅输入法"
[4-3]:http://github.com/fcitx/ "fcitx Github"
[谷歌拼音]:https://github.com/fcitx/fcitx-googlepinyin "fcitx-googlepinyin Github"
[中州韵]:https://code.google.com/p/rimeime/ "中州韵输入法"
[libpinyin]:https://github.com/fcitx/fcitx-libpinyin "libpinyin Github"
[sunpinyin]:https://github.com/sunpinyin/sunpinyin "sunpinyin Github"
[5-1]:https://fcitx-im.org/wiki/Distribution_Package_Status "fcitx 包列表"
[5-2]:https://github.com/fcitx/fcitx "fcitx Github"
[5-3]:https://github.com/fcitx/fcitx-configtool "fcitx-configtool Github"
[5-4]:https://github.com/fcitx/kcm-fcitx "kcm-fcitx Github"
[5-5]:https://github.com/fcitx/fcitx-ui-light "fcitx-ui-light Github"
[5-6]:https://github.com/fcitx/fcitx-fbterm "fcitx-fbterm Github"
[5-7]:https://github.com/fcitx/fcitx-cloudpinyin "fcitx-cloudpinyin Github"
[5-8]:https://libgooglepinyin.googlecode.com "libgooglepinyin GoogleCode"
[5-9]:https://github.com/fcitx/fcitx-googlepinyin "fcitx-googlepinyin Github"
[5-10]:https://github.com/schuhschuh/gflags "gflags Github"
[5-11]:https://google-glog.googlecode.com "glog GoogleCode"
[5-12]:https://yaml-cpp.googlecode.com "yaml-cpp GoogleCode"
[5-13]:https://github.com/lotem/librime "librime Github"
[5-14]:https://github.com/lotem/brise "brise Github"
[5-15]:https://github.com/fcitx/fcitx-rime "fcitx-rime Github"
[5-16]:https://github.com/fcitx/fcitx-libpinyin "fcitx-libpinyin Github"
[5-17]:https://code.google.com/p/open-gram/ "open-gram项目"
[5-18]:https://github.com/sunpinyin/sunpinyin "sunpinyin Github"
[5-19]:https://github.com/fcitx/fcitx-sunpinyin "fcitx-sunpinyin Github"
[openyoudao]:http://openyoudao.org "openyoudao 主页"
[6-1]:http://openyoudao.org "openyoudao 主页"
[6-2]:https://github.com/justzx2011/openyoudao "openyoudao Github"
[Deepin Music Player]:http://linuxdeepin.com/img/feature/2014/img_yinyue_1.png "截图"
[7-1]:http://linuxdeepin.com "linuxdeepin"
[7-2]:https://github.com/linuxdeepin/deepin-music "deepin-music Github"
[osdlyrics]:https://code.google.com/p/osd-lyrics/ "GoogleCode"
[8-1]:https://github.com/osdlyrics/osdlyrics "osdlyrics Github"
[PointDownload]:https://raw.githubusercontent.com/PointTeam/PointDownload/gh-pages/images/PointDownloadScreenshot/PointDownloadMainUI/downloading.png "截图"
[9-1]:https://github.com/PointTeam/PointDownload "Point Github"
[9-2]:http://www.linuxdeepin.com/forum/23/21124 "Deepin 社区讨论贴"
[MvGather]:http://mvgather.com/ "MvGather 官网"
[10-1]:http://www.linuxdeepin.com/forum/49/23695 "Deepin 社区讨论贴"
[10-2]:https://github.com/fcitx/fcitx-qt5 "fcitx-qt5 Github"
[10-3]:https://github.com/wang-bin/QtAV "QtAV Github"
[10-4]:https://github.com/xsjqqq123/MvGather "mvgather Github"
[Deepin Screenshot]:https://github.com/linuxdeepin/deepin-screenshot "deepin screenshot Github"
[11-1]:http://www.linuxdeepin.com/forum/7 "Deepin 社区讨论贴"
[Deepin Translator]:https://github.com/linuxdeepin/deepin-translator "deepin translator Github"
[12-1]:https://github.com/jflesch/pyocr "pyocr Github"
[12-2]:https://python-tesseract.googlecode.com "python tesseract Googlecode"
[12-3]:https://github.com/linuxdeepin/deepin-qml-widgets "deepin qml widgets Github"
[12-4]:https://github.com/linuxdeepin/deepin-menu "deepin menu Github"
[Xware Desktop]:https://github.com/Xinkai/XwareDesktop "Xware Desktop Github"
[13-1]:https://github.com/Xinkai/XwareDesktop/wiki/使用说明 "使用说明"
[13-2]:https://github.com/Xinkai/XwareDesktop/wiki/发行版支持情况 "发行版支持情况"
[BCloud]:https://raw.githubusercontent.com/LiuLang/bcloud/master/screenshots/bcloud-light.png "截屏"
[14-1]:https://github.com/LiuLang/bcloud "BCloud Github"
[screenFetch]:https://github.com/KittyKatt/screenFetch "screenFetch Github"
[15-1]:https://github.com/KittyKatt/screenFetch "screenFetch Github"
[MusicBox]:http://sdut-zrt.qiniudn.com/687474703a2f2f692e696d6775722e636f6d2f4a35333533764b2e676966.gif "截图"
[16-1]:https://github.com/darknessomi/musicbox "musicbox Github"
[MoonPlayer]:https://raw.githubusercontent.com/coslyk/moonplayer/master/src/screenshot.png "截图"
[17-1]:https://github.com/coslyk/moonplayer "moonplayer Github"
[17-2]:http://forum.ubuntu.org.cn/viewtopic.php?f=74&t=456351 "视频插件"
[17-3]:http://code.google.com/p/moonplayer/wiki/PluginTutorial "插件编写指南"
[17-4]:https://github.com/coslyk/moonplayer/wiki/HomePageZH "Chrome 扩展"
[GouYong]:https://github.com/jiffies/GouYong "GouYong Github"
[18-1]:https://github.com/jiffies/GouYong "GouYong Github"
[18-2]:http://www.linuxdeepin.com/forum/49/24510 "deepin 讨论贴"
[DoubanFM]:https://gitcafe.com/zonyitoo/doubanfm-qt/raw/master/screenshot.png "截图"
[19-1]:https://gitcafe.com/zonyitoo/doubanfm-qt "doubanfm-qt GitCafe"
[douban.fm]:http://ww1.sinaimg.cn/large/61ff0de3tw1ecij3dq80bj20m40ez75u.jpg "截图"
[20-1]:https://github.com/turingou/douban.fm "douban.fm Github"
[Kwplayer]:https://raw.githubusercontent.com/LiuLang/kwplayer/master/screenshots/Theme.jpg "截图"
[21-1]:https://github.com/LiuLang/kwplayer "kwplayer Github"
[21-2]:https://bitbucket.org/lazka/mutagen "python-mutagen Bitbucket"
[21-3]:https://github.com/LiuLang/python3-xlib "python3-xlib Github"
[21-4]:https://github.com/LiuLang/python3-keybinder "python3-keybinder Github"
[21-5]:http://bugs.debian.org/688079 "python3-cairo patch"
[21-6]:https://bugs.freedesktop.org/show_bug.cgi?id=44336 "python3-gobject patch"
[SimpleScreenRecorder]:http://files.maartenbaert.be/simplescreenrecorder/screenshot.png "截图"
[22-1]:https://github.com/MaartenBaert/ssr "SimpleScreenRecorder Github"
[22-2]:http://www.maartenbaert.be/simplescreenrecorder/ "main page"
[Guake]:http://upload.wikimedia.org/wikipedia/commons/5/5b/Guake_on_sid3.jpg "截图"
[23-1]:https://github.com/Guake/guake "Guake Github"
[wps office]:http://www.wps.cn "wps 主页"
[24-1]:http://community.wps.cn "wps community"
[24-2]:http://community.wps.cn/wiki "wps wiki"
[Opera]:http://www-static.opera.com/static-heap/e3/e364154fa9ddc7c4fab06def7421f84b073657a4/linux.jpg "截图"
[25-1]:http://www.opera.com "Opera 主页"
[25-2]:https://linuxtoy.org/archives/opera-26-for-linux.html "linuxtoy.org news"
[25-3]:http://www.webupd8.org/2014/12/how-to-get-flash-and-h264-to-work-in.html "启用 flash 和 h264"
[Chromium]:http://www.chromium.org "chromium.org"
[26-1]:https://storage.googleapis.com/chromium-browser-continuous/ "chromium-continuous"
[26-2]:https://storage.googleapis.com/chromium-browser-snapshots/ "chromium-snapshots"
[26-3]:https://download-chromium.appspot.com/ "Download Chromium"
[traGtor]:http://www.linuxidc.com/upload/2013_07/130717222088492.png "截图"
[27-1]:http://mein-neues-blog.de/tragtor-gui-for-ffmpeg "tragtor homepage"
[27-2]:http://www.linuxidc.com/Linux/2013-07/87496.htm "ffmpeg 图形前端"
[Chrome]:https://www.google.com/chrome "chrome browser"
[28-1]:http://www.chromium.org/getting-involved/dev-channel "dev channel"
[akmod-nvidia-340xx]:http://www.geforce.cn/drivers "GeForce drivers"
[29-1]:http://rpmfusion.org/Howto/nVidia "How to install nVidia driver"
[29-2]:ftp://download.nvidia.com/XFree86/Linux-x86/340.65/README/xconfigoptions.html "X Config Options"
[29-3]:http://blog.robotshell.org/2011/fedora-kmod-and-akmod/ "kmod 与 akmod"
