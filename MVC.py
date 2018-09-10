import json


class Person(object):
    def __init__(self, first_name=None, last_name=None):
        self.first_name = first_name
        self.last_name = last_name

    # returns Person name, ex: John Doe
    def name(self):
        return ("%s %s" % (self.first_name, self.last_name))

    @classmethod
    # returns all people inside db.txt as list of Person objects
    def getAll(self):
        database = open('db.txt', 'r')
        result = []
        json_list = json.loads(database.read())
        for item in json_list:
            item = json.loads(item)
            person = Person(item['first_name'], item['last_name'])
            result.append(person)
        return result

  #
    from model import Person
    def showAllView(list):
        print 'In our db we have %i users. Here they are:' % len(list)
        for item in list:
            print item.name()

    def startView():
        print 'MVC - the simplest example'
        print 'Do you want to see everyone in my db?[y/n]'

    def endView():
        print 'Goodbye!'

     #
        from model import Person
        import view

        def showAll():
            # gets list of all Person objects
            people_in_db = Person.getAll()
            # calls view
            return view.showAllView(people_in_db)

        def start():
            view.startView()
            input = raw_input()
            if input == 'y':
                return showAll()
            else:
                return view.endView()

        if __name__ == "__main__":
            # running controller function
            start()