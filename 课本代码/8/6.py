#coding:utf-8
person = {
    'name':'tom',
    'age':34,
    'occupation':'camper'
}
def describePerson(person):
    print "description of",person['name']
    print 'age:',person['age']
    if 'occupation' in person:
        """
        print 'occupation:',person['occupation']
        """
    try:
        print 'occputation:' + person['occupation']
    except:
        pass

describePerson(person)