import unittest

from Controller.ServicePeople import ServicePeople
from Domain.Person import Person
from Repository.FileRepositoryPeople import FileRepositoryPeople
from Validator.PersonValidator import PersonValidator
from Errors.Exeptions import ValidatorError, RepositoryError


class TestPersoaneDomain(unittest.TestCase):
    def setUp(self):
        self.__id_person = 2002
        self.__nume = "Moldovan Diana"
        self.__adresa = "str.Daliilor, nr.8, ap.11"
        self.__person = Person(self.__id_person, self.__nume, self.__adresa)

    def tearDown(self):
        pass

    def test_init_person(self):
        self.assertEqual(self.__person.get_id_person(), 2002)
        self.assertEqual(self.__person.get_name(), "Moldovan Diana")
        self.assertEqual(self.__person.get_address(), "str.Daliilor, nr.8, ap.11")

    def test_set_person(self):
        self.__person.set_name("Bosinceanu Raul")
        self.__person.set_address("str. Dumbravei, nr.10, ap.18")
        self.assertEqual(self.__person.get_name(), "Bosinceanu Raul")
        self.assertEqual(self.__person.get_address(), "str. Dumbravei, nr.10, ap.18")

    def test_equ_persoane(self):
        person_acelasi_id = Person(2002, "Moldovan Diana", "str.Daliilor, nr.8, Sighisora")
        self.assertEqual(self.__person, person_acelasi_id)

    def test_str_person(self):
        self.assertEqual(self.__person.__str__(), "2002, Moldovan Diana, str.Daliilor, nr.8, ap.11")


class TestepersonValidator(unittest.TestCase):

    def setUp(self):
        self.__id_person = 2002
        self.__nume = "Moldovan Diana"
        self.__adresa = "str.Daliilor, nr.8, ap.11"
        self.__person = Person(self.__id_person, self.__nume, self.__adresa)
        self.__id_person_invalid = -2003
        self.__nume_invalid = ""
        self.__adresa_invalida = ""
        self.__person_invalida = Person(self.__id_person_invalid, self.__nume_invalid, self.__adresa_invalida)

    def tearDown(self):
        pass

    def test_validator_persoane(self):
        validator_person = PersonValidator()
        self.assertIsNone(validator_person.validate(self.__person))
        try:
            self.assertFalse(validator_person.validate(self.__person_invalida))
        except ValidatorError as ve:
            self.assertEqual(str(ve), "Invalid Id!\nInvalid Name!\nInvalid Address!\n")


class TestepersonFileRepository(unittest.TestCase):
    def setUp(self):
        self.__cale_fisier_teste = '/Users/dianamoldovan/PycharmProjects/tema_laborator 10/Tests/TestPeople.txt'
        self.__file_repository_persoane = FileRepositoryPeople(self.__cale_fisier_teste)
        self.__goleste_fisier_teste()
        self.__id_person = 2002
        self.__nume = "Moldovan Diana"
        self.__adresa = "str.Daliilor, nr.8, ap.11"
        self.__person = Person(self.__id_person, self.__nume, self.__adresa)

    def tearDown(self):
        pass

    def __goleste_fisier_teste(self):
        with open(self.__cale_fisier_teste, "w") as f:
            pass

    def test_add_person_repository(self):
        self.assertEqual(self.__file_repository_persoane.size_repository(), 0)
        self.__file_repository_persoane.addPerson(self.__person)
        self.assertEqual(self.__file_repository_persoane.size_repository(), 1)
        try:
            self.assertFalse(self.__file_repository_persoane.addPerson(self.__person))
        except RepositoryError as re:
            self.assertEqual(str(re), "There is already a person with this id!\n")

    def test_find_person_repository(self):
        self.__file_repository_persoane.addPerson(self.__person)
        person_searched = self.__file_repository_persoane.findPerson(self.__id_person)
        self.assertEqual(person_searched.get_name(), self.__nume)
        try:
            self.assertFalse(self.__file_repository_persoane.findPerson(2450))
        except RepositoryError as re:
            self.assertEqual(str(re), "Person not found!\n")

    def test_modify_person_repository(self):
        self.__file_repository_persoane.addPerson(self.__person)
        person_modify = Person(self.__id_person, "Ion", "str.Garofelor")
        self.__file_repository_persoane.modifyPerson(person_modify)
        person_searched = self.__file_repository_persoane.findPerson(self.__id_person)
        self.assertEqual(person_searched.get_name(), "Ion")

    def test_stergere_person_repository(self):
        self.__file_repository_persoane.addPerson(self.__person)
        self.__file_repository_persoane.deletePerson(self.__id_person)
        self.assertTrue(self.__file_repository_persoane.size_repository() == 0)
        try:
            self.assertFalse(self.__file_repository_persoane.deletePerson(2002))
        except RepositoryError as re:
            self.assertTrue(str(re) == "Person not found!\n")


class TestePersoaneService(unittest.TestCase):
    def setUp(self):
        self.__cale_fisier_teste = '/Users/dianamoldovan/PycharmProjects/tema_laborator 10/Tests/TestPeople.txt'
        self.__file_repository_persoane = FileRepositoryPeople(self.__cale_fisier_teste)
        self.__validator_persoane = PersonValidator()
        self.__service_persoane = ServicePeople(self.__file_repository_persoane, self.__validator_persoane)

        self.__id_person = 2002
        self.__nume = "Moldovan Diana"
        self.__adresa = "str.Daliilor, nr.8, ap.11"
        self.__person = Person(self.__id_person, self.__nume, self.__adresa)

    def tearDown(self):
        pass

    def test_add_person_service(self):
        self.assertEqual(self.__service_persoane.size_service(), 0)
        self.__service_persoane.addPerrson(self.__id_person, self.__nume, self.__adresa)
        self.assertEqual(self.__service_persoane.size_service(), 1)
        try:
            self.assertFalse(self.__service_persoane.addPerrson(self.__id_person, self.__nume,
                                                                self.__adresa))
        except RepositoryError as re:
            self.assertEqual(str(re), "There is already a person with this id!\n")
        try:
            self.assertFalse(self.__service_persoane.addPerrson(-23, '', ''))
        except ValidatorError as va:
            self.assertEqual(str(va), "Invalid Id!\nInvalid Name!\nInvalid Address!\n")

    def test_find_person_service(self):
        student_searched = self.__service_persoane.findPerson(self.__id_person)
        self.assertEqual(student_searched.get_name(), self.__nume)
        try:
            self.assertFalse(self.__service_persoane.findPerson(2006))
        except RepositoryError as re:
            self.assertEqual(str(re), 'Person not found!\n')
        try:
            self.assertFalse(self.__service_persoane.findPerson(200))
        except ValidatorError as ve:
            self.assertEqual(str(ve), 'Invalid Id!\n')

    def test_modify_person_service(self):
        try:
            self.assertFalse(self.__service_persoane.modifyPerson(self.__id_person, '', ''))
        except ValidatorError as va:
            self.assertEqual(str(va), "Invalid Name!\nInvalid Address!\n")
        try:
            self.assertFalse(self.__service_persoane.modifyPerson(self.__id_person, 'Paraschiv Dariua',
                                                                               "str.Garoafelor nr.10 ap.12"))
        except RepositoryError as re:
            self.assertEqual(str(re), 'Person not found!\n')
        self.__service_persoane.modifyPerson(self.__id_person, "Munteanu Lavinia", "str.Lunga nr.34 ap2")
        person_searched = self.__service_persoane.findPerson(self.__id_person)
        self.assertEqual(person_searched.get_name(), "Munteanu Lavinia")