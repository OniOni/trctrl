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
    ls.add_argument('-s', '--status', action='store', default='all', choices=[
        'seeding', 'running', 'stopped'
    ])

    show = subparsers.add_parser('show', help="Show information about torrent.")
    show.add_argument('identifier')

    add = subparsers.add_parser('add', help="Add torrent by to list.")
    add.add_argument('torrent', help="File or url.")

    stop = subparsers.add_parser('stop', help="Stop torrent.")
    stop.add_argument('identifier', nargs='+')

    start = subparsers.add_parser('start', help="Start torrent.")
    start.add_argument('identifier', nargs='+')

    delete = subparsers.add_parser('delete', help="Delete torrent.")
    update = subparsers.add_parser('update', help="Update torrent.")

    return parser.parse_args()

def run(args):
    res = None
    if args.cmd == 'list':
        res = pprint(commands.list_torrents(args.status))
    elif args.cmd == 'stop':
        commands.pause_torrents(args.identifier)
    elif args.cmd == 'start':
        commands.start_torrents(args.identifier)
    elif args.cmd == 'add':
        res = pprint(commands.add_torrent(args.torrent))
    elif args.cmd == 'show':
        res = pprint(commands.info(args.identifier))

    print(res)

def main():
    args = setup()
    run(args)

if __name__ == '__main__':
    main()
