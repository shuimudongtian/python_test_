import random
def gen_code(length=10):
    """
    将0~9,a~z,A~Z保存到list中，用random.sample从list中取固定位数
    """
    code_list = []
    for i in range(10):
        code_list.append(str(i))
    # print i
    for i in range(65, 91):
        code_list.append(chr(i))
    # print chr(i)
    for i in range(97, 123):
        code_list.append(chr(i))

    myslice = random.sample(code_list, length)
    veri_code = ''.join(myslice)
    return veri_code
a=gen_code()
count=0
for i in range(201):
    count+=1
    print(a,end='   ')
    if count %3==0:
        print(end='\n')
    a=gen_code()

'''
1、range生成随机数

2、int类型转换成char类型用chr() 函数

3、从list中随机取数，用random.sample()
'''