# pip3 install beautifulsoup4
# pip3 install requests
# pip3 install lxml
import requests
import re
from bs4 import BeautifulSoup


def main():
    r = requests.get('https://www.incsgo.gg/user/562311');
    soup = BeautifulSoup(r.text, 'lxml');  # lxml为解析器
    # 通过标题获取邮箱
    title = soup('title')[0].string;
    pattern = re.compile('incsgo user - (\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*)$');
    # 正则获取检测邮箱地址
    matchObj = pattern.match(title);
    if matchObj:
        email = matchObj.group(1);
        if email:
            print("Find email is: " + email);
        else:
            print("No match!");
    else:
        print("No match!!");


if __name__ == '__main__':
    main();
