# pip3 install beautifulsoup4
# pip3 install requests
# pip3 install lxml
import requests
import re
from bs4 import BeautifulSoup
import threading

proxy = {
    "120.196.112.6:3128"
};
proxyid = -1

def pppoe():

    print(proxyid)


def readUser(num):

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
            'Cache-Control': 'no-cache',
            # 'Host':'https://www.incsgo.gg',
            'Accept': '*/*',
        }
        if proxyid == -1:
            # 本地
            r = requests.get('https://www.incsgo.gg/user/' + str(num), headers=headers);
        else:
            # 启动代理
            r = requests.get('https://www.incsgo.gg/user/' + str(num), headers=headers);
            #r = requests.get('https://www.incsgo.gg/user/' + str(num), headers=headers, proxy=proxy[proxyid]);

        print("Read user No." + str(num));
        soup = BeautifulSoup(r.text, 'lxml');  # lxml为解析器
        # 通过标题获取邮箱
        print(soup.text);
        if r.status_code != 200 or len(soup('title')) == 0:
            # 需要重新拨号
            pppoe();

        title = soup('title')[0].string;
        if title.find('incsgo.gg 能取回的CSGO开箱网') != -1:
            # 需要重新拨号
            pppoe();

        if soup.text.find('incsgo.gg 能取回的CSGO开箱网') != -1 or soup.text == '':
            # 需要重新拨号
            pppoe();
        pattern = re.compile('incsgo user - (\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*)$');
        # 正则获取检测邮箱地址
        matchObj = pattern.match(title);
        if matchObj:
            email = matchObj.group(1);
            if email:
                file_handle = open('incsgo-email.txt', mode='a')
                file_handle.write(email + '----' + str(num) + '\n');
                file_handle.close()
                print("Find email is: " + email);
            else:
                print("No match!");
        else:
            print("No match!!");




# res = os.system('ping 8.8.8.8')
# 没有网络的时候res为True
# if res:
#   os.system('@Rasdial 宽带连接 /DISCONNECT')  # 先断开宽带连接（这个宽带连接是你的网络名字，可以叫做别的）
# 然后重新拨号
#  os.system('@Rasdial 宽带连接 账号 密码')
# 有网络 什么都不做
# else:
#   pass
# 每隔 5分钟进行一次检测
# time.sleep(5 * 60)


def main():
    num = int(input("起始账号："))
    while num < 562312:
        readUser(num);
        num += 1;
    print("Project is finish!")


if __name__ == '__main__':
    main();
