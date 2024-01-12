from Domain.SignUp import SignUp
from Domain.SignUpDTO import PersonSituation, EventSituation
from Errors.Exeptions import RepositoryError


class ServiceSignUp:
    """
    GRASP Controller
    Responsible for performing the operations requested by the user
    Coordinates the necessary operations to carry out the action triggered by the user
    (i.e. trigger action: user -> ui-> service type object in ui -> service -> coordinate service
    the operations
    using other objects (e.g. repo, validator) to actually perform the operation
    """

    def __init__(self, repository_signUps, repository_people, repository_events, validator_signUp):
        """
        :param repository_signUps:
        :param repository_people:
        :param repository_events:
        :param validator_signUp:
        """
        self.__validatorSignUp = validator_signUp
        self.__repoPeople = repository_people
        self.__repoEvents = repository_events
        self.__repoSignUps = repository_signUps

    def size(self):
        """
        Returns the length of the registration list
        :return:
        """
        return self.__repoSignUps.size()

    def addSignUp(self, id_signUp, id_person, id_event):
        """
        register a person to an event, that is, add a signUp with an id, a client and an event
        :param id_signUp:
        :param id_person:
        :param id_event:
        :return:
        """
        person = self.__repoPeople.findPerson(id_person)
        event = self.__repoEvents.findEvent(id_event)
        signUp = SignUp(id_signUp, person, event)
        self.__validatorSignUp.validate(signUp)
        self.__repoSignUps.addSignUp(signUp)

    def findSignUp(self, id_signUp):
        """
        look for a signUp by id in the list of signUps
        :param id_signUp:
        :return:
        """
        self.__validatorSignUp.validate_id(id_signUp)
        return self.__repoSignUps.findSignUp(id_signUp)

    def modifySignUp(self, id_signUp, id_person, id_event):
        """
        modify a signUp in the list of signUps
        :param id_signUp:
        :param id_person:
        :param id_event:
        :return:
        """
        person = self.__repoPeople.findPerson(id_person)
        event = self.__repoEvents.findEvent(id_event)
        signUp = SignUp(id_signUp, person, event)
        self.__validatorSignUp.validate(signUp)
        self.__repoSignUps.modifySignUp(signUp)

    def deleteSignUp(self, id_signUp):
        """
        Delete a signUp by id from the list of signUps
        :param id_signUp:
        :return:
        """
        self.__validatorSignUp.validate_id(id_signUp)
        self.__repoSignUps.deleteSignUp(id_signUp)

    def deletePerson(self, id_person):
        """
        Delete a person from the Repo persons and delete all the signUps in which it appears
        :param id_person:
        :return:
        """
        self.__validatorSignUp.validate_id(id_person)
        self.__repoPeople.deletePerson(id_person)
        lista = self.__repoSignUps.getAllSignsUps()
        for signUp in lista:
            if signUp.get_person().get_id_person() == id_person:
                self.__repoSignUps.deleteSignUp(signUp.get_id_signUp())

    def deleteEvent(self, id_event):
        """
        Delete an event from the Repo by id and delete all signUps of people at this event
        :param id_event:
        :return:
        """
        self.__validatorSignUp.validate_id(id_event)
        self.__repoEvents.deleteEvent(id_event)
        listOfSignUps = self.__repoSignUps.getAllSignsUps()
        for signUp in listOfSignUps:
            if signUp.get_event().get_id_event() == id_event:
                self.__repoSignUps.deleteSignUp(signUp.get_id_signUp())

    def getAllSignUps(self):
        """
        Returns the list of signUps
        :return:
        """
        return self.__repoSignUps.getAllSignsUps()

# --------------------------------------------------------RAPOARTE------------------------------------------------------

    def getPeopleSituations(self):
        """
        create a dictionary with the key id_person, in which we will enter the events to which he participates
        staff
        :return:
        """
        all_signUps = self.getAllSignUps()
        signUpsSituation = {}
        for signUp in all_signUps:
            id_person = signUp.get_person().get_id_person()
            if id_person not in signUpsSituation:
                signUpsSituation[id_person] = []
            signUpsSituation[id_person].append(signUp.get_event())
        return signUpsSituation

    def getEventsSituation(self):
        """
        It takes the situation dictionary and transforms each pair (key, value) into a DTO object
        SignUps situation. Create a list of DTO objects with a person, a list of events and an event number
        :return: rez - a list of DTO objects
        """
        rez = []
        signUpsSituation = self.getPeopleSituations()
        for id_person in signUpsSituation:
            person = self.__repoPeople.findPerson(id_person)
            listOfEvents = []
            for event in signUpsSituation[id_person]:
                listOfEvents.append(event.get_id_event())
            situation_DTO = PersonSituation(person, listOfEvents)
            rez.append(situation_DTO)
        return rez

    def get_events_list_of_a_person_order_by_description(self, id_person):
        """
        It takes the signUps situation dictionary, from it takes the list of events from key = id_person and
        sort alphabetically by description
        :param id_person: int
        :return:
        """
        self.__validatorSignUp.validate_id(id_person)
        self.__repoPeople.findPerson(id_person)
        signUpsSituation = self.getPeopleSituations()
        if id_person in signUpsSituation:
            lista_evente = signUpsSituation[id_person]
            lista_evente.sort(key=lambda x: x.get_description().lower(), reverse=False)
        else:
            raise RepositoryError("the person doesn't signUp for any Event")
        return lista_evente

    def get_events_list_of_a_person_order_by_date(self, id_person):
        """
        It takes the situation signUps dictionary, from it takes the list of events from key = id_person and
        sort by date
        :param id_person: int
        :return:
        """
        self.__validatorSignUp.validate_id(id_person)
        self.__repoPeople.findPerson(id_person)
        signUpsSituation = self.getPeopleSituations()
        if id_person in signUpsSituation:
            lista_evente = signUpsSituation[id_person]
            lista_evente.sort(key=lambda x: x.get_date(), reverse=False)
        else:
            raise RepositoryError("person nu are signUps")
        return lista_evente

    def get_the_person_signUp_at_the_most_events(self):
        """
        Takes the list of DTO objects and sorts it in descending order by event_number and selects the first 3 people
        with the largest number of events
        :return:
        """
        signUpsSituation_DTO = self.getEventsSituation()
        print(signUpsSituation_DTO)
        signUpsSituation_DTO.sort(key=lambda x: x.get_numberOfEvents(), reverse=True)
        rez = signUpsSituation_DTO[:3]
        return rez

    def getEventsSituation(self):
        """
        create a dictionary with the id_event key, in which we will enter the people participating in the event
        :return:
        """
        all_signUps = self.getAllSignUps()
        eventsSituation = {}
        for signUp in all_signUps:
            id_event = signUp.get_event().get_id_event()
            if id_event not in eventsSituation:
                eventsSituation[id_event] = []
            eventsSituation[id_event].append(signUp.get_person())
        return eventsSituation

    def getEventsSituationDTO(self):
        """
        It takes the situation dictionary and transforms each pair (key, value) into a DTO object
        situationsignUps. Create a list of DTO objects with an event, a list of people and a number of people
        :return: rez - a list of DTO objects
        """
        rez = []
        eventsSituation = self.getEventsSituation()
        for id_event in eventsSituation:
            event = self.__repoEvents.findEvent(id_event)
            listOfPeople = []
            for person in eventsSituation[id_event]:
                listOfPeople.append(person.get_id_person())
            situation_DTO = EventSituation(event, listOfPeople)
            rez.append(situation_DTO)
        return rez

    def get_the_events_with_the_most_people(self):
        """
        PGets the list of DTO objects and sorts it descending by number_persons and selects the first 20% events
        with the largest number of events
        :return:
        """
        eventsSituation_DTO = self.getEventsSituationDTO()
        eventsSituation_DTO.sort(key=lambda x: x.get_numberOfPeeople(), reverse=True)
        numar_evente = self.__repoEvents.size()
        procent = (20 * numar_evente)//100
        rez = eventsSituation_DTO[:procent]
        return rez

    def get_people_order_by_name(self, id_event):
        """
        It takes the dictionary of situation events, from it takes the list of people from key = id_event and them
        sort alphabetically
        :param id_event: int
        :return:
        """
        self.__validatorSignUp.validate_id(id_event)
        self.__repoEvents.findEvent(id_event)
        eventsSituation = self.getEventsSituation()
        if id_event in eventsSituation:
            lista_persoane = eventsSituation[id_event]
            lista_persoane.sort(key=lambda x: x.get_name(), reverse=False)
        else:
            raise RepositoryError("The event doesn'y have any person signUp")
        cale_fisier_rapoarte = "Raports.txt"
        self.__repoSignUps.write_list_to_file(cale_fisier_rapoarte, lista_persoane)
        return lista_persoane
