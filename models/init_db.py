
#_*_ coding:utf-8 _*_

from models import oracle_get
#判断是否需要初始化
x = []
try:
    #x = (oracle_get.session.query (oracle_get.Users).first ())
    pass
except Exception as e:
    print('ERROR-00001 db connect failed!')
finally:

    if x == [] or x == None:
        oracle_get.init_create_table()
        #miaoshu = '管理员'.encode('utf-8')


        user_obj = oracle_get.Users (id = 1,username='admin', describtion='miaoshu', password='123123')
        user_obj1 = oracle_get.Users (id = 2,username='test', describtion='miaoshu', password='123123')

        group_obj = oracle_get.Groups (id=1,groupname = 'default')
        group_obj1 = oracle_get.Groups (id=2,groupname = 'IT')

        Host_obj = oracle_get.Hosts(ipaddr='127.0.0.1',port='1521',login_username='root',login_password='root',is_online='online',add_time='2018-01-11',describtion='localhost')
        Host_obj1 = oracle_get.Hosts(ipaddr='127.0.0.2',port='1521',login_username='root',login_password='root',is_online='online',add_time='2018-01-11',describtion='localhost')
        Host_obj2 = oracle_get.Hosts(ipaddr='127.0.0.3',port='1521',login_username='root',login_password='root',is_online='online',add_time='2018-01-11',describtion='localhost')
        group_obj1.host = [Host_obj]
        group_obj.host = [Host_obj1,Host_obj2]

        user_obj.group = [group_obj]
        user_obj1.group = [group_obj1]
        oracle_get.session.add (user_obj)
        oracle_get.session.add (user_obj1)
        try:
            oracle_get.session.commit ()  # 提交
        except Exception as e:
            print (e)





    else:
        print(x,'dfasdfasdfsa')
