#!/usr/bin/env python3

import argparse
import subprocess
import requests
import re
import os


# arguments
# ##################################################

# check if output file already exists
# if not check if dir does already exist
def validate_output_file(p, filepath) -> str:
    abspath = os.path.abspath(filepath)
    dirname = os.path.dirname(abspath)
    if os.path.isfile(abspath):
        p.error(f'The file {filepath} does already exist.')
    elif not os.path.exists(dirname):
        p.error(f'The directory {dirname} does not exist.')
    else:
        return filepath


def validate_time_string(p, time_string):
    time_string_regex = re.compile(r'^[0-9]+:[0-5][0-9]:[0-5][0-9]$')
    if not time_string_regex.match(time_string):
        p.error(f'Time could not be parsed: {time_string}')
    return time_string


def arguments():
    parser = argparse.ArgumentParser(description="Download lectures")
    parser.add_argument(
        '-u',
        dest='url',
        required=True,
        help='stream playlist url',
        metavar='URL',
        type=str
    )
    parser.add_argument(
        '-o',
        dest='output_file',
        required=True,
        help='output file name',
        metavar='OUT_FILE',
        type=lambda x: validate_output_file(parser, x),
    )
    parser.add_argument(
        '-t',
        dest='timeout',
        required=False,
        help='record time',
        metavar='TIME',
        type=lambda x: validate_time_string(parser, x),
    )
    return parser.parse_args()


# Playlist extraction
# ##################################################

def extract_playlist_links(url) -> list:
    html = _fetch_html(url)
    regex = re.compile(r'\bhttps://.*.m3u8\b')
    lst = regex.findall(html)
    return lst


def _fetch_html(url) -> str:
    if not (url.startswith('http://') or url.startswith('https://')):
        url = 'http://' + url
    response = requests.get(url)
    return response.text


# command line interaction
# ##################################################


def select_playlist(playlists) -> str:
    for i, playlist in enumerate(playlists):
        print(f'[{i + 1}] {playlist}')

    n = -1
    while n not in range(1, len(playlists) + 1):
        try:
            n = int(input('[!] select stream: '))
        except:
            n = -1
    return playlists[n]


# main
# ##################################################

def main():
    args = arguments()
    playlists = extract_playlist_links(args.url)
    if len(playlists) == 0:
        print('[i] no stream found')
        exit(0)

    playlist_url = playlists[0]
    if len(playlists) > 1:
        print('[i] more than one stream found. select one')
        playlist_url = select_playlist(playlists)

    time_string = f' -t {args.timeout}' if args.timeout else ""
    command = f'ffmpeg {time_string} -i "{playlist_url}" -codec copy {args.output_file}'
    subprocess.call(command, shell=True)


if __name__ == '__main__':
    main()
