#coding=utf-8
#演示了一个代码清单4_1的修改版，它使用get方法访问“数据库”实体
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
key = request #如果请求既不是p也不是a
if request == 'p':key = 'phone'
if request == 'a':key = "addr"
#使用get()方法提供默认值
person = people.get(name,{})
label = labels.get(key,key)
result = person.get(key,'not available')
print "%s's %s is %s." % (name,label,result)