import urllib.request
import urllib.parse
from lxml import etree
import time
import json
item_list = []
def handle_request(url,page):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'
    }
    #将url进行拼接
    url = url%page
    print(url)
    request = urllib.request.Request(url = url,headers = headers)
    return request
def parse_content(content):
    #生成对象
    tree = etree.HTML(content)
    #抓取对象
    div_list = tree.xpath('//ul[@class = "list-box"]/li')
    for odiv in div_list:
        # print(odiv)
        #获取标题
        title = odiv.xpath('.//div[@class = "head"]/h2/text()')
        print(title)
        content1 = odiv.xpath('.//div[@class = "content"]/a/text()')
        print(content1)
        content = odiv.xpath('.//div[@class = "content"]/a/p/text()')
        print(content)
        text = '\n'.join(content)
        # text1 = '\n\u3000\u3000'.join(content1)
        item = {
            '标题':title,
            '内容':content1,
            '补充':content
        }
        #将内容添加到列表中

        item_list.append(item)


def main():
    start_page = int(input('请输入起始页码:'))
    end_page = int(input('请输入结束页码：'))
    url = 'http://www.haoduanzi.com/category/?1-%s.html'
    for page in range(start_page,end_page+1):
        #拼接url
        request = handle_request(url,page)
        #发送请求
        content = urllib.request.urlopen(request).read().decode()
        #解析内容
        parse_content(content)
        #写入到文件
    # string = json.dumps(item_list,ensure_ascii=False)
    with open('duanzi.txt','w',encoding = 'utf-8') as fp:
        fp.write(str(item_list))

if __name__ == '__main__':
    main()