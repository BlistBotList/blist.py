class BlistException(Exception):
    pass

class UnknownBot(BlistException):
    pass

class InvalidAuthorization(BlistException):
    pass

class UnknownUser(BlistException):
    pass

class InvalidData(BlistException):
    def __init__(self, message):
        self.message = message

class HTTPException(BlistException):
    def __init__(self, response, message):
        self.response = response
        self.status = response.status
        self.message = message