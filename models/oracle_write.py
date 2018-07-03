#_*_ coding:utf-8 _*_
from models import oracle_get

# a = oracle_get.session.query (oracle_get.Hosts).filter(oracle_get.Hosts.id == 1)
# print(a)


def update_table_Hosts(id,data_dict):
    #更新数据库的host表
    if data_dict:
        oracle_get.session.query(oracle_get.Hosts).filter (oracle_get.Hosts.id==id).update ({'ipaddr':data_dict.get('ipaddr'),
                                                            'port' : data_dict.get('port'),
                                                            'group':  data_dict.get('group'),
                                                            'is_online' :data_dict.get('is_online'),
                                                            'describtion' :data_dict.get('describtion')
                                                            })
    try:
        oracle_get.session.commit ()  # 提交
    except Exception as e:
        print ('更新数据失败update_table_Hosts：'+e)


def add_table_Hosts(data_dict):
    #插入一条记录
    add_list = oracle_get.Hosts(ipaddr=data_dict.get('ipaddr'),
                                port=data_dict.get('port'),
                                group=data_dict.get('group'),
                                is_online=data_dict.get('is_online'),
                                describtion=data_dict.get('describtion'),
                                add_time=data_dict.get('add_time'))
    oracle_get.session.add(add_list)
    try:
        oracle_get.session.commit()  # 提交
    except Exception as e:
        print('插入记录失败：add_table_Hosts错误'+e )


data_dict = {'ipaddr': '1',
             'port': '2',
             'group': 'IT',
             'is_online': '4',
             'describtion': '5',
             'add_time' :'6'
             }
#add_table_Hosts(data_dict)
def del_table_Hosts(by_id):
    if by_id:
        try:
            rs = oracle_get.session.query( oracle_get.Hosts ).filter( oracle_get.Hosts.id == int(by_id )).first()
            #rs = oracle_get.Hosts(id=by_id)
            oracle_get.session.delete(rs)
            oracle_get.session.flush()
            oracle_get.session.commit ()

        except Exception as e:
            print ( '删除记录失败：del_table_Hosts错误' + e )

