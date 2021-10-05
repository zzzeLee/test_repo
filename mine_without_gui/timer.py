import time as t

""" 计时器实现，参考自CSDN @__N4c1__"""
""" 文章链接https://blog.csdn.net/qq_43504939/article/details/91480610?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522163171926416780274185992%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fall.%2522%257D&request_id=163171926416780274185992&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_ecpm_v1~rank_v31_ecpm-1-91480610.pc_search_result_cache&utm_term=python%E8%AE%A1%E6%97%B6%E5%99%A8&spm=1018.2226.3001.4187 """


class MyTimer():
    def __init__(self):
        self.time_spend = 0
        self.lasted = []
        self.begin = 0
        self.end = 0
        self.paused = 0

    # 开始计时

    def start(self):
        if not self.begin:
            self.begin = t.localtime()
            # 上面是time库中的一个方法
            print("计时开始-----")

    # 停止计时
    def stop(self):
        if not self.begin:
            print("提示，请先用start()进行计时")
        # 这里因为前面是0，没有的话就gg了
        self.end = t.localtime()
        self._calc()
        print("计时结束了!!!")

    # 因游戏需要新增暂停函数

    def pause(self):
        if not self.begin:
            print('game has not started!!')
            return False
        self.paused = t.localtime()
        for index in range(6):
            self.lasted.append(self.paused[index]-self.begin[index])
        return True

    # 因游戏需要新增继续函数

    def conti(self):
        self.contin = t.localtime()

    # 内部方法，计算运算时间的

    def _calc(self):
        self.time_spend = 0
        if not self.paused:
            for index in range(6):
                self.lasted.append(self.end[index]-self.begin[index])
        else:
            for index in range(6):
                self.lasted[index] += (self.end[index]-self.contin[index])

        self.time_spend = (self.lasted[3] * 60 +
                           self.lasted[4]) * 60 + self.lasted[5]
        # 这里是为了将多余的那些0去掉

    # 为下一轮计时初始化变量
        self.begin = 0
        self.end = 0

    def get_time(self):
        return self.time_spend
