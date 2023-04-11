from music_hunter.utils.patterns import Singleton


class SettingsCache(Singleton):
    """ SettingsCache class """
    
    __data: dict = {}
    
    def __init__(self) -> None:
        return super().__init__()
    
    def set_cache(self, value):
        self.__data = value
    
    @property
    def data(self):
        return self.__data
