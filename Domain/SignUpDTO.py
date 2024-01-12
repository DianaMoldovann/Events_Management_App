class SignUpDTO:
    def __init__(self, id_signUp, id_person, id_event):
        self.__id_signUp = id_signUp
        self.__id_person = id_person
        self.__id_event = id_event

    def get_id_signUp(self):
        return self.__id_signUp

    def get_id_person(self):
        return self.__id_person

    def get_id_event(self):
        return self.__id_event

class PersonSituation(object):
    """
    Data Transfer Class
    """

    def __init__(self, person, listOfEvents):
        """
        Data Transfer Object
        :param person: Person
        :param list_events: list of event ids
        """
        self.__person = person
        self.__listOfEvents = listOfEvents
        self.__numberOfEvents = len(self.__listOfEvents)

    def __str__(self):
        return f"PERSON: {self.get_person()} IDs OF EVENTS:{self.get_listOfEvents()} " \
               f"NUMBER OF EVENTS: {self.get_numberOfEvents()}"

    def get_person(self):
        """
       Retune the person
        :return:
        """
        return self.__person

    def get_listOfEvents(self):
        """
        Restore the list of events
        :return:
        """
        return self.__listOfEvents

    def get_numberOfEvents(self):
        """
       Returns the number of events in which a person participates
        :return:
        """
        return self.__numberOfEvents


class EventSituation(object):
    """
    Data Transfer Class
    """

    def __init__(self, event, listOfPeople):
        """
        Data Transfer Object
        :param event: Eveniment
        :param listOfPeople: the list of people's ids
        """
        self.__event = event
        self.__listOfPeople = listOfPeople
        self.__numberOfPeople = len(self.__listOfPeople)

    def __str__(self):
        return f"EVENT: {self.get_event()}, PEOPLE ID's::{self.get_listOfPeople()}" \
               f", NUMBER OF PEOPLE: {self.get_numberOfPeeople()}"

    def get_event(self):
        """
       Repeat the event
        :return:
        """
        return self.__event

    def get_listOfPeople(self):
        """
        Retuneaza list of people
        :return:
        """
        return self.__listOfPeople

    def get_numberOfPeeople(self):
        """
        Returns the number of people participating in an event
        :return:
        """
        return self.__numberOfPeople
