from addressbook_pb2 import Person


if __name__ == '__main__':
    person = Person()
    person.id = 1234
    person.name = "John Doe"
    person.email = "jdoe@example.com"
    phone = person.phones.add()
    phone.number = "555-4321"
    phone.type = Person.HOME
    # person.no_such_field = 1  # raises AttributeError
    # person.id = "1234"  # raises TypeError
    # pass
    print(person)
