import logging
import discogs_client
from music_hunter.lib.enums import TypeEnum
from music_hunter.lib.redis import RedisClient
from music_hunter.settings import get_discogs_settings


logging.basicConfig(level=logging.INFO)
_LOGGER = logging.getLogger('Discogs Crawler -> ')


class DiscogsCrawler:
    """ Discogs crawler class """

    __redis = RedisClient()
    __token = get_discogs_settings().token
    __user_agent = get_discogs_settings().user_agent
    
    def __log_release(self, release):
        _LOGGER.info(f'Type: {type(release).__name__}')
        _LOGGER.info(f'ID: {release.id}')
        _LOGGER.info(f'Title: {release.title}')
        _LOGGER.info(f'Formats: {release.formats}')
        _LOGGER.info(f'Tracklist:')
        _LOGGER.info(f'-----------------------------')
        for track in release.tracklist:
            _LOGGER.info(f'\t{track.position}: {track.title} ({track.duration})')
        _LOGGER.info(f'-----------------------------')
        _LOGGER.info(f'Genres: {", ".join(release.genres)}')
        _LOGGER.info(f'Styles: {", ".join(release.styles)}')
        _LOGGER.info(f'Artists: {", ".join((a.name for a in release.artists))}')
        _LOGGER.info(f'Country: {release.country}')
        _LOGGER.info('==============================')

    def search(self, query, type, style, genre, country, verbose: bool = False):
        params = {
            "query": query,
            "type": type,
        }
        if type == TypeEnum.RELEASE.value or type == TypeEnum.MASTER.value or type:
            params.update({"country": country, "style": style, "genre": genre})
        
        client = discogs_client.Client(self.__user_agent, user_token=self.__token)
        for item in client.search(**params):
            if not self.__redis.conn.exists(f'{type}:{item.id}'):
                self.__redis.conn.set(f'{type}:{item.id}', 1)
            if verbose:
                if type == TypeEnum.RELEASE.value:
                    self.__log_release(item)

