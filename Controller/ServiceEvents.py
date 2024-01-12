from Domain.Event import Event
import datetime


class ServiceEvents:
    """
    GRASP Controller
    Responsible for performing the operations requested by the user
    Coordinates the necessary operations to carry out the action triggered by the user
    (i.e. trigger action: user -> ui-> service type object in ui -> service -> service coordinates the operations
    using other objects (e.g. repo, validator) to actually perform the operation
    """

    def __init__(self, __repository_events, __validator_event):
        """
        Initialize service
        :param __repository_events: repo type object that helps us manage the crowd
        :param __validator_event: validator for verifying people
        """
        self.__repoEvents = __repository_events
        self.__validatorEvent = __validator_event

    def size_service(self):
        """
        Returns the length of the list of people
        :return:
        """
        return self.__repoEvents.size()

    def addEvent(self, id_event, date, time, description):
        """
        Validate the input and add the Events if that's valid
        :param id_event:
        :param date:
        :param time:
        :param description:
        :return:
        """
        event = Event(id_event, date, time, description)
        self.__validatorEvent.validate(event)
        parts_date = date.split("/")
        date = datetime.date(int(parts_date[2]), int(parts_date[1]), int(parts_date[0]))
        event = Event(id_event, date, time, description)
        self.__repoEvents.addEvent(event)

    def findEvent(self, id_event):
        """
        Search for the event with the same id
        :param id_event:
        :return:
        """
        self.__validatorEvent.validate_id(id_event)
        return self.__repoEvents.findEvent(id_event)

    def modifyEvent(self, id_event, date, time, description):
        """
        Validate the input and modify the event with the same id
        :param id_event:
        :param date:
        :param time:
        :param description:
        :return:
        """
        event = Event(id_event, date, time, description)
        self.__validatorEvent.validate(event)
        parts_date = date.split("/")
        date = datetime.date(int(parts_date[2]), int(parts_date[1]), int(parts_date[0]))
        event = Event(id_event, date, time, description)
        self.__repoEvents.modifyEvent(event)

    def getAllEvents(self):
        """
        Return a list with all events
        :return:
        """
        return self.__repoEvents.getAllEvents()
