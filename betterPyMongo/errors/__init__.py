class InvalidCollectionError(Exception):
    pass


class MongoSaveError(Exception):
    pass


class MongoRepeatedUniqueKey(Exception):
    pass


class InvalidDataType(Exception):
    pass


class InvalidDataPassed(Exception):
    pass