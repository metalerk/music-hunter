from redis import Redis
from music_hunter.utils.patterns import Singleton
from music_hunter.settings import (
    get_redis_settings,
)

class RedisClient(Singleton):
    """ Redis Connection class"""
    
    __conn: Redis
    __is_connected: bool = False
    
    def __init__(self) -> None:
        settings = get_redis_settings()
        if not self.__is_connected:
            self.__conn = Redis(
                host=settings.host,
                port=settings.port,
                db=settings.db
            )
            self.__is_connected = True
    
    @property
    def conn(self):
        return self.__conn
    