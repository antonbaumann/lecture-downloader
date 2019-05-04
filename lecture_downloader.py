import arguments
import subprocess

import playlist_extraction
import interaction


def main():
    args = arguments.arguments()
    playlists = playlist_extraction.extract_playlist_links(args.url)
    if len(playlists) == 0:
        print('[i] no stream found')
        exit(0)

    playlist_url = playlists[0]
    if len(playlists) > 1:
        print('[i] more than one stream found. select one')
        playlist_url = interaction.select_playlist(playlists)

    command = f'ffmpeg -i "{playlist_url}" -codec copy {args.output_file}'
    subprocess.call(command, shell=True)


if __name__ == '__main__':
    main()
