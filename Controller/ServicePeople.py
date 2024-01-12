from Domain.Person import Person


class ServicePeople:
    """
    GRASP Controller
    Responsible for performing the operations requested by the user
    Coordinates the necessary operations to carry out the action triggered by the user
    (i.e. trigger action: user -> ui-> service type object in ui -> service -> service coordinates the operations
    using other objects (e.g. repo, validator) to actually perform the operation
    """

    def __init__(self, __repository_people, __validator_person):
        """
        Initialize service
        :param __repository_persons: repo type object that helps us manage the crowd of people
        :param __people_validator: validator for checking people
        """
        self.__repoPeople = __repository_people
        self.__validatorPerson = __validator_person

    def size_service(self):
        """
        Returns the length of the list of people
        :return:
        """
        return self.__repoPeople.size_repository()

    def addPerrson(self, id_person, name, address):
        """
        Valiidate and add a person if the input is valid
        :param id_person:
        :param name:
        :param address:
        :return:
        """
        person = Person(id_person, name, address)
        self.__validatorPerson.validate(person)
        self.__repoPeople.addPerson(person)

    def findPerson(self, id_person):
        """
        Search for a person with the given id
        :param id_person:
        :return:
        """
        self.__validatorPerson.validate_id(id_person)
        return self.__repoPeople.findPerson(id_person)

    def modifyPerson(self, id_person, name, address):
        """
        Validate the inpuut and if that's valiid modify  the person with the given id
        :param id_person:
        :param name:
        :param address:
        :return:
        """
        person = Person(id_person, name, address)
        self.__validatorPerson.validate(person)
        self.__repoPeople.modifyPerson(person)

    def getAllPeople(self):
        """
        :return: a list with all people
        """
        return self.__repoPeople.gatAllPeoplee()
