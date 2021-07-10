class Singleton():
    __instance = None       # This is static attribute of class, not instance attribute

    def __init__(self, name) -> None:
        if Singleton.__instance != None:
            raise Exception("This is a singleton class")
        self.name = name
        Singleton.__instance = self
    
    @staticmethod
    def getInstance(name):
        """This is static method be called by class"""
        if Singleton.__instance == None:
            Singleton(name)
        return Singleton.__instance
    
    def __str__(self) -> str:
        return "{}:{}".format(Singleton.__name__, self.name)