from Errors.Exeptions import RepositoryError


class RepositoryPeople:
    """
        The class created with the responsibility of managing the crowd
    """

    def __init__(self):
        """
        People is a dictionary whose elements are entities of the person type
        """
        self._people = {}

    def addPerson(self, person):
        """
        Add a person to the list
        :param person: the person to be added
        :type person: Person
        ; the list of people is modified by adding the given person
        :return:
        """
        if person.get_id_person() in self._people:
            raise RepositoryError("There is already a person with this id!\n")
        self._people[person.get_id_person()] = person

    def findPerson(self, id_person):
        """
        search in people, a person with the same id
        :return: True - if it finds a person with the same id
                 False - if it does not find a person with the same id
        """
        if id_person not in self._people:
            raise RepositoryError("Person not found!\n")
        return self._people[id_person]

    def modifyPerson(self, person):
        """
        update the Person with the same id
        :param person: Persoana
        :return:
        """
        if person.get_id_person() not in self._people:
            raise RepositoryError("Person not found!\n")
        self._people[person.get_id_person()] = person

    def gatAllPeoplee(self):
        """
        Returns a list of all existing people
        :rtype: list of objects of type Persons
        :return:
        """
        r = []
        for id_person in self._people:
            person = self._people[id_person]
            r.append(person)
        return r

    def deletePerson(self, id_person):
        if id_person not in self._people:
            raise RepositoryError("Person not found!\n")
        del self._people[id_person]

    def size_repository(self):
        """
        returneaza number of people
        :return:
        """
        return len(self._people)
