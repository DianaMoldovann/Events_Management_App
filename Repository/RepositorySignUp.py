from Errors.Exeptions import RepositoryError


class RepositorySignUp:
    """
        The class created with the responsibility of managing SignUps
    """

    def __init__(self):
        """
        SignUps is a dictionary whose elements are Entities of type SignUp
        """
        self._signUps = {}

    def size(self):
        """
        returns the length of the dictionary of entries
        :return:
        """
        return len(self._signUps)

    def addSignUp(self, signUp):
        """
    Add an entry in the dictionary
        :param signUp: signUp to be added
        :type signUp: signUp
        ; the signUp list is changed by adding the signUp
        :return:
        """
        if signUp.get_id_signUp() in self._signUps:
            raise RepositoryError("There is already a signUp with this id!\n")
        self._signUps[signUp.get_id_signUp()] = signUp

    def findSignUp(self, id_signUp):
        """
        search in signUps, a signUp with the same id
        :return: True - if it finds an entry with the same id
                 False - if it does not find an entry with the same id
        """
        if id_signUp not in self._signUps:
            raise RepositoryError("Signup not found!\n")
        return self._signUps[id_signUp]

    def modifySignUp(self, signUp):
        """
      updated
        :param signUp: Signup
        :return:
        """
        if signUp.get_id_signUp() not in self._signUps:
            raise RepositoryError("SignUp not found!\n")
        self._signUps[signUp.get_id_signUp()] = signUp

    def getAllSignsUps(self):
        """
        Returns a list of all existing signUps
        :rtype: list of Enrollment type objects
        :return:
        """
        r = []
        for id_signUp in self._signUps:
            signUp = self._signUps[id_signUp]
            r.append(signUp)
        return r

    def deleteSignUp(self, id_signUp):
        """
        Delete the signUp with id_signUp_id
        :param id_signUp: int, the id of the entry to be deleted
        :return:
        """
        if id_signUp not in self._signUps:
            raise RepositoryError("Signup not found!\n")
        del self._signUps[id_signUp]
