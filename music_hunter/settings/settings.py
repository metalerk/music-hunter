import json
from music_hunter.dataclasses.settings import (
    DiscogsSettings,
    RedisSettings,
)
from music_hunter.cache import SettingsCache


def get_settings(dataclass, section: str, reload: bool = False):
    cache = SettingsCache()
    if not cache.data or reload:
        with open('settings.json', 'r') as sf:
            settings = json.load(sf)
        return dataclass(**settings.get(section))
    return dataclass(**cache.data.get(section))

def get_redis_settings(reload: bool = False):
    return get_settings(RedisSettings, 'redis', reload=reload)

def get_discogs_settings(reload: bool = False):
    return get_settings(DiscogsSettings, 'discogs', reload=reload)
