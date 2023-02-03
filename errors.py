class ValidationError(Exception):
    def __init__(self, message):
        self.message = message


class SchemaError(Exception):
    def __init__(self, message):
        self.message = message