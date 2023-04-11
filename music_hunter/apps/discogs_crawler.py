#!/usr/bin/env python3
import argparse
from music_hunter.lib.crawlers import DiscogsCrawler


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument('--query', help="type of search")
    parser.add_argument('--type', help="type of search")
    parser.add_argument('--style', help="type of search")
    parser.add_argument('--genre', help="type of search")
    parser.add_argument('--country', help="type of search")
    parser.add_argument('-v', action='store_true', default=False)

    args = parser.parse_args()
    
    crawler = DiscogsCrawler()
    crawler.search(
        query=args.query,
        type=args.type,
        style=args.style,
        genre=args.genre,
        country=args.country,
        verbose=args.v
    )
