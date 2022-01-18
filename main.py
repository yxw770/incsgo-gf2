# pip3 install beautifulsoup4
# pip3 install requests
# pip3 install lxml
import requests
import re
from bs4 import BeautifulSoup
import threading


def readUser(num):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
            'cookie': 'JSESSIONID=2BD0C2A344175664A98F14362FACEC0C; _gat=1',
            'sec-ch-ua':'" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
            'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        }
        r = requests.get('https://www.incsgo.gg/user/562311', headers=headers);
        print("Read user No." + str(num));
        soup = BeautifulSoup(r.text, 'lxml');  # lxml为解析器
        # 通过标题获取邮箱
        print(soup.text)
        title = soup('title')[0].string;

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
    except:
        readUser(num);


def main():
    num = int(input("起始账号："))
    while num < 562312:
        readUser(num);
        num += 1;
    print("Project is finish!")


if __name__ == '__main__':
    main();
