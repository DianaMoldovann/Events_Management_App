class Event:
    """
        Event is an abstract date type
        Domain: {{id, date, time, description}, where
        id - int (unique code for each event)
        date - string
        time - int
        description - string}
    """
    def __init__(self, id_event, date, time, description):
        """
            creates an object of the class (an event) that has the fields: id_event, date, time, description
        """
        self.__id_event = id_event
        self.__date = date
        self.__time = time
        self.__description = description

    def __eq__(self, __o):
        """
        check if two objects have the same id
        :param __o:
        :return: True - if they have the same id
                 False - if they have different id
        """
        return self.__id_event == __o.__id_event

    def __str__(self):
        """
        returns the object as a string
        :return:
        """
        return f"{self.__id_event}, {self.__date}, {self.__time}, {self.__description}"

    def get_id_event(self):
        """
            Getter method
            returns the id of an event
        """
        return self.__id_event

    def get_date(self):
        """"
            Getter method
            returns the date of an event as a string
        """
        return self.__date

    def get_time(self):
        """
            Getter method
            returns the time/duration of an event
        """
        return self.__time

    def get_description(self):
        """
            Getter method
            returns the description of an event
        """
        return self.__description

    def set_date(self, value):
        """
        modify the name value with the value string
        :param value: the new date
        :return:
        """
        self.__date = value

    def set_time(self, value):
        """
        change the value of address with the address in value
        :param value: the new time
        :return:
        """
        self.__time = value

    def set_description(self, value):
        """
        replace the list of events with the new list
        :param value: the new description
        :return:
        """
        self.__description = value
