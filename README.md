# Introduction
这是我的 fedora 个人软件源 - **[myrepo](https://copr.fedoraproject.org/coprs/mosquito/myrepo/)**, 目前包含以下源:
- **[myrepo](https://copr.fedoraproject.org/coprs/mosquito/myrepo/)** : 此源支持 fedora 19/20/21/rawhide, rhel 7. 包含一些不错的第三方软件, 如 搜狗输入法, bcloud, point, 深度音乐等;
- **[myrepo-testing](https://copr.fedoraproject.org/coprs/mosquito/myrepo-testing/)** : 此源主要用于测试, myrepo 源中的个别软件依赖此源的软件包;
- **[myrepo-el6](https://copr.fedoraproject.org/coprs/mosquito/myrepo-el6/)** : 此源更新了 rhel 6 老旧的软件包, 并且使 rhel 6 成功的运行了 google chrome 28+;
- **[myrepo-dev](https://copr.fedoraproject.org/coprs/mosquito/myrepo-dev/)** : 此源主要用于编译并测试 rpm 包.

***

## Introduction myrepo repository

**Fedora 19/20/21/rawhide Include:** pidgin-sendscreenshot, pidgin-openfetion, pidgin-lwqq, lwqq, libofetion, wiznote, sogou-pinyin, sogou-pinyin-skins, libgooglepinyin, fcitx-googlepinyin, fcitx-rime, openyoudao, deepin-utils, deepin-gsettings, deepin-ui, pyjavascriptcore, deepin-music-player, dmusic-plugin-baidumusic, osdlyrics, pointdownload, mvgather, fcitx-qt5, libqtav, deepin-screenshot, deepin-translator, python-tesseract, python-pyocr, deepin-qml-widgets, deepin-menu, chrpath, xware-desktop, bcloud, screenfetch, musicbox...   

**RHEL/CentOS 7 Include(included above list):** pidgin, fcitx, fcitx-configtool, kcm-fcitx, fcitx-ui-light, fcitx-fbterm, fcitx-cloudpinyin, gflags, glog, yaml-cpp, librime, brise, fcitx-libpinyin, sunpinyin, fcitx-sunpinyin, pywebkitgtk, python-keybinder, python-pyquery, python-restkit, python-socketpool, python-http-parser, libmpd-devel, xmms2-devel, Pyrex, ecore-devel, eet-devel, libeina-devel, evas-devel, tslib-devel, libmodplug-devel, libdbusmenu-gtk2-devel, libindicator, libappindicator, python-enum34, python-inotify, zbar-pygtk, python-xpyb, tesseract-langpack, python-cssselect, python-lxml, Cython, pygobject3, python3-cairo, python-urllib3, python-tornado, python-mock, python-nose, python-coverage, python-six, pytest, python-py, python-crypto, python-keyring, dbus-python, rtmpdump, faac, xvidcore, libdc1394, lame, libmp4v2, opencore-amr, vo-amrwbenc...   

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
未完待续...   

***

## Feedback - 反馈
- 任何关于软件包的问题，可以通过如下几种方式反馈：    
    - Email：sensor.wen-AT-gmail.com
    - 贴吧：[CentOS][0-1]、[Fedora][0-2]
    - Github: https://github.com/1dot75cm/myrepo

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
  `# yum install pidgin-lwqq pidgin-sendscreenshot pidgin-openfetion wiz-note sogou-pinyin sogou-pinyin-skins fcitx-cloudpinyin fcitx-googlepinyin fcitx-rime fcitx-libpinyin fcitx-sunpinyin sunpinyin-data openyoudao deepin-music-player dmusic-plugin-baidumusic osdlyrics pointdownload deepin-screenshot`

    注：el6 软件源的软件正在内部测试。

## 1) Install [lwqq][] - 安装 lwqq
- 测试系统：fc20√、el7√
- 执行以下命令安装lwqq：   
  `# yum install pidgin-lwqq pidgin-sendscreenshot`   
lwqq 配置请参考[用户手册][]。其中包括：配置 lwqq 与 GNOME3 集成、pidgin推荐插件等内容。

    参考：[lwqq][1-1]、[pidgin-lwqq][1-2]、[pidgin-sendscreenshot][1-3]、[GNOME3 支持][1-4]、[pidgin推荐插件][1-5]

## 2) Install [fetion][] - 安装飞信
- 测试系统：fc20√、el7√
- 执行以下命令安装飞信：   
  `# yum install pidgin-openfetion`

    参考：[ofetion][2-1]、[libofetion][2-2]、[pidgin-openfetion][2-3]

## 3) Install [WizNote][] - 安装为知笔记
- 测试系统：fc20√、el7√
- 执行以下命令安装为知笔记：   
  `# yum install wiznote`  # 稳定版   
  `# yum install wiznote-beta`  # 开发版

    注1：如果使用 fcitx 无法输入，则需要安装 fcitx-qt5。   

    参考：[WizQTClient][3-1]

## 4) Install [sogou][] - 安装搜狗拼音输入法
- 测试系统：fc20√、el7√
- 执行以下命令安装搜狗拼音：   
  `# yum install sogou-pinyin sogou-pinyin-skins`   

- **Configuration fcitx**
  1. 结束 ibus 守护进程   
 `$ sudo pkill ibus-daemon`
  2. 关闭 gnome-shell 对键盘的监听   
 `$ gsettings set org.gnome.settings-daemon.plugins.keyboard active false`
  3. 切换输入法为 fcitx   
 `$ imsettings-switch fcitx`
  4. 重载 fcitx, 启动搜狗面板   
 `$ fcitx -r; fcitx-configtool`   
 `$ sogou-qimpanel`

    注1：重启系统后，会自动启动搜狗面板。   
    注2：以普通用户执行以上命令。

    参考：[fcitx 维基百科][4-1]、[fcitx项目主页][4-2]、[fcitx Github][4-3]

## 5) Install input method - 安装xx输入法
- 测试系统：fc20√、el7√
- 选择喜欢的输入法，使用 yum 安装，之后使用 fcitx-configtool 等配置工具进行配置即可。  
  `# yum install fcitx-googlepinyin fcitx-cloudpinyin` **\# [谷歌拼音][]输入法**   
  `# yum install fcitx-rime fcitx-cloudpinyin` **\# [中州韵][]输入法**   
  `# yum install fcitx-libpinyin fcitx-cloudpinyin` **\# [libpinyin][]输入法**   
  `# yum install fcitx-sunpinyin sunpinyin-data fcitx-cloudpinyin` **\# [sunpinyin][]输入法**   

    fedora 源已包含 libpinyin 和 sunpinyin，此包提供给 rhel/centos 7 系统使用。   

    参考：[fcitx 包列表][5-1]、[fcitx][5-2]、[fcitx-configtool][5-3]、[kcm-fcitx][5-4]、[fcitx-ui-light][5-5]、[fcitx-fbterm][5-6]、[fcitx-cloudpinyin][5-7]、[libgooglepinyin][5-8]、[fcitx-googlepinyin][5-9]、[gflags][5-10]、[glog][5-11]、[yaml-cpp][5-12]、[librime][5-13]、[brise][5-14]、[fcitx-rime][5-15]、[fcitx-libpinyin][5-16]、[open-gram项目][5-17]、[sunpinyin][5-18]、[fcitx-sunpinyin][5-19]

## 6) Install [openyoudao][] - 安装有道词典
- 测试系统：fc20√、el7√
- Fedora 19/20/21/rawhide 使用以下命令安装：  
  `# yum install openyoudao`   

- RHEL/CentOS 7 使用以下命令安装：   
  `# yum --enablerepo=epel-testing install openyoudao`

    参考：[openyoudao项目][6-1]、[openyoudao Github][6-2]

## 7) Install [Deepin Music Player][] - 安装深度音乐播放器
- 测试系统：fc20√、el7√
- Fedora 19/20/21/rawhide、RHEL/CentOS 7 使用以下命令安装：  
  `# yum install deepin-music-player dmusic-plugin-baidumusic`

    PS：国外有大神将 deepin 桌面环境移植到 Arch 了。我在移植 deepin-media-player 就遇到困难了。它现在已经不维护了，新的 deepin-movie 需要的依赖太多，移植成功再发上来吧。    
    参考：[deepin官网][7-1]、[deepin-music Github][7-2]

## 8) Install [osdlyrics][] - 安装桌面歌词
- 测试系统：fc20√、el7√
- 一款桌面歌词软件，支持常用的音乐播放器，如 Amarok, Audacious, Banshee, Rhythmbox, VLC 等。Fedora / RHEL 7 使用如下命令安装：    
  `# yum install osdlyrics`

    参考：[osdlyrics Github][8-1]

## 9) Install [PointDownload][] - 安装点载
- 测试系统：fc20√、el7√
- 一款方便高效的下载软件，支持 HTTP, BT, Magnet, ed2k, Thunder 等下载协议，支持迅雷离线加速和高速通道功能，支持视频下载功能。Fedora / RHEL 7 使用如下命令安装：    
  `# yum install pointdownload`
 
    注1：安装完成后，如果未成功安装 firefox、chrome 插件，需手动安装。(/usr/share/pointdownload/extensions/)

    参考：[PointDownload Github][9-1]、[Deepin 社区讨论贴][9-2]

## 10) Install [MvGather][] - 安装影视集结号
- 测试系统：fc20√、el7√
- 一款视频点播软件，支持电影点播，电视直播。Fedora / RHEL 7 使用如下命令安装：    
  `# dnf copr enable mosquito/myrepo-testing`   
  `#(el7) yum-config-manager --add-repo=https://copr.fedoraproject.org/coprs/mosquito/myrepo-testing/repo/epel-$(rpm -E %?rhel)/mosquito-myrepo-testing-epel-$(rpm -E %?rhel).repo`   
  `# yum install mvgather`

    注1：如果使用 fcitx 无法输入，则需要安装 fcitx-qt5。     

    参考：[Deepin 社区讨论贴][10-1]、[fcitx-qt5][10-2]、[libqtav][10-3]、[mvgather Github][10-4]

## 11) Install [Deepin Screenshot][] - 安装深度截图
- 测试系统：fc20√、el7√
- 深度截图，支持截图编辑，分享微博。可以自定义快捷键为 ctrl+alt+a，这样就更像 QQ 截图了。Fedora 使用如下命令安装：    
  `# yum install deepin-screenshot`

    参考：[Deepin 社区讨论贴][11-1]

## 12) Install [Deepin Translator][] - 安装深度翻译
- 测试系统：fc20√、el7√
- 深度翻译，支持鼠标取词，词库来自有道、谷歌翻译服务。另外，源中的 GoldenDict 也挺好用的。Fedora 使用如下命令安装：   
  `# dnf copr enable mosquito/myrepo-testing`  # PyQt5 在测试源, 建议卸载低版本的 sip 和 PyQt4   
  `# yum install deepin-translator`

- RHEL/CentOS 7 使用以下命令安装：   
  `# yum-config-manager --add-repo=https://copr.fedoraproject.org/coprs/mosquito/myrepo-testing/repo/epel-$(rpm -E %?rhel)/mosquito-myrepo-testing-epel-$(rpm -E %?rhel).repo`   
  `# yum install --enablerepo=epel-testing deepin-translator`

    参考：[python-pyocr][12-1]、[python-tesseract][12-2]、[deepin-qml-widgets][12-3]、[deepin-menu][12-4]

## 13) Install [Xware Desktop][] - 安装迅雷桌面版
- 测试系统：fc20√、el7√
- Xware Desktop 作为 Xware 的前端，提供与 windows 版迅雷功能相当的体验。Fedora / RHEL 7 使用如下命令安装：   
  `# dnf copr enable mosquito/myrepo-testing`   
  `#(el7) yum-config-manager --add-repo=https://copr.fedoraproject.org/coprs/mosquito/myrepo-testing/repo/epel-$(rpm -E %?rhel)/mosquito-myrepo-testing-epel-$(rpm -E %?rhel).repo`   
  `# yum install xware-desktop`

    参考：[使用说明][13-1]、[发行版支持情况][13-2]

## 14) Install [BCloud][] - 安装百度云
- 测试系统：fc20√、el7√
- BCloud 是百度云的 linux 桌面客户端。采用类似 nautilus 的操作模式，支持上传、下载、播放网盘中的视频等功能。Fedora / RHEL 7 使用以下命令安装：   
  `# yum install bcloud`

    参考：[BCloud Github][14-1]

## 15) Install [screenFetch][] - 安装 screenFetch
- 测试系统：fc20√
- screenFetch 是一款获取系统/主题信息的命令行工具。Fedora / RHEL 使用以下命令安装：   
  `# yum install screenfetch`

    参考：[screenFetch Github][15-1]

## 16) Install [MusicBox][] - 安装网易云音乐
- 测试系统：fc20√
- MusicBox 是一款 Python 编写的网易云音乐 CLI 客户端。Fedora / RHEL 使用以下命令安装：   
  `# yum install musicbox`

    参考：[MusicBox Github][16-1]

***

## Changelog
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
[Deepin Music Player]:http://linuxdeepin.com/img/feature/2014/img_yinyue_1.png "deepin music snapshot"
[7-1]:http://linuxdeepin.com "linuxdeepin"
[7-2]:https://github.com/linuxdeepin/deepin-music "deepin-music Github"
[osdlyrics]:https://code.google.com/p/osd-lyrics/ "GoogleCode"
[8-1]:https://github.com/osdlyrics/osdlyrics "osdlyrics Github"
[PointDownload]:https://github.com/PointTeam/PointDownload "Point Github"
[9-1]:https://github.com/PointTeam/PointDownload "Point Github"
[9-2]:http://www.linuxdeepin.com/forum/23/21124 "Deepin 社区讨论贴"
[MvGather]:http://mvgather.com/ "MvGather 官网"
[10-1]:http://www.linuxdeepin.com/forum/49/23695 "Deepin 社区讨论贴"
[10-2]:https://github.com/wang-bin/QtAV "QtAV Github"
[10-3]:https://github.com/fcitx/fcitx-qt5 "fcitx-qt5 Github"
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
[BCloud]:https://raw.githubusercontent.com/LiuLang/bcloud/master/screenshots/bcloud.png "截屏"
[14-1]:https://github.com/LiuLang/bcloud "BCloud Github"
[screenFetch]:https://github.com/KittyKatt/screenFetch "screenFetch Github"
[15-1]:https://github.com/KittyKatt/screenFetch "screenFetch Github"
[MusicBox]:http://sdut-zrt.qiniudn.com/687474703a2f2f692e696d6775722e636f6d2f4a35333533764b2e676966.gif "截图"
[16-1]:https://github.com/darknessomi/musicbox "musicbox Github"
