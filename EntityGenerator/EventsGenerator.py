class EntityGeneration:
    def __init__(self, service_evenimente):
        self.__service_evenimente = service_evenimente

    def generate_event(self):
        """
        Generate an event
        :return:
        """
        import random
        self.__id_event = random.randint(1000, 9999)
        self.__date_day = random.randint(1, 31)
        self.__date_month = random.randint(1, 12)
        self.__date_year = random.randint(2022, 4000)
        self.__date_event = str(self.__date_day) + '/' + str(self.__date_month) + '/' + str(self.__date_year)
        self.__time_h = random.randint(1, 23)
        self.__time_min = random.randint(1, 59)
        self.__time_event = str(self.__time_h) + ":" + str(self.__time_min)
        self.__description_event = random.choice(["party", 'wedding', 'christening', 'untold', 'festival', 'Ec',
                                                    'Nervsea', "MediFun"])
        return self.__id_event, self.__date_event, self.__time_event, self.__description_event

    def generate_events(self, nr):
        """
        Generate a number of events
        :param nr:
        :return:
        """
        i = 0
        while i < nr:
            idd, date, time, description = self.generate_event()
            try:
                self.__service_evenimente.addEvent(idd, date, time, description)
                i += 1
            except:
                continue
