
#_*_ coding:utf-8 _*_



class MyException(Exception):
    #打印错误信息，结合raise使用
    def __init__(self,message):
        Exception.__init__(self)
        self.message=message