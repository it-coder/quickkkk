#!/usr/bin/python3
import signal, time, subprocess, threading, sys, os

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator
from gi.repository import Gtk

APPINDICATOR_ID = 'myappindicator'

signal.signal(signal.SIGINT, signal.SIG_DFL)

base_path = os.path.dirname(os.path.abspath(__file__))

ERR_LOG_PATH = os.path.join(base_path, "ssr-local-gui.log")
ICON_ABS_PATH = os.path.join(base_path, "ssr_icon.png") 
SSR_CONFIG_PATH = os.path.join(base_path,  "ssrconfigfaguo.json")

SSR_RUNNING = False

SSR_STATUS = 'stoped'

SSR_CMD = None


def cb_msg():
    global SSR_RUNNING, SSR_STATUS
    while not SSR_CMD.poll():
        time.sleep(2)
        SSR_RUNNING = True
        SSR_STATUS = 'running'
        print('running')
    else:
        SSR_RUNNING = False
        SSR_STATUS = 'stopped'
        print('stopped')

class MyWindow(Gtk.Window):

    def __init__(self):
        self.window = Gtk.Window.__init__(self, title="ssr gui")
        
        self.set_default_size(180, 75)
        self.set_resizable(False)
        # self.set_decorated(False)

        self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.set_icon_from_file(ICON_ABS_PATH)
        self.add(self.vbox)

        self.box = Gtk.Box(spacing=6)
        self.vbox.pack_start(self.box, False, False, 0)

        self.button1 = Gtk.Button(label="start")
        self.button1.connect("clicked", self.on_button1_clicked)
        self.box.pack_start(self.button1, True, True, 0)

        self.button2 = Gtk.Button(label="stop")
        self.button2.connect("clicked", self.on_button2_clicked)
        self.box.pack_start(self.button2, True, True, 0)

        self.entry = Gtk.Label()
        self.vbox.pack_start(self.entry, False, True, 0)
        self.connect('destroy', self.exit)
        self.init_status()

    def init_status(self):
        self.entry.set_text(SSR_STATUS)

    def late_update(self):
        time.sleep(3)
        self.entry.set_text(SSR_STATUS)

    def on_button1_clicked(self, widget):
        if SSR_RUNNING is True:
            self.entry.set_text('is running')
            return
        
        global SSR_CMD
        SSR_CMD = subprocess.Popen(['ssr-local', '-c', SSR_CONFIG_PATH], stdout=open('/dev/null', 'w'), stderr=open(ERR_LOG_PATH, 'w'))
        self.entry.set_text('staring')
        t = threading.Thread(target=cb_msg)
        t.start()
        self.late_update()

    def on_button2_clicked(self, widget):
        self.entry.set_text('stopping')
        global SSR_CMD
        if SSR_CMD:
            try:
                SSR_CMD.kill()
            except Exception as e:
                print(e)
            self.late_update()

    def exit(self, *arg, **kw):
        print('exit')
        self.destroy()
    


def show_window(w):
    win = MyWindow()
    win.show_all()


def main():
    indicator = appindicator.Indicator.new(APPINDICATOR_ID, ICON_ABS_PATH, appindicator.IndicatorCategory.SYSTEM_SERVICES)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(build_menu())
    indicator.set_menu(build_menu())
    gtk.main()

def build_menu():
    menu = gtk.Menu()

    item_show = gtk.MenuItem('Show')
    item_show.connect('activate', show_window)
    item_quit = gtk.MenuItem('Quit')
    item_quit.connect('activate', quit)
    menu.append(item_show)
    menu.append(item_quit)
    menu.show_all()
    return menu

def quit(source):
    if SSR_CMD:
        try:
            SSR_CMD.kill()
        except Exception as e:
            print(e)
    gtk.main_quit()

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    main()