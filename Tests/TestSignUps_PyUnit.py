import unittest
import datetime

from Controller.ServiceSingUp import ServiceSignUp
from Domain.Event import Event
from Domain.SignUp import SignUp
from Domain.Person import Person
from Repository.FileRepositoryEvents import FileRepositoryEvents
from Repository.FileRepositorySignUp import FileRepositorySignUp
from Repository.FileRepositoryPeople import FileRepositoryPeople
from Validator.SignInValidator import SignInValidator
from Errors.Exeptions import ValidatorError, RepositoryError


class TestesignUpsDomain(unittest.TestCase):
    def setUp(self):
        self.__id_signUp = 2200
        self.__persoana = Person(2022, "Moldovan Diana", "str.Daliilor nr.8 ap.11")
        self.__eveniment = Event(2222, '23/09/2002', '10:30', 'nunta')
        self.__signUp = SignUp(self.__id_signUp, self.__persoana, self.__eveniment)
        self.__persoana_noua = Person(3033, "Bosinceanu Raul", "str.Dumb nr.9 ap.10")
        self.__eveniment_nou = Event(3333, "27/08/2003", '13:45', 'botez')
        self.__signUp_acelasi_id = SignUp(self.__id_signUp, self.__persoana_noua, self.__eveniment_nou)

    def tearDown(self):
        pass

    def test_get_signUps(self):
        self.assertTrue(self.__signUp.get_id_signUp() == self.__id_signUp)
        self.assertTrue(self.__signUp.get_person() == self.__persoana)
        self.assertTrue(self.__signUp.get_event() == self.__eveniment)

    def test_eq_inscrier(self):
        assert(self.__signUp == self.__signUp_acelasi_id)

    def test_str_signUps(self):
        assert(self.__signUp.__str__() == "2200, 2022, Moldovan Diana, str.Daliilor nr.8 ap.11, 2222, 23/09/2002,"
                                             " 10:30, nunta")


class TestesignUpsValidator(unittest.TestCase):
    def setUp(self):
        self.__id_signUp = 2200
        self.__persoana = Person(2022, "Moldovan Diana", "str.Daliilor nr.8 ap.11")
        self.__eveniment = Event(2222, '23/09/2002', '10:30', 'nunta')
        self.__signUp = SignUp(self.__id_signUp, self.__persoana, self.__eveniment)

        self.__id_signUp_invalid = 22
        self.__persoana_invalida = Person(-24, 'nfnf', 'bhf')
        self.__eveniment_invalid = Event(-45, 'mdnjf', 'fnf', 'dnhjf')
        self.__signUp_invalida = SignUp(self.__id_signUp_invalid, self.__persoana, self.__eveniment)

    def tearDown(self):
        pass

    def test_validator_signUps(self):
        self.__validator_signUps = SignInValidator()
        self.__validator_signUps.validate(self.__signUp)
        try:
            self.__validator_signUps.validate(self.__signUp_invalida)
            assert False
        except ValidatorError as ve:
            assert(str(ve) == 'Invalid Id!\n')


class TestesignUpsRepository(unittest.TestCase):
    def setUp(self):
        self.__path = "/Users/dianamoldovan/PycharmProjects/tema_laborator 10/Tests/TestSignUps.txt"
        self.__file_repository_signUps = FileRepositorySignUp(self.__path)
        self.__id_signUp = 2200
        self.__persoana = Person(2022, "Moldovan Diana", "str.Daliilor nr.8 ap.11")
        self.__eveniment = Event(2222, '23/09/2002', '10:30', 'nunta')
        self.__signUp = SignUp(self.__id_signUp, self.__persoana, self.__eveniment)
        self.__id_signUp_invalid = 22
        self.__persoana_invalida = Person(-24, 'nfnf', 'bhf')
        self.__eveniment_invalid = Event(-45, 'mdnjf', 'fnf', 'dnhjf')
        self.__signUp_invalida = SignUp(self.__id_signUp_invalid, self.__persoana, self.__eveniment)
        self.__id_signUp_nou = 1234
        self.__persoana_noua = Person(3033, "Bosinceanu Raul", "str.Dumb nr.9 ap.10")
        self.__eveniment_nou = Event(3333, "27/08/2003", '13:45', 'botez')
        self.__signUp_acelasi_id = SignUp(self.__id_signUp, self.__persoana_noua, self.__eveniment_nou)
        self.__signUp_noua = SignUp(self.__id_signUp_nou, self.__persoana_noua, self.__eveniment_nou)
        self.__empty_file()
        self.__file_repository_signUps.addSignUp(self.__signUp)

    def tearDown(self):
        pass

    def __empty_file(self):
        with open(self.__path, "w") as f:
            pass

    def test_add_signUp(self):
        self.assertTrue(self.__file_repository_signUps.size() == 1)
        try:
            self.assertFalse(self.__file_repository_signUps.addSignUp(self.__signUp_acelasi_id))
        except RepositoryError as re:
            self.assertTrue(str(re) == 'There is already a signUp with this id!\n')

    def test_modify_signUp(self):
        self.__file_repository_signUps.modifySignUp(self.__signUp_acelasi_id)
        signUp_searched = self.__file_repository_signUps.findSignUp(self.__id_signUp)
        self.assertTrue(signUp_searched.get_person() == self.__persoana_noua)
        self.assertTrue(signUp_searched.get_event() == self.__eveniment_nou)

    def test_find_signUp(self):
        signUp_searched = self.__file_repository_signUps.findSignUp(self.__id_signUp)
        print(type(signUp_searched.get_person().get_id_person()), self.__persoana.get_id_person())
        self.assertTrue(signUp_searched.get_person().get_id_person() == self.__persoana.get_id_person())
        try:
            self.assertFalse(self.__file_repository_signUps.findSignUp(2333))
        except RepositoryError as re:
            self.assertTrue(str(re) == "Signup not found!\n")

    def test_sterge_signUp(self):
        self.assertTrue(self.__file_repository_signUps.size() == 1)
        self.__file_repository_signUps.deleteSignUp(self.__id_signUp)
        self.assertTrue(self.__file_repository_signUps.size() == 0)
        try:
            self.assertFalse(self.__file_repository_signUps.deleteSignUp(self.__id_signUp))
        except RepositoryError as re:
            self.assertTrue(str(re) == 'Signup not found!\n')


class TestsSignUpsService(unittest.TestCase):

    def setUp(self):
        self.__cale_fisier_signUps = "/Users/dianamoldovan/PycharmProjects/tema_laborator 10/Tests/teste_" \
                                       "signUps.txt"
        self.__cale_fisier_peoplea = "/Users/dianamoldovan/PycharmProjects/tema_laborator 10/Tests/teste_" \
                                       "people.txt"
        self.__cale_fisier_evenimente = "/Users/dianamoldovan/PycharmProjects/tema_laborator 10/Tests/teste_" \
                                        "evenimente.txt"
        self.__file_repo_signUps = FileRepositorySignUp(self.__cale_fisier_signUps)
        self.__file_repo_people = FileRepositoryPeople(self.__cale_fisier_peoplea)
        self.__file_repo_evenimente = FileRepositoryEvents(self.__cale_fisier_evenimente)
        self.__validator_signUps = SignInValidator()
        self.__service_signUps = ServiceSignUp(self.__file_repo_signUps, self.__file_repo_people,
                                                 self.__file_repo_evenimente, self.__validator_signUps)

        self.__id_signUp = 2200
        self.__persoana = Person(2022, "Moldovan Diana", "str.Daliilor nr.8 ap.11")
        self.__eveniment = Event(2222, datetime.date(2002, 9, 23), '10:30', 'nunta')
        self.__signUp = SignUp(self.__id_signUp, self.__persoana, self.__eveniment)

        self.__id_signUp_invalid = 22
        self.__persoana_invalida = Person(-24, 'nfnf', 'bhf')
        self.__eveniment_invalid = Event(-45, 'mdnjf', 'fnf', 'dnhjf')
        self.__signUp_invalida = SignUp(self.__id_signUp_invalid, self.__persoana, self.__eveniment)
        self.__id_signUp_nou = 1234
        self.__persoana_noua = Person(3033, "Bosinceanu Raul", "str.Dumb nr.9 ap.10")
        self.__eveniment_nou = Event(3333, datetime.date(2003, 8, 27), '13:45', 'botez')
        self.__signUp_acelasi_id = SignUp(self.__id_signUp, self.__persoana_noua, self.__eveniment_nou)
        self.__signUp_noua = SignUp(self.__id_signUp_nou, self.__persoana_noua, self.__eveniment_nou)

        self.__persoana1 = Person(1111, 'Moldovan Diana', 'str.Daliilor nr.8 ap.11')
        self.__persoana2 = Person(2222, 'Viorel Alexandra', 'str.Daliilor nr.8 ap.11')
        self.__persoana3 = Person(3333, 'Bosinceanu Raul', 'str.Daliilor nr.8 ap.11')
        self.__persoana4 = Person(4444, 'Petrila Ilinca', 'str.Lunga nr.20 ap.30')

        self.__eveniment1 = Event(1000, datetime.date(2003, 8, 27), '13:45', 'ec')
        self.__eveniment2 = Event(2000, datetime.date(2003, 8, 22), '13:45', 'botez')
        self.__eveniment3 = Event(3000, datetime.date(2003, 9, 22), '13:45', 'untold')
        self.__eveniment4 = Event(4000, datetime.date(2009, 1, 12), '13:45', 'mEdiFun')
        self.__eveniment5 = Event(5000, datetime.date(2003, 10, 2), '13:45', 'nunta')
        self.__eveniment6 = Event(6000, datetime.date(2003, 9, 22), '13:45', 'party bratari')
        self.__eveniment7 = Event(7000, datetime.date(2023, 9, 20), '13:45', 'dj. Cristian Rujoi')
        self.__eveniment8 = Event(8000, datetime.date(2013, 4, 4), '13:45', 'manepica')
        self.__eveniment9 = Event(9000, datetime.date(2066, 9, 8), '13:45', 'nerversea')
        self.__eveniment10 = Event(1100, datetime.date(2053, 7, 10), '13:45', 'cumetrie')

        self.__signUp1 = SignUp(1001, 1111, 1000)
        self.__signUp2 = SignUp(1002, 1111, 2000)
        self.__signUp3 = SignUp(1003, 1111, 3000)
        self.__signUp4 = SignUp(1004, 2222, 9000)
        self.__signUp5 = SignUp(1005, 4444, 1000)
        self.__signUp6 = SignUp(1006, 4444, 6000)
        self.__signUp7 = SignUp(1007, 4444, 8000)
        self.__signUp8 = SignUp(1008, 4444, 9000)
        self.__signUp9 = SignUp(1009, 3333, 1000)
        self.__signUp10 = SignUp(1010, 3333, 1100)

        self.goleste_fisier(self.__cale_fisier_signUps)
        self.goleste_fisier(self.__cale_fisier_peoplea)
        self.goleste_fisier(self.__cale_fisier_evenimente)

        self.__file_repo_people.addPerson(self.__persoana1)
        self.__file_repo_people.addPerson(self.__persoana2)
        self.__file_repo_people.addPerson(self.__persoana3)
        self.__file_repo_people.addPerson(self.__persoana4)
        self.__file_repo_evenimente.addEvent(self.__eveniment1)
        self.__file_repo_evenimente.addEvent(self.__eveniment2)
        self.__file_repo_evenimente.addEvent(self.__eveniment3)
        self.__file_repo_evenimente.addEvent(self.__eveniment4)
        self.__file_repo_evenimente.addEvent(self.__eveniment5)
        self.__file_repo_evenimente.addEvent(self.__eveniment6)
        self.__file_repo_evenimente.addEvent(self.__eveniment7)
        self.__file_repo_evenimente.addEvent(self.__eveniment8)
        self.__file_repo_evenimente.addEvent(self.__eveniment9)
        self.__file_repo_evenimente.addEvent(self.__eveniment10)

        self.__service_signUps.addSignUp(self.__signUp1.get_id_signUp(),
                                           self.__persoana1.get_id_person(),
                                           self.__eveniment1.get_id_event())
        self.__service_signUps.addSignUp(self.__signUp2.get_id_signUp(),
                                           self.__persoana1.get_id_person(),
                                           self.__eveniment2.get_id_event())
        self.__service_signUps.addSignUp(self.__signUp3.get_id_signUp(),
                                           self.__persoana1.get_id_person(),
                                           self.__eveniment3.get_id_event())
        self.__service_signUps.addSignUp(self.__signUp4.get_id_signUp(),
                                           self.__persoana2.get_id_person(),
                                           self.__eveniment9.get_id_event())
        self.__service_signUps.addSignUp(self.__signUp5.get_id_signUp(),
                                           self.__persoana4.get_id_person(),
                                           self.__eveniment1.get_id_event())
        self.__service_signUps.addSignUp(self.__signUp6.get_id_signUp(),
                                           self.__persoana4.get_id_person(),
                                           self.__eveniment6.get_id_event())
        self.__service_signUps.addSignUp(self.__signUp7.get_id_signUp(),
                                           self.__persoana4.get_id_person(),
                                           self.__eveniment8.get_id_event())
        self.__service_signUps.addSignUp(self.__signUp8.get_id_signUp(),
                                           self.__persoana4.get_id_person(),
                                           self.__eveniment9.get_id_event())
        self.__service_signUps.addSignUp(self.__signUp9.get_id_signUp(),
                                           self.__persoana3.get_id_person(),
                                           self.__eveniment1.get_id_event())
        self.__service_signUps.addSignUp(self.__signUp10.get_id_signUp(),
                                           self.__persoana3.get_id_person(),
                                           self.__eveniment10.get_id_event())

    def tearDown(self):
        pass

    def goleste_fisier(self, cale_fisier):
        with open(cale_fisier, "w") as f:
            pass

    def test_stergere_persoana_service(self):
        self.assertTrue(self.__file_repo_people.size_repository() == 4)
        self.__service_signUps.deletePerson(self.__persoana1.get_id_person())
        self.assertTrue(self.__file_repo_people.size_repository() == 3)
        try:
            self.assertFalse(self.__service_signUps.deletePerson(1222))
        except RepositoryError as re:
            self.assertTrue(str(re) == "Person not found!\n")

    def test_stergere_eveniment_service(self):
        self.assertTrue(self.__file_repo_evenimente.size_repository() == 10)
        self.__service_signUps.deleteEvent(self.__eveniment1.get_id_event())
        self.assertTrue(self.__file_repo_evenimente.size_repository() == 9)
        try:
            self.assertFalse(self.__service_signUps.deleteEvent(9000))
        except RepositoryError as re:
            self.assertTrue(str(re) == "Event not found!!\n")

    def test_add_signUp_service(self):
        self.__file_repo_people.addPerson(self.__persoana)
        self.__file_repo_evenimente.addEvent(self.__eveniment)
        self.assertTrue(self.__service_signUps.size() == 10)
        self.__service_signUps.addSignUp(self.__id_signUp, self.__persoana.get_id_person(),
                                           self.__eveniment.get_id_event())
        self.assertTrue(self.__service_signUps.size() == 11)
        try:
            self.assertFalse(self.__service_signUps.addSignUp(self.__id_signUp_invalid,
                                                                self.__persoana.get_id_person(),
                                                                self.__eveniment.get_id_event()))
        except ValidatorError as ve:
            self.assertTrue(str(ve) == 'Invalid Id!\n')

    def test_modify_signUp_service(self):
        self.__file_repo_people.addPerson(self.__persoana_noua)
        self.__file_repo_evenimente.addEvent(self.__eveniment_nou)
        self.__service_signUps.modifySignUp(self.__signUp1.get_id_signUp()
                                              , self.__persoana_noua.get_id_person(),
                                              self.__eveniment_nou.get_id_event())
        signUp_searched = self.__service_signUps.findSignUp(
            self.__signUp1.get_id_signUp())
        self.assertTrue(signUp_searched == self.__signUp1)
        try:
            self.assertFalse(self.__service_signUps.modifySignUp(self.__id_signUp_invalid,
                                                                   self.__persoana_noua.get_id_person(),
                                                                   self.__eveniment_nou.get_id_event()
                                                                   ))
        except ValidatorError as ve:
            self.assertTrue(str(ve) == "Invalid Id!\n")
        try:
            self.assertFalse(self.__service_signUps.modifySignUp(self.__id_signUp_nou,
                                                                   self.__persoana_noua.get_id_person(),
                                                                   self.__eveniment_nou.get_id_event()
                                                                   ))
        except RepositoryError as re:
            self.assertTrue(str(re) == "SignUp not found!\n")

    def test_find_signUp_dupa_id_service(self):
        signUp_searched = self.__service_signUps.findSignUp(
                            self.__signUp1.get_id_signUp())
        assert (signUp_searched == self.__signUp1)
        try:
            self.__service_signUps.findSignUp(4566)
            assert False
        except RepositoryError as re:
            self.assertTrue(str(re) == "Signup not found!\n")

    def test_sterge_signUp_dupa_id_service(self):
        self.__service_signUps.deleteSignUp(self.__signUp1.get_id_signUp())
        self.assertTrue(self.__service_signUps.size() == 9)
        try:
            self.__service_signUps.deleteSignUp(4556)
            assert False
        except RepositoryError as re:
            self.assertTrue(str(re) == "Signup not found!\n")

    def test_creeaza_situatie_people(self):
        situatie_people = self.__service_signUps.getPeopleSituations()
        self.assertTrue(len(situatie_people) == 4)

    def test_creeaza_situatie_people_DTO(self):
        situatie_people_DTO = self.__service_signUps.getEventsSituation()
        self.assertTrue(len(situatie_people_DTO) == 7)

    def test_lista_de_evenimente_pt_o_persoana_ordonata_alfabetic(self):
        lista_ordonata = self.__service_signUps.get_events_list_of_a_person_order_by_description(
            self.__persoana1.get_id_person())
        self.assertTrue(lista_ordonata[0] == self.__eveniment2)
        self.assertTrue(lista_ordonata[1] == self.__eveniment1)
        self.assertTrue(lista_ordonata[2] == self.__eveniment3)

    def test_lista_de_evenimente_pt_o_persoana_ordonata_dupa_data(self):
        lista_ordonata = self.__service_signUps.get_events_list_of_a_person_order_by_date(
            self.__persoana1.get_id_person())
        self.assertTrue(lista_ordonata[0] == self.__eveniment2)
        self.assertTrue(lista_ordonata[1] == self.__eveniment1)
        self.assertTrue(lista_ordonata[2] == self.__eveniment3)

    def test_creeaza_situatie_evenimente(self):
        situatie_evenimente = self.__service_signUps.getEventsSituation()
        self.assertTrue(len(situatie_evenimente) == 7)

    def test_creeaza_situatie_evenimente_DTO(self):
        situatie_evenimente_dto = self.__service_signUps.getEventsSituationDTO()
        self.assertTrue(len(situatie_evenimente_dto) == 7)

    def test_evenimente_cu_cele_mai_multe_people(self):
        lista_ordonata = self.__service_signUps.get_the_events_with_the_most_people()
        self.assertTrue(lista_ordonata[0].get_event() == self.__eveniment1)
        self.assertTrue(lista_ordonata[1].get_event() == self.__eveniment9)

    def test_lista_de_people_ordonate_alfabetic(self):
        lista_ordonata = self.__service_signUps.get_people_order_by_name(
            self.__eveniment1.get_id_event())
        self.assertTrue(lista_ordonata[0] == self.__persoana3)
        self.assertTrue(lista_ordonata[1] == self.__persoana1)
        self.assertTrue(lista_ordonata[2] == self.__persoana4)
