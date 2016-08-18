from collections import OrderedDict
from . import rpc


def list_torrents(status):
    c = rpc.TrClient()
    res = c.send('torrent-get', {'fields': ['id', 'name', 'status', 'hashString']}).json()

    _all = False
    if status == 'all':
        _all = True
    else:
        code = {
            'running': 4,
            'seeding': 6,
            'stopped': 0
        }[status]

    return [
        OrderedDict([
            ("id", t['id']),
            ("name", t['name']),
            ("status", t['status']),
            ("hash", t['hashString'])
        ]) for t in res['arguments']['torrents']
        if _all or t['status'] == code
    ]

def pause_torrents(ids):
    c = rpc.TrClient()

    if ids == 'all':
        args = None
    else:
        args = {'ids': ids}

    res = c.send('torrent-stop', args)

    return res

def start_torrents(ids):
    c = rpc.TrClient()

    if ids == 'all':
        args = None
    else:
        args = {'ids': ids}

    res = c.send('torrent-start', args)

    return res

def add_torrent(uri):
    c = rpc.TrClient()

    res = c.send('torrent-add', {
        'filename': uri
    }).json()

    print(res)

    if res['result'] == 'success' and 'torrent-added' in res['arguments']:
        t = res['arguments']['torrent-added']
        ret = [
            "Added torrent:",
            OrderedDict([('name', t['name'])])
        ]
    else:
        ret = ['???']

    return ret
