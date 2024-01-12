from Errors.Exeptions import ValidatorError, RepositoryError


class UI(object):

    def __init__(self, service_persoana, service_eveniment, service_inscriere, generator_persoane,
                 generator_evenimente):
        self.__generator_evenimente = generator_evenimente
        self.__generator_persoane = generator_persoane
        self.__service_inscriere = service_inscriere
        self.__service_eveniment = service_eveniment
        self.__service_persoana = service_persoana
        self.__comenzi = {
            "adauga_persoana": self.__ui_adauga_persoana,
            "sterge_persoana_dupa_id": self.__ui_sterge_persoana_dupa_id,
            "modifica_persoana": self.__ui_modifica_persoana,
            "cauta_persoana_dupa_id": self.__ui_cauta_persoana_dupa_id,
            "generare_persoane": self.__ui_generare_persoane,
            "adauga_eveniment": self.__ui_adauga_eveniment,
            "sterge_eveniment_dupa_id": self.__ui_sterge_eveniment_dupa_id,
            "modifica_eveniment": self.__ui_modifica_eveniment,
            "cauta_eveniment_dupa_id": self.__ui_cauta_eveniment_dupa_id,
            "generare_evenimente": self.__ui_generare_evenimente,
            "inscrie_persoana_la_eveniment": self.__ui_adauga_inscriere,
            "print_persoane": self.__ui_print_persoane,
            "print_evenimente": self.__ui_print_evenimente,
            "print_inscrieri": self.__ui_print_inscrieri,
            "lista_de_evenimente_ordonate_alfabetic": self.__ui_lista_de_evenimente_ordonate_alfacebtic,
            "lista_de_evenimente_ordonate_dupa_data": self.__ui_lista_de_evenimente_ordonate_dupa_data,
            "persoane_participante_la_cele_mai_multe_evenimente":
                self.__ui_persoane_participante_la_cele_mai_multe_evenimente,
            "primele_20%_evenimente_cu_cei_mai_mulți_participanți": self.__ui_evenimente_cu_cele_mai_multe_persoane,
            "lista_de_persoane_ordonate_alfabetic": self.__ui_lista_de_persoane_ordonate_alfabetic
        }

    def __print_menu(self):
        print('\n\n\n\n\n\n\n\n\n\n\n')
        print('------------------------------------------------------------APLICATIA DE ORGANIZARE A EVENIMENTELOR-----'
              '-------------------------------------------------------\n\n')
        print('Aplicatia gestioneaza persoane si evenimente\n')
        print('Fiecare persoana are un id unic format din patru cifre, un nume si un prenume si o adresa formata din '
              'str., nr. si ap.')
        print('Persoana: XXXX, Nume Prenume, str.Nume_Strada nr.NR ap.AP\n')
        print('Fiecare eveniment are un id unic format din patru cifre, o data, un timp si o descriere')
        print('Evenimente: XXXX, zz/ll/aaaa, hh:mm, Descriere\n\n')
        print('MENIU DE TIP CONSOLA:')
        print('         >>>adauga_persoana: id_persoana, nume, adresa')
        print('         >>>modifica_poersoana: id_persoana, nume_nou, adresa_noua')
        print('         >>>sterge_persoana_dupa id: id_persoana')
        print('         >>>cauta_persoana_dupa_id: id_persoana')
        print('         >>>generare_persoane: nr')
        print('         >>>print_persoane\n')
        print('         >>>adauga_eveniment: id_persoana, data, timp, descriere')
        print('         >>>modifica_eveniment: id_persoana, data_noua, timp_noua, descriere_noua')
        print('         >>>sterge_evenimente_dupa_id: id_eveniment')
        print('         >>>cauta_evemniment_dupa_id: id_eveniment')
        print('         >>>generare_evenimente: nr')
        print('         >>>print_evenimente\n')
        print('         >>>inscrie_persoana_la_eveniment: id_inscriere, id_persoana, id_eveniment')
        print('         >>>print_inscrieri')
        print('         >>>lista_de_evenimente_ordonate_alfabetic: id_persoana')
        print('         >>>lista_de_evenimente_ordonate_dupa_data: id_persoana')
        print('         >>>persoane_participante_la_cele_mai_multe_evenimente')
        print('         >>>primele_20%_evenimente_cu_cei_mai_mulți_participanți')
        print('         >>>lista_de_persoane_ordonate_alfabetic: id_eveniment')
        print('         >>>exit')

# -----------------------------------------------------Persoane-----------------------------------------------------

    def __ui_adauga_persoana(self):
        if len(self.__params) != 3:
            print("Numar parametri invalid!")
            return
        id_persoana = int(self.__params[0])
        nume = self.__params[1]
        adresa = self.__params[2]
        self.__service_persoana.addPerrson(id_persoana, nume, adresa)
        print("Persoana a fost adaugata cu succes")

    def __ui_sterge_persoana_dupa_id(self):
        if len(self.__params) != 1:
            print("Numar parametri invalid!")
            return
        self.__service_inscriere.deletePerson(int(self.__params[0]))
        print("Persoana a fost stearsa cu succes")

    def __ui_modifica_persoana(self):
        if len(self.__params) != 3:
            print("Numar parametri invalid!")
            return
        self.__service_persoana.modifyPerson(int(self.__params[0]), self.__params[1], self.__params[2])
        print("Persoana a fost modificata cu succes")

    def __ui_cauta_persoana_dupa_id(self):
        if len(self.__params) != 1:
            print("Numar parametri invalid!")
            return
        print(self.__service_persoana.findPerson(int(self.__params[0])))

    def __ui_print_persoane(self):
        if len(self.__params) != 0:
            print("Numar parametri invalid!")
            return
        persoane = self.__service_persoana.getAllPeople()
        if len(persoane) == 0:
            print("Nu exista persoane inregistrate")
            return
        for persoana in persoane:
            print(persoana)

    def __ui_generare_persoane(self):
        if len(self.__params) != 1:
            print("Numar parametri invalid!")
            return
        self.__generator_persoane.generate_people(int(self.__params[0]))
        print('Cele', self.__params[0], 'de persoane generate cu succes')

# -----------------------------------------------------EVENIMENTE----------------------------------------------------

    def __ui_adauga_eveniment(self):
        if len(self.__params) != 4:
            print("numar parametri invalid!")
            return
        id_eveniment = int(self.__params[0])
        data = self.__params[1]
        timp = self.__params[2]
        descriere = self.__params[3]
        self.__service_eveniment.addEvent(id_eveniment, data, timp, descriere)
        print("Evenimentul a fost adaugat cu succes")

    def __ui_sterge_eveniment_dupa_id(self):
        if len(self.__params) != 1:
            print("numar parametri invalid!")
            return
        id_eveniment = int(self.__params[0])
        self.__service_inscriere.deleteEvent(id_eveniment)
        print("Evenimentul a fost sters cu succes")

    def __ui_modifica_eveniment(self):
        if len(self.__params) != 4:
            print("numar parametri invalid!")
            return
        id_eveniment = int(self.__params[0])
        data = self.__params[1]
        timp = self.__params[2]
        descriere = self.__params[3]
        self.__service_eveniment.modifyEvent(id_eveniment, data, timp, descriere)
        print("Evenimentul a fost modificat cu succes")

    def __ui_cauta_eveniment_dupa_id(self):
        if len(self.__params) != 1:
            print("numar parametri invalid!")
            return
        id_eveniment = int(self.__params[0])
        print(self.__service_eveniment.findEvent(id_eveniment))

    def __ui_print_evenimente(self):
        if len(self.__params) != 0:
            print("Numar parametri invalid!")
            return
        evenimente = self.__service_eveniment.getAllEvents()
        if len(evenimente) == 0:
            print("Nu exista evenimente inregistrate")
            return
        for eveniment in evenimente:
            print(eveniment)

    def __ui_generare_evenimente(self):
        if len(self.__params) != 1:
            print("Numar parametri invalid!")
            return
        self.__generator_evenimente.generate_events(int(self.__params[0]))
        print('Cele', self.__params[0], 'de evenimente generate cu succes')

# -----------------------------------------------------INSCRIERI-------------------------------------------------------
    def __ui_adauga_inscriere(self):
        if len(self.__params) != 3:
            print("numar parametri invalid!")
            return
        id_inscriere = int(self.__params[0])
        id_persoana = int(self.__params[1])
        id_eveniment = int(self.__params[2])
        self.__service_inscriere.addSignUp(id_inscriere, id_persoana, id_eveniment)
        print("Persoana inscrisa cu succes")

    def __ui_print_inscrieri(self):
        if len(self.__params) != 0:
            print("Numar parametri invalid!")
            return
        inscrieri = self.__service_inscriere.getAllSignUps()
        if len(inscrieri) == 0:
            print("Nu exista inscrieri inregistrate")
            return
        for inscriere in inscrieri:
            print(inscriere)

    def __ui_lista_de_evenimente_ordonate_alfacebtic(self):
        if len(self.__params) != 1:
            print("Numar parametri invalid!")
            return
        lista_sortata = self.__service_inscriere.getEventsList_ofAPerson_orderByDescription(int(
            self.__params[0]))
        if lista_sortata == []:
            print('Persoana nu participa la nici un eveniment')
        else:
            for eveniment in lista_sortata:
                print(eveniment)

    def __ui_lista_de_evenimente_ordonate_dupa_data(self):
        if len(self.__params) != 1:
            print("Numar parametri invalid!")
            return
        lista_sortata = self.__service_inscriere.get_events_list_of_a_person_order_by_date(int(
            self.__params[0]))
        if lista_sortata == []:
            print('Persoana nu participa la nici un eveniment')
        else:
            for eveniment in lista_sortata:
                print(eveniment)

    def __ui_persoane_participante_la_cele_mai_multe_evenimente(self):
        if len(self.__params) != 0:
            print("Numar parametri invalid!")
            return
        lista_DTO = self.__service_inscriere.get_the_person_signUp_at_the_most_events()
        for element_DTO in lista_DTO:
            print(element_DTO)

    def __ui_evenimente_cu_cele_mai_multe_persoane(self):
        if len(self.__params) != 0:
            print("Numar parametri invalid!")
            return
        lista_DTO = self.__service_inscriere.get_the_events_with_the_most_people()
        if len(lista_DTO) == 0:
            print("20% din evenimentele introduse reprezinta mai putin de un eveniment")
        for element_DTO in lista_DTO:
            print(element_DTO)

    def __ui_lista_de_persoane_ordonate_alfabetic(self):
        if len(self.__params) != 1:
            print("Numar parametri invalid!")
            return
        lista_sortata = self.__service_inscriere.get_people_order_by_name(int(
            self.__params[0]))
        if lista_sortata == []:
            print('Evenimentul nu are persoane inscrise')
        else:
            for persoana in lista_sortata:
                print(persoana)

# -----------------------------------------------------RUN UI-------------------------------------------------------

    def run_ui(self):
        while True:
            self.__print_menu()
            comanda = input(">>>")
            comanda = comanda.strip()
            if comanda == "":
                continue
            if comanda == "exit":
                return
            parti = comanda.split(': ')
            nume_comanda = parti[0]
            if len(parti) > 1:
                parametrii = parti[1].split(', ')
                self.__params = parametrii
            else:
                self.__params = []
            if nume_comanda in self.__comenzi:
                try:
                    self.__comenzi[nume_comanda]()
                except ValueError as ve:
                    print(ve)
                except ValidatorError as ve:
                    print(ve)
                except RepositoryError as re:
                    print(re)
            else:
                print("comanda invalida!")
