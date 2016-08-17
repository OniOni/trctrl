import argparse

from .lib import commands

def setup():
    parser = argparse.ArgumentParser("Transmission ctrl.")

    subparsers = parser.add_subparsers(dest='cmd')

    ls = subparsers.add_parser('list', help="List torrents")
    show = subparsers.add_parser('show', help="Show information about specific torrent.")
    add = subparsers.add_parser('add', help="Add torrent to list.")
    pause = subparsers.add_parser('pause', help="Pause torrent.")
    delete = subparsers.add_parser('delete', help="Delete torrent.")
    update = subparsers.add_parser('update', help="Update torrent.")

    return parser.parse_args()

def run(args):
    if args.cmd == 'list':
        print(commands.list())

if __name__ == '__main__':
    args = setup()
    run(args)
