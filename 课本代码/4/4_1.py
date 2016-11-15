#coding=utf-8
#一个简单的数据库
people = {
    'alice':{
        'phone':'2341',
        'addr':'foo drive 23'
    },
    'beth':{
        'phone':'9102',
        'addr':'bar street 42'
    },
    'cecil':{
        'phone':'3158',
        'addr':'baz avenue 90'
    }
}
#针对电话号码和地址使用的描述标签，会在打印输出的时候用到
labels = {
    'phone':'phpne number',
    'addr':'address'
}
name = raw_input("name:")
#查找电话号码还是地址
request = raw_input('phobe number (p) or address (a) ?')

#使用正确的键
if request == 'p':key = 'phone'
if request == 'a':key = "addr"
#如果名字是字典中的有效键才打印信息
if name in people: print "%s's %s is %s." % (name,labels[key],people[name][key])