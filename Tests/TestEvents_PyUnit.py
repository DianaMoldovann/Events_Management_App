import unittest
import datetime

from Controller.ServiceEvents import ServiceEvents
from Domain.Event import Event
from Repository.FileRepositoryEvents import FileRepositoryEvents
from Validator.EventValidator import EventValidator
from Errors.Exeptions import ValidatorError, RepositoryError


class TestsEventDomain(unittest.TestCase):
    def setUp(self):
        self.__id_event = 2200
        self.__date = datetime.date(2024, 8, 9)
        self.__time = "11:34"
        self.__description = "nunta"
        self.__event = Event(self.__id_event, self.__date, self.__time, self.__description)
        self.__new_date = datetime.date(2003, 9, 23)
        self.__new_time = '20:56'
        self.__new_description = 'botez'

    def tearDown(self):
        pass

    def test_init_event(self):
        self.assertTrue(self.__event.get_id_event() == self.__id_event)
        self.assertTrue(self.__event.get_date() == self.__date)
        self.assertTrue(self.__event.get_time() == self.__time)
        self.assertTrue(self.__event.get_description() == self.__description)

    def test_set_event(self):
        self.__event.set_date(self.__new_date)
        self.__event.set_time(self.__new_time)
        self.__event.set_description(self.__new_description)
        self.assertTrue(self.__event.get_date() == self.__new_date)
        self.assertTrue(self.__event.get_time() == self.__new_time)
        self.assertTrue(self.__event.get_description() == self.__new_description)

    def test_equ_event(self):
        event_same_id = Event(self.__id_event, self.__new_date, self.__new_time, self.__new_description)
        self.assertTrue(event_same_id == self.__event)

    def test_str_event(self):
        self.assertTrue(self.__event.__str__() == "2200, 2024-08-09, 11:34, nunta")


class TestsEventValidator(unittest.TestCase):
    def setUp(self):
        self.__validator = EventValidator()
        self.__id_event = 2200
        self.__date = "9/8/2024"
        self.__date_test = datetime.date(2024, 8, 9)
        self.__time = "11:34"
        self.__description = "nunta"
        self.__event = Event(self.__id_event, self.__date, self.__time, self.__description)

    def tearDown(self):
        pass

    def test_validator_events_white_box(self):
        self.__validator.validate(self.__event)
        try:
            self.assertFalse(self.__validator.validate(Event(-23, '12/12/2020', '23:00', "MediFun")))
        except ValidatorError as ve:
            self.assertTrue(str(ve) == "Invalid id!\n")
        try:
            self.assertFalse(self.__validator.validate(Event(-2300, '12/12/2020', '23:00', "MediFun")))
        except ValidatorError as ve:
            self.assertTrue(str(ve) == "Invalid id!\n")
        try:
            self.assertFalse(self.__validator.validate(Event(234, '12/12/2020', '23:00', "MediFun")))
        except ValidatorError as ve:
            self.assertTrue(str(ve) == "Invalid id!\n")
        try:
            self.assertFalse(self.__validator.validate(Event(0000, '12/12/2020', '23:00', "MediFun")))
        except ValidatorError as ve:
            self.assertTrue(str(ve) == "Invalid id!\n")
        try:
            self.assertFalse(self.__validator.validate(Event(1111, '34/12/0', '23:00', "MediFun")))
        except ValidatorError as ve:
            self.assertTrue(str(ve) == "Invalid Date!\n")
        try:
            self.assertFalse(self.__validator.validate(Event(1111, '-2/3/2323', '23:00', "MediFun")))
        except ValidatorError as ve:
            self.assertTrue(str(ve) == "Invalid Date!\n")
        try:
            self.assertFalse(self.__validator.validate(Event(1111, '1/16/2323', '23:00', "MediFun")))
        except ValidatorError as ve:
            self.assertTrue(str(ve) == "Invalid Date!\n")
        try:
            self.assertFalse(self.__validator.validate(Event(1111, '6/0/2323', '23:00', "MediFun")))
        except ValidatorError as ve:
            self.assertTrue(str(ve) == "Invalid Date!\n")
        try:
            self.assertFalse(self.__validator.validate(Event(1111, '2/3/0', '23:00', "MediFun")))
        except ValidatorError as ve:
            self.assertTrue(str(ve) == "Invalid Date!\n")
        try:
            self.assertFalse(self.__validator.validate(Event(1111, '2/3/2323', '26:00', "MediFun")))
        except ValidatorError as ve:
            self.assertTrue(str(ve) == "Invalid Time!\n")
        try:
            self.assertFalse(self.__validator.validate(Event(1111, '2/3/2323', '0:08', "MediFun")))
        except ValidatorError as ve:
            self.assertTrue(str(ve) == "Invalid Time!\n")
        try:
            self.assertFalse(self.__validator.validate(Event(1111, '2/3/2323', '10:234', "MediFun")))
        except ValidatorError as ve:
            self.assertTrue(str(ve) == "Invalid Time!\n")
        try:
            self.assertFalse(self.__validator.validate(Event(1111, '2/3/2323', '10:08', "")))
        except ValidatorError as ve:
            self.assertTrue(str(ve) == "Invalid Description!\n")
        try:
            self.assertFalse(self.__validator.validate(Event(111, '82/-9/2323', '56:89', "")))
        except ValidatorError as ve:
            self.assertTrue(str(ve) == "Invalid id!\nInvalid Date!\nInvalid Time!\nInvalid Description!\n")

    def test_validator_events_black_box(self):
        self.__validator.validate(self.__event)
        try:
            self.assertFalse(self.__validator.validate(Event(238, '12/12/2020', '23:00', "MediFun")))
        except ValidatorError as ve:
            self.assertTrue(str(ve) == "Invalid id!\n")
        try:
            self.assertFalse(self.__validator.validate(Event(2383, '', '23:00', "MediFun")))
        except ValidatorError as ve:
            self.assertTrue(str(ve) == "Invalid Date!\n")
        try:
            self.assertFalse(self.__validator.validate(Event(2383, '23/09/2003', '', "MediFun")))
        except ValidatorError as ve:
            self.assertTrue(str(ve) == "Invalid Time!\n")
        try:
            self.assertFalse(self.__validator.validate(Event(1111, '2/3/2323', '10:08', "")))
        except ValidatorError as ve:
            self.assertTrue(str(ve) == "Invalid Description!\n")
        try:
            self.assertFalse(self.__validator.validate(Event(111, '', '', "")))
        except ValidatorError as ve:
            self.assertTrue(str(ve) == "Invalid id!\nInvalid Date!\nInvalid Time!\nInvalid Description!\n")


class TestsFileRepositoryPeeople(unittest.TestCase):
    def setUp(self):
        self.__path_file_tests = 'TestEvents.txt'
        self.__file_repository_events = FileRepositoryEvents(self.__path_file_tests)
        self.__empty_the_file_for_tests()
        self.__id_event = 2200
        self.__date = datetime.date(2024, 8, 9)
        self.__time = "11:34"
        self.__description = "nunta"
        self.__event = Event(self.__id_event, self.__date, self.__time, self.__description)
        self.__new_date = datetime.date(2003, 9, 23)
        self.__new_time = '20:56'
        self.__new_description = 'botez'

    def tearDown(self):
        pass

    def __empty_the_file_for_tests(self):
        with open(self.__path_file_tests, "w") as f:
            pass

    def test_add_event_repository(self):
        self.assertEqual(self.__file_repository_events.size_repository(), 0)
        self.__file_repository_events.addEvent(self.__event)
        self.assertEqual(self.__file_repository_events.size_repository(), 1)
        try:
            self.assertFalse(self.__file_repository_events.addEvent(self.__event))
        except RepositoryError as re:
            self.assertEqual(str(re), "There is already a event with the same id!")

    def test_find_event_repository(self):
        self.__file_repository_events.addEvent(self.__event)
        persoana_cautata = self.__file_repository_events.findEvent(self.__id_event)
        self.assertEqual(persoana_cautata.get_date(), self.__date)
        try:
            self.assertFalse(self.__file_repository_events.findEvent(2450))
        except RepositoryError as re:
            self.assertEqual(str(re), "Event not found!\n")

    def test_modify_event_repository(self):
        self.__file_repository_events.addEvent(self.__event)
        modify_event = Event(self.__id_event, self.__new_date, self.__new_time, self.__new_description)
        self.__file_repository_events.modifyEvent(modify_event)
        searched_event = self.__file_repository_events.findEvent(self.__id_event)
        self.assertEqual(searched_event.get_date(), self.__new_date)

    def test_delete_event_repository(self):
        self.__file_repository_events.addEvent(self.__event)
        self.__file_repository_events.deleteEvent(self.__id_event)
        self.assertTrue(self.__file_repository_events.size_repository() == 0)
        try:
            self.assertFalse(self.__file_repository_events.deleteEvent(2002))
        except RepositoryError as re:
            self.assertTrue(str(re) == "Event not found!\n")


class TesteEventsService(unittest.TestCase):
    def setUp(self):
        self.__path_file_tests = 'TestEvents.txt'
        self.__file_repository_events = FileRepositoryEvents(self.__path_file_tests)
        self.__validator_events = EventValidator()
        self.__service_events = ServiceEvents(self.__file_repository_events, self.__validator_events)
        self.__id_event = 2200
        self.__date = "9/8/2024"
        import datetime
        self.__date_test = datetime.date(2024, 8, 9)
        self.__time = "11:34"
        self.__description = "nunta"
        self.__event = Event(self.__id_event, self.__date, self.__time, self.__description)
        self.__id_invalid = '12'
        self.__date_invalid = '9/24'
        self.__time_imvalid = '25:89'
        self.__description_invalid = ''
        self.__event_invalid = Event(self.__id_invalid, self.__date_invalid, self.__time_imvalid,
                                         self.__description_invalid)
        self.__id_nou = 2332
        self.__new_date = '23/9/2003'
        self.__new_date_test = datetime.date(2003, 9, 23)
        self.__new_time = '20:56'
        self.__new_description = 'botez'

    def tearDown(self):
        pass

    def test_adaugare_event_service(self):

        self.assertTrue(self.__service_events.size_service() == 0)
        self.__service_events.addEvent(self.__id_event, self.__date, self.__time,
                                           self.__description)
        self.assertTrue(self.__service_events.size_service() == 1)
        try:
            self.assertFalse(self.__service_events.addEvent(self.__id_event, self.__date,
                                                                self.__time, self.__description))
        except RepositoryError as re:
            self.assertTrue(str(re) == "There is already a event with the same id!")
        try:
            self.assertFalse(self.__service_events.addEvent(self.__id_invalid, self.__date_invalid,
                                                                self.__time_imvalid,
                                                                self.__description_invalid))
        except ValidatorError as va:
            self.assertTrue(str(va) == "Invalid id!\nInvalid Date!\nInvalid Time!\nInvalid Description!\n")

    def test_cauta_event_service(self):
        searched_event = self.__service_events.findEvent(self.__id_event)
        self.assertTrue(searched_event.get_date() == self.__date_test)
        try:
            self.assertFalse(self.__service_events.findEvent(2006))
        except RepositoryError as re:
            self.assertTrue(str(re) == "Event not found!\n")

    def test_modifica_event_service(self):
        try:
            self.assertFalse(self.__service_events.modifyEvent(9000, self.__new_date,
                                                                   self.__new_time,
                                                                   self.__new_description))
        except RepositoryError as re:
            self.assertTrue(str(re) == "Event not found!\n")
        self.__service_events.modifyEvent(self.__id_event, self.__new_date, self.__new_time,
                                              self.__new_description)
        searched_event = self.__service_events.findEvent(self.__id_event)
        self.assertTrue(searched_event.get_date() == self.__new_date_test)
        self.__service_events.modifyEvent(self.__id_event, self.__date, self.__time,
                                              self.__description)
