from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba
import numpy as np
filename = "/Users/zlinzhang/Desktop/笔记.txt"
with open(filename) as f:
    my_text = f.read()
mytext = "  ".join(jieba.cut(my_text))
#print(mytext)
wordcloud = WordCloud(font_path="Arial.ttf").generate(mytext)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()


from wordcloud import WordCloud
import PIL.Image as image
import numpy as np
import jieba


# 分词
def trans_CN(text):
    # 接收分词的字符串
    word_list = jieba.cut(text)
    # 分词后在单独个体之间加上空格
    result = " ".join(word_list)
    return result


with open("/Users/zlinzhang/Desktop/笔记.txt") as fp:
    text = fp.read()
    # print(text)
    # 将读取的中文文档进行分词
    text = trans_CN(text)
    mask = np.array(image.open("/Users/zlinzhang/Downloads/xin.png"))
    wordcloud = WordCloud(
#       # 添加遮罩层
        mask=mask,
        # 生成中文字的字体,必须要加,不然看不到中文
        font_path="PingFang.ttc"
    ).generate(text)
    image_produce = wordcloud.to_image()
    image_produce.show()
    print(type(image_produce))

