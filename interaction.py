def select_playlist(playlists) -> str:
    for i, playlist in enumerate(playlists):
        print(f'[{i + 1}] {playlist}')

    n = -1
    while n not in range(1, len(playlists) + 1):
        n = input('[!] select stream: ')
    return playlists[n]
