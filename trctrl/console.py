import argparse

from .lib import commands

def pprint(obj):
    if isinstance(obj, list):
        return "\n".join([pprint(e) for e in obj])
    elif isinstance(obj, dict):
        return ", ".join(["{}: {}".format(k,v) for k,v in obj.items()])

def setup():
    parser = argparse.ArgumentParser("Transmission ctrl.")

    subparsers = parser.add_subparsers(dest='cmd')

    ls = subparsers.add_parser('list', help="List torrents")
    ls.add_argument('-s', '--status', action='store', default='all')

    show = subparsers.add_parser('show', help="Show information about specific torrent.")
    add = subparsers.add_parser('add', help="Add torrent to list.")
    add.add_argument('torrent')

    pause = subparsers.add_parser('pause', help="Pause torrent.")
    pause.add_argument('identifier')

    start = subparsers.add_parser('start', help="Pause torrent.")
    start.add_argument('identifier')

    delete = subparsers.add_parser('delete', help="Delete torrent.")
    update = subparsers.add_parser('update', help="Update torrent.")

    return parser.parse_args()

def run(args):
    res = None
    if args.cmd == 'list':
        res = pprint(commands.list_torrents(args.status))
    elif args.cmd == 'pause':
        commands.pause_torrents(args.identifier)
    elif args.cmd == 'start':
        commands.start_torrents(args.identifier)
    elif args.cmd == 'add':
        res = pprint(commands.add_torrent(args.torrent))

    print(res)

if __name__ == '__main__':
    args = setup()
    run(args)
