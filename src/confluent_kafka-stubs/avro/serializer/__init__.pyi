class SerializerError(Exception):
    message: str
    def __init__(self, message: str) -> None: ...

class KeySerializerError(SerializerError): ...
class ValueSerializerError(SerializerError): ...
