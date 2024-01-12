from Errors.Exeptions import ValidatorError


class EventValidator(object):
    """
    The class responsible for validating events
    """

    def validate(self, event):
        """
              validate an event
              :param  event  - Event
              raise ValueError: - if the id of an event does not consist of 4 digits, the string "id
                                  invalid!\n" will be concatenated to the error string
                                - if the date is the string is empty the string "invalid date!\n" will be
                                 concatenated to error string
                                - if the time is the empty string the string "invalid time!" will be concatenated to
                                string of errors
                                - if the description is the empty string, the string "invalid description!\n" will be concatenated to the string
                                 of errors
            """

        err = ""
        if len(str(event.get_id_event())) != 4:
            err += "Invalid id!\n"
        parts_data = event.get_date().split('/')
        if (len(parts_data) != 3) or (len(parts_data[0]) < 1) or (len(parts_data[1]) < 1) or (len(parts_data[2]) != 4) \
                or (int(parts_data[0]) > 31) or (int(parts_data[0]) < 1) or (int(parts_data[1]) > 12) or (
                int(parts_data[1]) < 1) or (int(parts_data[2]) < 1):
            err += "Invalid Date!\n"
        parts_timp = event.get_time().split(':')
        if (len(parts_timp) != 2) or (int(parts_timp[0]) > 23) or (int(parts_timp[0]) > 59):
            err += "Invalid Time!\n"
        if event.get_description() == "":
            err += "Invalid Description!\n"

        if len(err) > 0:
            raise ValidatorError(err)

    def validate_id(self, id):
        if len(str(id)) != 4:
            raise ValidatorError("Invalid Id!\n")
