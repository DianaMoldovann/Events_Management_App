from Domain.Person import Person
from Repository.RepositoryPeople import RepositoryPeople


class FileRepositoryPeople(RepositoryPeople):
    def __init__(self, path):
        """
        The class created with the responsibility of managing people and storing them in a file
        :param file_path: the path to the text file where we store the people
        """
        RepositoryPeople.__init__(self)
        self.__path = path

    def __read_all_from_file(self):
        """
        Reads one person from each line from the file and adds them to the dictionary in RepsoitoryPersons
        :return:
        """
        with open(self.__path, "r") as f:
            lines = f.readlines()
            self._people.clear()
            for line in lines:
                line = line.strip()
                if line != '':
                    parts = line.split(', ')
                    id_person= int(parts[0])
                    name = parts[1]
                    address= parts[2]
                    person = Person(id_person, name, address)
                    self._people[id_person] = person

    def __write_all_to_file(self):
        """
        Write in the file on each line one person from the dictionary of persons
        :return:
        """
        with open(self.__path, 'w') as f:
            for person in self._people.values():
                f.write(str(person) + "\n")

    def addPerson(self, person):
        """
        Add a person to the dictionary, but also to the file
        :param person: the person to be added
        :type person: Person
        ; the list of people is modified by adding the given person
        ; the text file is modified by adding the given person
        :return:
        """
        self.__read_all_from_file()
        RepositoryPeople.addPerson(self, person)
        self.__write_all_to_file()

    def findPerson(self, id_person):
        """
        search in persons (in the file), a person with the same id
        :return: True - if it finds a person with the same id
                 False - if it does not find a person with the same id
        """
        self.__read_all_from_file()
        return RepositoryPeople.findPerson(self, id_person)

    def modifyPerson(self, person):
        """
        It updates the person with the given ID, with the new data and modifies the persons dictionary and the file where they are
        store
        :param person: The person
        :return:
        """
        self.__read_all_from_file()
        RepositoryPeople.modifyPerson(self, person)
        self.__write_all_to_file()

    def deletePerson(self, id_person):
        """
        Delete the person with the given id
        :param id_person:
        :return:
        """
        self.__read_all_from_file()
        RepositoryPeople.deletePerson(self, id_person)
        self.__write_all_to_file()

    def gatAllPeoplee(self):
        """
        Returns a list of all existing people
        :rtype: list of objects of type Persons
        :return:
        """
        self.__read_all_from_file()
        return RepositoryPeople.gatAllPeoplee(self)

    def size_reppsitory(self):
        """
        Retuurn the number of the People
        :return:
        """
        self.__read_all_from_file()
        return RepositoryPeople.size_repository(self)
