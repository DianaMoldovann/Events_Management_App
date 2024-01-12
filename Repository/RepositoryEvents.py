from Errors.Exeptions import RepositoryError


class RepositoryEvents:
    """
        The class created with the responsibility of handling many events
    """

    def __init__(self):
        """
        Events is a dictionary whose elements are entities of type Events
        """
        self._events = {}

    def size(self):
        """
        returns the length of the event dictionary
        :return:
        """
        return len(self._events)

    def addEvent(self, event):
        """
        Add an event to the dictionary
        :param event: event to be added
        :type event: Event
        ; the list of events is changed by adding the event
        :return:
        """
        if event.get_id_event() in self._events:
            raise RepositoryError("There is already a event with the same id!")
        self._events[event.get_id_event()] = event

    def findEvent(self, id_event):
        """
        search in events, an event with the same id
        :return: True - if it finds an event with the same id
                 False - if it does not find an event with the same id
        """
        if id_event not in self._events:
            raise RepositoryError("Event not found!\n")
        return self._events[id_event]

    def modifyEvent(self, event):
        """
        update the event with the same id
        :param event: Event
        :return:
        """
        if event.get_id_event() not in self._events:
            raise RepositoryError("Event not found!\n")
        self._events[event.get_id_event()] = event

    def getAllEvents(self):
        """
        Returns a list of all existing events
        :rtype: list of Event type objects
        :return:
        """
        r = []
        for id_event in self._events:
            eveniment = self._events[id_event]
            r.append(eveniment)
        return r

    def deleteEvent(self, id_event):
        if id_event not in self._events:
            raise RepositoryError("Event not found!\n")
        del self._events[id_event]
