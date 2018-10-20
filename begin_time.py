import time
class Ctimer:
    '''
    创建实例后即开始计时，total函数即可截止计时并返回时间长度
    如果需要多个计时，可以创建多个实例，也可以用addTimer函数增加计时对，或者在创建实例时就设置计时对数
    '''
    def __init__(self,timeStart=time.time(),timeStop=0,timerNum=1):
        self.time_start=range(timerNum) ;self.time_start[0]=timeStart
        self.time_stop=range(timerNum) ;self.time_stop[0]=timeStop
        self.time_num=timerNum

    def addTimer(self,addnum=1):
        #扩展原start和stop数组
        extenders=range(len(self.time_start),len(self.time_start)+addnum)
        self.time_start.extend(extenders)
        self.time_stop.extend(extenders)
        self.time_num+=addnum
        #初始化新增的time_start和time_stop数组，前者在增加计时器时默认开始计时，后者初始化为0，返回增加的计时器开始计时的时间
        for num in extenders:
            self.time_start[num]=time.time()
        for num in extenders:
            self.time_stop[num]=0
        return [self.time_start[order] for order in extenders]

    def start(self,order=0):
        self.time_start[order]=time.time()
        return time.time()

    def stop(self,order=0):
        self.time_stop[order]=time.time()
        return time.time()

    def total(self,order=-1,out=True):
        #如果order是‘all’的话，终止并输出、返回所有计时
        #如果out为真，则打印出结果，并返回结果；如果out为假，则只返回，不输出
        total=[0]*self.time_num
        if order==-1:
            for i in range(self.time_num):
                if self.time_stop[i]==0:
                    self.time_stop[i] = time.time()
                total[i]=self.time_stop[i]-self.time_start[i]
            if out ==True:
                print(total)
            return total

        else:
            if self.time_stop[order] == 0:
                self.time_stop[order] = time.time()
            total[order]=self.time_stop[order]=self.time_start[order]
            if out == True:
                print(total[order])
            return total[order]
