import subprocess
import os
import time
import libtmux

from pathlib import Path

from rich import print, box
from rich.console import Console
from rich.table import Table

# TODO: random incomplete album
# TODO: random non-FLAC album


# connect to tmux so that we can switch panes
# tmux must be started directly outside the script
try:
    server = libtmux.Server()
    session = server.find_where({ "session_name": "cmus" })
    window = session.attached_window
except:
    print('no tmux running')

console = Console()

console.print('gathering data...', justify='center')

while True:

    # populated by beets_stats.sh
    stats = Path('/Users/stvnrlly/dev/dotfiles/data/stats').read_text().splitlines()
    flac_stats = Path('/Users/stvnrlly/dev/dotfiles/data/flac_stats').read_text().splitlines()
    mp3_stats = Path('/Users/stvnrlly/dev/dotfiles/data/mp3_stats').read_text().splitlines()
    missing = Path('/Users/stvnrlly/dev/dotfiles/data/missing').read_text().splitlines()

    non_format = int(stats[4].split(':')[1].strip()) - (int(flac_stats[4].split(':')[1].strip()) + int(mp3_stats[4].split(':')[1].strip()))

    console.clear()

    table = Table(box=box.SIMPLE)
    table2 = Table(box=box.SIMPLE)

    # print(stats)
    table.add_row('Total albums', stats[4].split(':')[1].strip(), stats[2].split(':')[1].strip())
    table.add_row('FLAC albums', flac_stats[4].split(':')[1].strip(), flac_stats[2].split(':')[1].strip())
    table.add_row('MP3 albums', mp3_stats[4].split(':')[1].strip(), mp3_stats[2].split(':')[1].strip())
    table2.add_row('Incomplete albums', str(len(missing)))
    table2.add_row('Other formats', str(non_format))

    # window.select_pane(2)
    console.print(table, justify='center')
    console.print(table2, justify='center')

    time.sleep(120)