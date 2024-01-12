from Controller.ServiceEvents import ServiceEvents
from Controller.ServiceSingUp import ServiceSignUp
from Controller.ServicePeople import ServicePeople
from EntityGenerator.EventsGenerator import EntityGeneration
from EntityGenerator.PeopleGenerator import PeopleGenerator
from Interface.UI import UI
from Repository.FileRepositoryEvents import FileRepositoryEvents
from Repository.FileRepositorySignUp import FileRepositorySignUp
from Repository.FileRepositoryPeople import FileRepositoryPeople
from Tests.teste_file_persoane import TesteFilePersoane
from Tests.teste_inscrieri import TesteInscrieri
from Validator.EventValidator import EventValidator
from Validator.SignInValidator import SignInValidator
from Validator.PersonValidator import PersonValidator


def run_main():
    teste_inscrieri = TesteInscrieri()
    # teste_inscrieri.ruleaza_toate_testele_inscrieri()

    teste_file_persoane = TesteFilePersoane()
    # teste_file_persoane.ruleaza_teste_file_repository()

    validator_persoane = PersonValidator()
    validator_evenimente = EventValidator()
    validator_inscrieri = SignInValidator()

    cale_fisier_persoane = "Persoane.txt"
    file_repository_persoane = FileRepositoryPeople(cale_fisier_persoane)
    cale_fiser_evenimente = "Events.txt"
    file_repository_evenimente = FileRepositoryEvents(cale_fiser_evenimente)
    cale_fiser_inscxrieri = "SignUps.txt"
    file_repository_inscrieri = FileRepositorySignUp(cale_fiser_inscxrieri)

    service_persoana = ServicePeople(file_repository_persoane, validator_persoane)
    service_eveniment = ServiceEvents(file_repository_evenimente, validator_evenimente)
    service_inscriere = ServiceSignUp(file_repository_inscrieri, file_repository_persoane,
                                      file_repository_evenimente, validator_inscrieri)

    generator_persoane = PeopleGenerator(service_persoana)
    generator_evenimente = EntityGeneration(service_eveniment)

    ui = UI(service_persoana, service_eveniment, service_inscriere, generator_persoane, generator_evenimente)
    ui.run_ui()


run_main()
