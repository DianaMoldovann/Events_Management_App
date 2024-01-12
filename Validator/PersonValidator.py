from Errors.Exeptions import ValidatorError


class PersonValidator(object):
    """
    The class responsible for validation
    """

    def validate(self, person):
        """
              validate a person
              :param persona - Person
              raise ValueError: - if a person's id is <0 the string "invalid id!\n" will be concatenated
                                  to the string of errors
                                - if the name is the string is empty the string "invalid name!\n" will be
                                 concatenated to error string
                                - if the address is empty, the string "invalid address!" will be concatenated to
                                string of errors
            """

        err = ""
        if (person.get_id_person() < 1000):
            err += "Invalid Id!\n"
        parts_nume = person.get_name().split()
        if len(parts_nume) < 2:
            err += "Invalid Name!\n"
        parts_adresa = person.get_address().split()
        if len(parts_adresa) < 3:
            err += "Invalid Address!\n"

        if len(err) > 0:
            raise ValidatorError(err)

    def validate_id(self, idd):
        if len(str(idd)) != 4:
            raise ValidatorError("Invalid Id!\n")
