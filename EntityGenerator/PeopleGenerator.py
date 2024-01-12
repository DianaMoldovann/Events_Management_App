class PeopleGenerator:
    def __init__(self, service_persoane):
        self.__service_persoane = service_persoane

    def generate_person(self):
        """
        Generate a random person
        :return:
        """
        import random
        self.__id_person = random.randint(1000, 9999)
        self.__lastName = random.choice(['Moldovan', 'Bosinceanu', 'Muntean', 'Ardelean', 'Olar', 'Petrila', 'Viorel',
                                     'Lacusteanu', 'Moraru', 'Adam'])
        self.__firstName = random.choice(['Diana', 'Andreea', 'Raul', 'Marian', 'Andrei', 'Rares', 'Ioana', 'Miăiță',
                                        'Tudor', 'Adriana', 'Ilinca'])
        self.__lastName_person = self.__lastName + ' ' + self.__firstName
        self.__address_str = random.choice(['Daliilor', 'Dumbravei', 'M.Viteazau', 'Garoafelor', 'B.Petriceicu',
                                              'Noua'])
        self.__address_nr = random.randint(0, 100)
        self.__address_ap = random.randint(0, 30)
        self.__address_person = "str." + self.__address_str + ' ' + "nr." + str(self.__address_nr) + ' ' + "ap." +\
                                 str(self.__address_ap)
        return self.__id_person, self.__lastName_person, self.__address_person

    def generate_people(self, nr):
        """
        Generate a number of people
        :param nr:
        :return:
        """
        i = 0
        while i < nr:
            idd, lastName, address = self.generate_person()
            try:
                self.__service_persoane.addPerrson(idd, lastName, address)
                i += 1
            except:
                continue
