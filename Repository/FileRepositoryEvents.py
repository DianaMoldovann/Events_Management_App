from Domain.Event import Event
from Repository.RepositoryEvents import RepositoryEvents
import datetime


class FileRepositoryEvents(RepositoryEvents):
    def __init__(self, path):
        """
        The class creates with the responsibility of handling events and storing them in a file
        :param path: the path to the text file where we store the Events
        """
        RepositoryEvents.__init__(self)
        self.__path = path

    def __read_all_from_file(self):
        """
       Reads one event from each line from the file and adds them to the RepsoitoryEvenimente dictionary
       :return:
       """
        with open(self.__path, "r") as f:
            lines = f.readlines()
            self._events.clear()
            for line in lines:
                line = line.strip()
                if line != '':
                    parts = line.split(', ')
                    id_event = int(parts[0])
                    data = parts[1]
                    parts_data = data.split("-")
                    date = datetime.date(int(parts_data[0]), int(parts_data[1]), int(parts_data[2]))
                    time = parts[2]
                    description = parts[3]
                    event = Event(id_event, date, time, description)
                    self._events[id_event] = event

    def __write_all_to_file(self):
        """
        Write one event from the event dictionary on each line in the file
        :return:
        """
        with open(self.__path, 'w') as f:
            for event in self._events.values():
                f.write(str(event) + "\n")

    def addEvent(self, event):
        """
        Add an event to the dictionary, but also to the file
        :param event: event to be added
        :type event: Event
        ; the list of events is modified by adding the given event
        ; the text file is modified by adding the given event
        :return:
        """
        self.__read_all_from_file()
        RepositoryEvents.addEvent(self, event)
        self.__write_all_to_file()

    def findEvent(self, id_event):
        """
        search in events (in the file), an event with the same id
        :return: True - if it finds an event with the same id
                 False - if it does not find an event with the same id
        """
        self.__read_all_from_file()
        return RepositoryEvents.findEvent(self, id_event)

    def modifyEvent(self, event):
        """
        Update the event with the given id, with the new data and modify the event dictionary and the file where
        store
        :param event: event
        :return:
        """
        self.__read_all_from_file()
        RepositoryEvents.modifyEvent(self, event)
        self.__write_all_to_file()

    def deleteEvent(self, id_event):
        """
        Delete the event with the given id
        :param id_event:
        :return:
        """
        self.__read_all_from_file()
        RepositoryEvents.deleteEvent(self, id_event)
        self.__write_all_to_file()

    def getAllEvents(self):
        """
        Returns a list of all existing events
        :rtype: list of Event type objects
        :return:
        """
        self.__read_all_from_file()
        return RepositoryEvents.getAllEvents(self)

    def size_repository(self):
        """
        :return: the numbe of events
        """
        self.__read_all_from_file()
        return RepositoryEvents.size(self)
