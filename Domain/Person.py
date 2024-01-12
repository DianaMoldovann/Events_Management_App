class Person:
    """
        persons is an abstract data type
        Domain: {{person_id, name, address}
    """

    def __init__(self, id_person, name, address):
        """
        create a new person with id_person, name, address
        :param id_person - the unique id of the person int
        :param name - string consisting of Name and Surname
        :param address - string consisting of street name, number, city
        :lista_evenimente - list, the list of events in which the person participates
        """
        self.__id_person = id_person
        self.__name = name
        self.__address = address

    def __eq__(self, other):
        """
        check if two objects have the same id
        :param other:
        :return: True - if they have the same id
                 False - if they have different id
        """
        return self.__id_person == other.__id_person

    def __str__(self):
        """
        returns the object as a string
        :return:
        """
        return f"{self.__id_person}, {self.__name}, {self.__address}"

    def get_id_person(self):
        """
           Getter method
            returns the id of a person
        """
        return self.__id_person

    def get_name(self):
        """"
            Getter method
            returns a person's name
        """
        return self.__name

    def get_address(self):
        """"
            Getter method
            returns a person's name
        """
        return self.__address

    def set_name(self, value):
        """
        modify the name value with the value string
        :param value: the new name
        :return:
        """
        self.__name = value

    def set_address(self, value):
        """
        change the value of address with the address in value
        :param value: the new address
        :return:
        """
        self.__address = value

