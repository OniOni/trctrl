from . import rpc, table

STATUSES = {
    'running': 4,
    'seeding': 6,
    'stopped': 0
}


def list_torrents(status):
    c = rpc.TrClient()
    res = c.send('torrent-get', {
        'fields': ['id', 'name', 'status', 'hashString', 'eta', 'leftUntilDone']
    }).json()

    _all = False
    if status == 'all':
        _all = True
    else:
        code = STATUSES[status]

    t = table.Table("id", "name", "status", "done")
    t.append_rows([
        {'id': t['hashString'], 'name': t['name'], 'status': t['status'], 'done': t['leftUntilDone']}
        for t in res['arguments']['torrents']
        if _all or t['status'] == code
    ])

    return t

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

def info(identifier):
    c = rpc.TrClient()

    res = c.send('torrent-get', {
        'ids': [identifier],
        'fields': ['id', 'name', 'status', 'eta', 'leftUntilDone']
    }).json()

    return [{k: v} for k,v in res['arguments']['torrents'][0].items()]
