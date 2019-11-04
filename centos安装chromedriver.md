# **centos**安装chromedriver

### (1) 添加chrome的repo源

```shell
vi /etc/yum.repos.d/google.repo

[google]
name=Googlex86_64baseurl=http://dl.google.com/linux/rpm/stable/x86_64
enabled=1
gpgcheck=0
gpgkey=https://dl-ssl.google.com/linux/linux_signing_key.pub
```

### (2)安装

```shell
yum update 

yum install google-chrome-stable
```

### (3)安装 chromerriver

将下载的文件解压，放在如下位置

> /usr/bin/chromedriver

给予执行权限

> chmod +x /usr/bin/chromedriver

### (4)安装 XVFB

```shell
yum install Xvfb -y
yum install xorg-x11-fonts* -y
```

新建在/usr/bin/ 一个名叫 xvfb-chrom 的文件写入以下内容：

```shell
vi /usr/bin/xvfb-chrome
```

> #!/bin/bash
> _kill_procs() {
> kill -TERM $chrome
> wait $chrome
> kill -TERM $xvfb
> }
>
> #Setup a trap to catch SIGTERM and relay it to child processes
>
> trap _kill_procs SIGTERM
> XVFB_WHD=${XVFB_WHD:-1280x720x16}
>
> #Start Xvfb
>
> Xvfb :99 -ac -screen 0 $XVFB_WHD -nolisten tcp &
> xvfb=$!
> export DISPLAY=:99
> chrome --no-sandbox --disable-gpu$@ &
> chrome=$!
> wait $chrome
> wait $xvfb

**添加执行权限**

> chmod +x /usr/bin/xvfb-chrome

**查看当前映射关系**

> ll /usr/bin/ | grep chrom

**更改Chrome启动的软连接**

```shell
ln -s /etc/alternatives/google-chrome /usr/bin/chrome
rm -rf /usr/bin/google-chrome
ln -s /usr/bin/xvfb-chrome /usr/bin/google-chrome
```

**查看修改后的映射关系**

> ll /usr/bin/ | grep chrom



### (5)调试

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')  # 使用无头谷歌浏览器模式
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(chrome_options=chrome_options,executable_path='/usr/bin/chromedriver')

driver.get('http://c.biancheng.net/view/2745.html')
html = driver.page_source
print(html)

```

