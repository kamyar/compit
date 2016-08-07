

class URLInvalid(Exception):
     def __init__(self, value):
         self.value = value
     def __str__(self):
         return repr(self.value)


class RepositoryNotValid(Exception):
     def __init__(self, value):
         self.value = value
     def __str__(self):
         return repr(self.value)
