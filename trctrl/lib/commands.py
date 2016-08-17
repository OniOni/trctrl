from . import rpc


def list(*a, **k):
    c = rpc.TrClient()
    return "\n".join([
        "id: {}, name: {}, status: {}".format(
            t['id'], t['name'], t['status']
        ) for t in c.send(
            'torrent-get', {
                'fields': ['id', 'name', 'status']
            }
        ).json()['arguments']['torrents']
    ])
