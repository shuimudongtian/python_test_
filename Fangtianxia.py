import requests
from lxml import etree
import re
def fangtx():
    print('数据爬取中,请等待...')
    start_url = 'http://xian.newhouse.fang.com/house/s/b9{}'
    with open('/Users/zlinzhang/Downloads/ftx.csv', 'a') as f:
        f.write('小区，大小，区域，详细信息，价格，电话'+'\n')
        for i in range(36):
            url=start_url.format(i+1)
            headers = {
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"

            }
            res = requests.get(url, headers=headers)
            ret = res.content.decode('gbk')
            result = etree.HTML(ret)
            content_list = result.xpath(".//div[@id='newhouse_loupai_list']/ul/li")
            if content_list:
                for content in content_list:
                    if content_list.index(content)==5:
                        continue
                    title=content.xpath(".//div[@class='nlcd_name']/ a / text()")
                    title = title[0].strip() if len(title) > 0 else ''
                    #print(title)

                    area = content.xpath(".//span[@class='sngrey']/text()")
                    area = area[0].strip() if len(area) > 0 else ''
                    #print(area)

                    address = content.xpath(".//span[@class='snarey']/../text()")
                    address = address[1].strip() if len(address) > 0 else ''
                   # print(address)

                    size = content.xpath(".//div[contains(@class,'house_type')]/text()[last()]")
                    size = re.sub(r"\t|\n|", '', size[0]) if len(size) > 0 else ''
                   # print(size)

                    price1 = content.xpath(".//div[@class='nhouse_price']/span/text()")
                    price3 = content.xpath(".//div[@class='kanzx']/h3/a/text()")
                    price2 = content.xpath(".//div[@class='nhouse_price']/em/text()")
                 #   price = html.xpath('//*[@class="nhouse_price"]//span|//*[@class="kanesf"]//p//a|//*[@class="kanzx"]//h3//a')

                    if price3:
                        price = '优惠楼盘'
                    if price1:
                        if price1[0]=='价格待定':
                            price='价格待定'
                        else:
                            price = price1[0]+price2[0]

                    #print(price1)

                    phone=content.xpath(".//div[@class='tel']/p//text()")
                    phone=''.join(phone)

                    f.write(title+','+size+','+area+','+address+'+'+price+','+phone+','+'\n')

if __name__ == '__main__':
    fangtx()
    print('爬取完毕')
