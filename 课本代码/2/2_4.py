#coding=utf-8
database = [['albert','1234'],['dilbert','4242'],['smith'],['7524'],['jones'],['9843']]
username = raw_input('User name:')
pin = raw_input('Pin code:')
if [username,pin] in database:
    print "Access granted"
else:
    print "请注册！"
    new_username = raw_input("name:")
    new_pin =raw_input("pin:")
    new_database = database + [[new_username,new_pin]]
    print new_database