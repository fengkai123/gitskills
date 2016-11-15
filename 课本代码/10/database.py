#coding=utf-8
#简单的shelve模块的数据库应用程序
import sys,shelve

def store_person(db):
    pid = raw_input('enter unique ID number:')
    person = {}
    person['name'] = raw_input('enter name:')
    person['age'] = raw_input('enter age:')
    person['phone'] = raw_input('enter phone:')

    db[pid] = person
def lookup_person(db):
    pid = raw_input('enter ID number:')
    field = raw_input("what would you like to know? (age,name,phone OR all)")
    field = field.strip().lower()
    if field == 'all':
        print 'ID:',pid + ' ' + '姓名:',db[pid]['name'] + ' ' + '年龄：',db[pid]['age'] + ' ' + '电话：',db[pid]['phone']
    else:
        print field.capitalize() + ':',db[pid][field]
def print_help():
    print 'the available commands are:'
    print 'store : store information about a person'
    print 'lookup: looks up a person from ID number'
    print 'quit  : save change and exit'
    print ' ?    : print this message'
def enter_commands():
    cmd = raw_input('enter command (? for help):')
    cmd = cmd.strip().lower()
    return cmd
def main():
    database = shelve.open('C:\\database.dat')
    try:
        while True:
            cmd = enter_commands()
            if cmd == 'store':
                store_person(database)
            elif cmd == 'lookup':
                lookup_person(database)
            elif cmd == "?":
                print_help()
            elif cmd == 'quit':
                return
    finally:
        database.close()

if __name__=='__main__': main()