import discogs_client
import json
import libtmux
import os
import subprocess
import shutil
import time

from dotenv import dotenv_values
from PIL import Image
from imgcat import imgcat

from rich import print, box
from rich.console import Console
from rich.table import Table
# from rich.rule import Rule

def get_info(status):
    
    info = {}

    for line in status:

        if 'file ' in line:
            info['file'] = ' '.join(line.split(' ')[1:])
        if ' title ' in line:
            info['title'] = ' '.join(line.split(' ')[2:])
        if ' artist ' in line:
            info['artist'] = ' '.join(line.split(' ')[2:])
        if ' album ' in line:
            info['album'] = ' '.join(line.split(' ')[2:])
        if 'originaldate' in line:
            info['year'] = line.split(' ')[2][0:4]
        elif 'date' in line:
            info['year'] = line.split(' ')[2][0:4]
        if ' label ' in line:
            info['label'] = ' '.join(line.split(' ')[2:])
        if 'duration ' in line:
            info['length'] = line.split(' ')[1]
        if 'position ' in line:
            info['position'] = line.split(' ')[1]

    return info

def build_table(info):

    table = Table(box=box.SIMPLE)

    table.add_row('Title', info['title'])
    table.add_row('Artist', info['artist'])
    table.add_row('Album', info['album'])
    table.add_row('Year', info['year'])
    try:
        table.add_row('Label', info['label'])
    except:
        pass

    return table

def find_image(file):
    # get file location
    folder = os.path.dirname(file)

    # look for cover.jpg or cover.png
    if os.path.isfile(folder + '/cover.jpg'):
        image = folder + '/cover.jpg'
    elif os.path.isfile(folder + '/cover.png'):
        image = folder + '/cover.png'
    else:
        image = None
        print('no cover art found')

    return image

def get_album_info(album, artist):
    pass
    # print(album, artist)
    # results = d.search(release_title=album, artist=artist, type='master')
    # print(results.page(1))

def display():

    console.clear()
    
    columns = shutil.get_terminal_size()[0] * 12

    info = get_info(status)
    try:
        image = find_image(info['file'])
        table = build_table(info)

        # doesn't need to be saved to file, but tmux won't
        # display it properly otherwise
        im_file = os.getcwd() + '/art.jpg'
        im = Image.open(image)
        im = im.resize((columns,columns), reducing_gap=2)
        quality = 75
        im.save(im_file, 'JPEG', optimize=True, quality=quality)
        while os.path.getsize(im_file) > 77000:
            quality -= 5
            im.save(im_file, 'JPEG', optimize=True, quality=quality)
        else:
            window.select_pane(1)
            imgcat(open(im_file))
        # imgcat(im)
    except Exception as e:
        # print(Exception, e)
        table = Table(box=box.SIMPLE)
    window.select_pane(1)
    console.print(table, justify='center')
    try:
        get_album_info(info['album'], info['artist'])
    except Exception as e:
        # print(Exception, e)
        pass

    # do some discogs searching
    # TODO: try to avoid running multiple searches for the same album
    try:
        d_search = d.search(artist=info['artist'], title=info['album'])
        owned = False
        for i in d_search:
            if i.id in collection:
                console.print('In collection! [link=https://discogs.com'+i.url+']see release[/link]', justify='center')
                owned = True
        if not owned:
            # TODO: add link to find a copy
            # ----- grab the master release in previous for loop
            # ----- search bandcamp?
            console.print('Not in collection', justify='center')
    except Exception as e:
        pass
        # print(Exception, e)

    window.select_pane(0)

###############################################################
# running starts here
#

config = dotenv_values(".env")

d = discogs_client.Client('stvnrlly/0.1', user_token=config['DISCOGS_TOKEN'])

# connect to tmux so that we can switch panes
# tmux must be started directly outside the script

try:
    server = libtmux.Server()
    session = server.find_where({ "session_name": "cmus" })
    window = session.attached_window
except:
    print('no tmux running')

# grab initial cmus status
status = [line.decode('utf-8') for line in subprocess.check_output(['cmus-remote', '-Q']).splitlines()]

# initialize discogs collection info
collection = {}
with open('./data/discogs.json') as f:
    collection = json.load(f)

# set up rich (used for centering text)
console = Console()

# create initial display
if status[0] == 'status playing':
    display()

# start scrobble counter
listened = 0

while True:

    # check if track changed
    new_status = [line.decode('utf-8') for line in subprocess.check_output(['cmus-remote', '-Q']).splitlines()]

    if status[1] != new_status[1]:
        listened = 0
        status = new_status
        display()
    else:
        listened += 1
        # if listened == 10:
        # TODO: scrobble here

    time.sleep(1)
