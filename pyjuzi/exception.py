class ApiException(Exception):

    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message

    def __str__(self):
        return f"{self.code}:{self.message}"
