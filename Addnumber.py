from imp import reload

from PIL import Image, ImageFont, ImageDraw  # 从PIL库导入所需模块
import sys

reload(sys)  # 必须要reload
#sys.setdefaultencoding('utf-8')  # 字符编码改为utf8

headPath = r"/Users/zlinzhang/Downloads/"
# 头像图片路径
outputPath = r"/Users/zlinzhang/Downloads/"
# 处理后输出路径
fontPath = r"/System/Library/Fonts"
# 字体路径
headFile = "head.jpg"  # 头像文件
outFile = "output.jpg"  # 输出文件
# 打开图片，建立画布
image = Image.open(headPath + headFile, 'r')
draw = ImageDraw.Draw(image)

# 由图片大小确定字体大小
fontsize = min(image.size) / 4

# 增加文字
fontobj = ImageFont.truetype(font=fontPath + "AdobeHeitiStd-Regular.otf", size=fontsize, index=0, encoding='',
                             filename=None)  # 实例字体对象
draw.text((image.size[0] - fontsize, 0), text="5", fill=(255, 0, 0), font=fontobj,
          anchor=None)  # 用draw对象的text()方法添加文字
image.save(outputPath + outFile)  #