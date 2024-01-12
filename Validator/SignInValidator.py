from Errors.Exeptions import ValidatorError


class SignInValidator(object):
    def __init__(self):
        pass

    """
        The class responsible for validating registrations
        """

    def validate(self, signIn):
        """
              validate a registration
              :param signIn- Registration
              raise ValueError: - if the id_id of an entry is <0 the string "invalid entry id!\n" will be concatenated
                                  to the string of errors
            """
        err = ""
        if len(str(signIn.get_id_signUp())) != 4:
            err += "Invalid Id!\n"

        if len(err) > 0:
            raise ValidatorError(err)

    def validate_id(self, idd):
        if len(str(idd)) != 4:
            raise ValidatorError("Invalid Id!\n")
