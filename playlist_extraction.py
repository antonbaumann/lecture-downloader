import requests
import re


def extract_playlist_links(url) -> list:
    html = _fetch_html(url)
    regex = re.compile(r'\bhttps://.*playlist.m3u8\b')
    lst = regex.findall(html)
    return lst


def _fetch_html(url) -> str:
    if not (url.startswith('http://') or url.startswith('https://')):
        url = 'http://' + url
    response = requests.get(url)
    return response.text
