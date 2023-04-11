# Music Hunter

[![PyPI license](https://img.shields.io/pypi/l/instauto)](https://pypi.python.org/project/instauto/)

This is a crawler intended to crawl Discogs to discover music based on certain parameters.

## Installation
Create a virtual environment and install dependencies:

```sh
$ python -m venv env
$ . env/bin/activate
$ poetry install
```

## Quickstart
```
$ poetry run discogs --style "Goa Trance" --type release --genre Electronic --country netherlands -v
```

This will find all the albums matching this criteria:

```
INFO:Discogs Crawler -> :Type: Release
INFO:Discogs Crawler -> :ID: 2404570
INFO:Discogs Crawler -> :Title: Various - BooM! Records Promo
INFO:Discogs Crawler -> :Formats: [{'name': 'CD', 'qty': '1', 'descriptions': ['Compilation', 'Promo']}]
INFO:Discogs Crawler -> :Tracklist:
INFO:Discogs Crawler -> :-----------------------------
INFO:Discogs Crawler -> :	1: Boom Shakra (8:22)
INFO:Discogs Crawler -> :	2: Enter The Door (7:01)
INFO:Discogs Crawler -> :	3: Exiter (10:40)
INFO:Discogs Crawler -> :	4: One More For M.A.D. (6:28)
INFO:Discogs Crawler -> :	5: Disclosure (7:46)
INFO:Discogs Crawler -> :	6: Hypersonic (8:28)
INFO:Discogs Crawler -> :	7: Freak Out (7:40)
INFO:Discogs Crawler -> :	8: You're A Moonlander Mate (7:54)
INFO:Discogs Crawler -> :	9: Strange World (8:07)
INFO:Discogs Crawler -> :-----------------------------
INFO:Discogs Crawler -> :Genres: Electronic
INFO:Discogs Crawler -> :Styles: Goa Trance, Acid, Psy-Trance
INFO:Discogs Crawler -> :Artists: Various
INFO:Discogs Crawler -> :Country: Netherlands
INFO:Discogs Crawler -> :==============================
```

# ToDo

- [ ] Finish models
- [ ] Add loggers for artist, label and master entities
- [ ] Add tests