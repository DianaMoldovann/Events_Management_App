from Domain.Event import Event
from Domain.SignUp import SignUp
from Domain.Person import Person
from Repository.RepositorySignUp import RepositorySignUp


class FileRepositorySignUp(RepositorySignUp):

    def __init__(self, path):
        """
        The class created with the responsibility of managing signUps and storing them in a file
        :param path: the path to the text file where we store the address
        """
        RepositorySignUp.__init__(self)
        self.path = path

    def __read_all_from_file(self):
        """
        Read from the file where we store the signUps, all the signUps and add them to the signUp repo
        :return:
        """
        with open(self.path, "r") as f:
            lines = f.readlines()
            self._signUps.clear()
            for line in lines:
                if line != "":
                    line = line.strip()
                    parts = line.split(', ')
                    id_signUp = int(parts[0])
                    person = Person(int(parts[1]), parts[2], parts[3])
                    event = Event(int(parts[4]), parts[5], parts[6], parts[7])
                    signUp = SignUp(id_signUp, person, event)
                    self._signUps[id_signUp] = signUp

    def __write_all_to_file(self):
        """
        Writes to the file on each line, each entry that is in the entries repo
        :return:
        """
        with open(self.path, "w") as f:
            for signUp in self._signUps.values():
                f.write(str(signUp) + "\n")

    def addSignUp(self, signUp):
        """
        Add an entry in the entries dictionary, but also in the file where we store the entries
        :param signUp: Signup
        :return:
        """
        self.__read_all_from_file()
        RepositorySignUp.addSignUp(self, signUp)
        self.__write_all_to_file()

    def findSignUp(self, id_signUp):
        """
        Search in the dictionary of entries (read from the file), the entry with the entered id
        :param id_signUp: int
        :return: True - if there is a signUp with this id
                 Flase - if there is no signUp with this id
        """
        self.__read_all_from_file()
        return RepositorySignUp.findSignUp(self, id_signUp)

    def modifySignUp(self, signUp):
        """
        Updates the signUp with the given id, with the new data and modifies the signUp dictionary and the file where they are
        store
        :param signUp: Signup
        :return:
        """
        self.__read_all_from_file()
        RepositorySignUp.modifySignUp(self, signUp)
        self.__write_all_to_file()

    def deleteSignUp(self, id_signUp):
        """
        Updates the signUp with the given id, with the new data and modifies the signUp dictionary and the file where they are
        blind
        :param signUp: Signup
        :return:
        """
        self.__read_all_from_file()
        RepositorySignUp.deleteSignUp(self, id_signUp)
        self.__write_all_to_file()

    def size(self):
        """
        Returns the number of entries present in the entries dictionary or the number of lines in the where file
        we store them
        :return:
        """
        self.__read_all_from_file()
        return RepositorySignUp.size(self)

    def getAllSignsUps(self):
        """
        Reruns a list with all signUps
        :return:
        """
        self.__read_all_from_file()
        return RepositorySignUp.getAllSignsUps(self)

    def write_list_to_file(self, cale_fisier_raport, lista_sortata):
        """
        Write a list of reports in the file
        :param report_file_path:
        :param sorted_list:
        :return:
        """
        with open(cale_fisier_raport, "w") as f:
            if len(lista_sortata) == 0:
                f.write("The events has no people sigUp!")
            else:
                for element in lista_sortata:
                    f.write(str(element) + '\n')
