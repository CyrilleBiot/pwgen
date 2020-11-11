#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import sys, subprocess


class MyWindow(Gtk.Window):

    # a window
    def __init__(self, app):

        self.dictAttributs = {
            "maj": ("True"),
            "min": ("True"),
            "chif": ("True"),
            "spec": ("True")
        }

        Gtk.Window.__init__(self, title="Password Generator", application=app)
        self.set_default_size(300, 300)
        self.set_border_width(10)


        # create a label
        self.label = Gtk.Label()
        # set the text of the label
        self.label.set_text("Ici le password")
        self.label.set_name('labelMdp')




        main_layout = Gtk.Grid()
        main_layout.set_column_spacing(6)
        main_layout.set_row_spacing(6)
        main_layout.set_row_homogeneous(True)






        # Majuscules
        buttonMaj = Gtk.CheckButton()
        buttonMaj.set_label("Majuscules")
        buttonMaj.connect("toggled", self.toggled_cb, "maj")

        # Minuscules
        buttonMin = Gtk.CheckButton()
        buttonMin.set_label("Minuscules")
        buttonMin.connect("toggled", self.toggled_cb, "min")

        # Chiffres
        buttonChif = Gtk.CheckButton()
        buttonChif.set_label("Chiffres")
        buttonChif.connect("toggled", self.toggled_cb, "chif")

        # Speciaux
        buttonSpec = Gtk.CheckButton()
        buttonSpec.set_label("Speciaux")
        buttonSpec.connect("toggled", self.toggled_cb, "spec")

        # Par défaut, tous les boutons sont actifs
        buttonMaj.set_active(True)
        buttonMin.set_active(True)
        buttonChif.set_active(True)
        buttonSpec.set_active(True)

        # add the checkbutton to the window
        # Creation d'une grille
        main_layout.attach(buttonMaj, 0, 0, 1, 1)
        main_layout.attach(buttonMin, 0, 1, 1, 1)
        main_layout.attach(buttonChif, 0, 2, 1, 1)
        main_layout.attach(buttonSpec, 0, 3, 1, 1)
        main_layout.attach(self.label,0,4,1,1)

        self.add(main_layout)





    # callback function
    def toggled_cb(self, button, name):
        #print(button.get_active())
        if button.get_active():
            self.dictAttributs[name] = True
        else:
            self.dictAttributs[name] = False
        self.pwdgen()

    def pwdgen(self):
        print(self.dictAttributs)

        if self.dictAttributs["maj"] == True:
            shellMaj = "--capitalize "
        else:
            shellMaj = ""

        if self.dictAttributs["min"] == True:
            shellMin = "--no-capitalize "
        else:
            shellMin = ""

        if self.dictAttributs["chif"] == True:
            shellChif = "-n "
        else:
            shellChif = "-0 "

        if self.dictAttributs["spec"] == True:
            shellSpec = "--symbols "
        else:
            shellSpec = ""

        cmd = 'pwgen -1 14 ' + shellMaj + shellMin + shellChif + shellSpec
        print("cmd : " + cmd)
        proc = subprocess.Popen( cmd ,  shell=True,  stdout=subprocess.PIPE)
        output = proc.stdout.read()
        self.label.set_markup(str(output)[2:-3])


class MyApplication(Gtk.Application):

    def __init__(self):
        Gtk.Application.__init__(self)

    def do_activate(self):
        win = MyWindow(self)
        win.show_all()

    def do_startup(self):
        Gtk.Application.do_startup(self)

app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
