class InvalidCollectionError(Exception):
    pass


class MongoSaveError(Exception):
    pass


class MongoRepeatedUniqueKey(Exception):
    pass