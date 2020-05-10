配置新网站
========

## 需要安装的包：

* nginx
* Python 3
* Git
* pip
* virtualenv

以Ubuntu为例，可以执行下面的命令安装：

    sudo apt-get install nginx git python3 python3-pip
    sudo pip3 install virtualenv

## 配置nginx虚拟主机

* 参考nginx.template.conf
* 可以把ip替换成所需要的域名

## Upstart任务

* 参考gunicore-upstart.template.conf
* 可以把ip替换成所需要的域名

## 文件夹结构:

假设有用户账号，家目录为/home/username

