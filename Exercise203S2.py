class Result:
    def __init__(self, message1, message2=""):
        self.isSuccess = None
        self.message1 = message1
        self.message2 = message2

    def isOK(self):
        return self.isSuccess


class Ok(Result):
    def __init__(self, message1, message2):
        super().__init__(message1, message2)
        self.isSuccess = True


class Error(Result):
    def __init__(self, message1, message2):
        super().__init__(message1, message2)
        self.isSuccess = False

