#_*_ coding:utf-8 _*_
from models import oracle_get

def get_user_field(username):
    #查询用户名字段users
    my_user = oracle_get.session.query(oracle_get.Users).filter( oracle_get.Users.username == username,
                                                                       ).first()
    return (my_user)


def get_hosts_field(hostname=None):
    #查询主机字段,验证是否重复用户名
    if hostname:
        host_list = oracle_get.session.query(oracle_get.Hosts).filter( oracle_get.Hosts.ipaddr == hostname,
                                                                       ).first()
    else:
        pass
    return(host_list)


def get_user_hosts(username):
    #通过用户名查询出对应用户组的主机信息
    #1.查询出用户对应的组
    #2.用组来反查主机信息
    user2groupname = oracle_get.session.query ( oracle_get.Users ).filter ( oracle_get.Users.username == username,
                                                                       ).first ()
    if user2groupname:
        groupname =   (user2groupname.group[0].groupname)

        host_list = oracle_get.session.query(oracle_get.Hosts).filter( oracle_get.Hosts.group == groupname,
                                                                           ).all()
        return host_list
    else:
        return None

def get_all_groups():
    #查询所有的组，用来显示select option的组下拉列表
    groups = oracle_get.session.query (oracle_get.Groups).all ()
    return (groups)
#
# a = get_hosts_field()
# for i in a :
#     print(i)

