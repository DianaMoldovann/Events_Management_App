class SignUp:
    """
    The class responsible for the connection between people and events
    """
    def __init__(self, signUp_id, person, events):
        """
        create an entry with parameters:
        :param signUp_id: int, unique_id for the registration
        :param person: Person, the person assigned to an event
        :param events: Event, the event to which a person is assigned
        """
        self.__signUp_id = signUp_id
        self.__events = events
        self.__person = person

    def __eq__(self, other):
        """
        check if two registrations are equal by id
        :param other:
        :return:
        """
        return self.get_id_signUp() == other.get_id_signUp()

    def __str__(self):
        """
        returns the class object as a string
        :return:
        """
        return f"{self.get_id_signUp()}, {self.get_person()}, {self.get_event()}"

    def get_id_signUp(self):
        """
        returns the registration id
        :return:
        """
        return self.__signUp_id

    def get_person(self):
        """
        returns the id of the person
        :return:
        """
        return self.__person

    def get_event(self):
        """
        returns the event id
        :return:
        """
        return self.__events