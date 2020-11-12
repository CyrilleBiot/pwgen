#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pwgen.py
Utilitaire de création de mot de passe
Aucune utilité, juste pédagogique pou manipuler GTK

  Source : https://github.com/CyrilleBiot/pwgen

__author__ = "Cyrille BIOT <cyrille@cbiot.fr>"
__copyright__ = "Copyleft"
__credits__ = "Cyrille BIOT <cyrille@cbiot.fr>"
__license__ = "GPL"
__version__ = "0.1"
__date__ = "2020/11/10"
__maintainer__ = "Cyrille BIOT <cyrille@cbiot.fr>"
__email__ = "cyrille@cbiot.fr"
__status__ = "Devel"
"""


import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GdkPixbuf
import sys, subprocess


class MyWindow(Gtk.Window):

    # a window
    def __init__(self, app):

        # Création d'un dictionnaire recueillant les arguments passés à pwgen
        self.dictAttributs = {
            "maj": ("True"),
            "min": ("True"),
            "chif": ("True"),
            "spec": ("True")
        }

        Gtk.Window.__init__(self, title="Password Generator", application=app)
        self.set_icon_from_file("apropos.png")
        self.set_default_size(300, 300)
        self.set_border_width(10)

        # Qq ajustements
        ad1 = Gtk.Adjustment(0, 0, 100, 5, 10, 0)


        # Label pour le mot de passe
        self.label = Gtk.Label()
        # set the text of the label
        self.label.set_text("Ici le password")
        self.label.set_name('labelMdp')



        # SCALE horizontal
        self.h_scale = Gtk.Scale(
            orientation=Gtk.Orientation.HORIZONTAL, adjustment=ad1)
        # avec des entiers (no digits)
        self.h_scale.set_digits(0)
        # Dans l'espace du grid
        self.h_scale.set_hexpand(True)
        self.h_scale.set_valign(Gtk.Align.START)

        # SIGNAL DU SCALE
        self.h_scale.connect("value-changed", self.scale_moved)

        # LABEL DU SCALE
        self.labelScale = Gtk.Label()
        self.labelScale.set_text("Déplacer le curseur et générer un mdp...")

        # Création d'un grid
        grid = Gtk.Grid()
        grid.set_column_spacing(6)
        grid.set_row_spacing(6)
        grid.set_row_homogeneous(True)

        # Checkbutton Majuscules
        buttonMaj = Gtk.CheckButton()
        buttonMaj.set_label("Majuscules")
        buttonMaj.connect("toggled", self.toggled_cb, "maj")

        # Checkbutton Minuscules
        buttonMin = Gtk.CheckButton()
        buttonMin.set_label("Minuscules")
        buttonMin.connect("toggled", self.toggled_cb, "min")

        # Checkbutton Chiffres
        buttonChif = Gtk.CheckButton()
        buttonChif.set_label("Chiffres")
        buttonChif.connect("toggled", self.toggled_cb, "chif")

        # Checkbutton Speciaux
        buttonSpec = Gtk.CheckButton()
        buttonSpec.set_label("Speciaux")
        buttonSpec.connect("toggled", self.toggled_cb, "spec")

        # Par défaut, tous les boutons sont actifs
        buttonMaj.set_active(True)
        buttonMin.set_active(True)
        buttonChif.set_active(True)
        buttonSpec.set_active(True)

        # Bouton A PROPOS
        buttonAbout = Gtk.Button("A PROPOS")

        # SIGNAL SUR FCT
        buttonAbout.connect("clicked", self.cliquer_sur_bouton_a_propos)

        # Creation d'une grille
        grid.attach(buttonMaj, 0, 0, 1, 1)
        grid.attach(buttonMin, 0, 1, 1, 1)
        grid.attach(buttonAbout,1,0,2,1)
        grid.attach(buttonChif, 0, 2, 1, 1)
        grid.attach(buttonSpec, 0, 3, 1, 1)
        grid.attach(self.h_scale, 0, 4, 1, 1)
        grid.attach(self.labelScale, 0, 5, 2, 1)
        grid.attach(self.label,0,7,1,1)

        # On ajoute tout cela à la windows
        self.add(grid)

    def cliquer_sur_bouton_a_propos(self, widget):
        """
        Fonction de la Boite de Dialogue About
        :param widget:
        :return:
        """
        # Recuperation n° de version
        print(__doc__)
        lignes = __doc__.split("\n")
        for l in lignes:
            if '__version__' in l:
                version = l[15:-1]
            if '__date__' in l:
                dateGtKBox = l[12:-1]

        authors = ["Cyrille BIOT"]
        documenters = ["Cyrille BIOT"]
        self.dialog = Gtk.AboutDialog()
        logo = GdkPixbuf.Pixbuf.new_from_file("apropos.png")
        if logo != None:
            self.dialog.set_logo(logo)
        else:
            print("A GdkPixbuf Error has occurred.")
        self.dialog.set_name("Gtk.AboutDialog")
        self.dialog.set_version(version)
        self.dialog.set_copyright("(C) 2020 Cyrille BIOT")
        self.dialog.set_comments("pwgen.py.\n\n" \
                                 "[" + dateGtKBox + "]")
        self.dialog.set_license("GNU General Public License (GPL), version 3.\n"
                                "This program is free software: you can redistribute it and/or modify\n"
                                "it under the terms of the GNU General Public License as published by\n"
                                "the Free Software Foundation, either version 3 of the License, or\n"
                                "(at your option) any later version.\n"
                                "\n"
                                "This program is distributed in the hope that it will be useful,\n"
                                "but WITHOUT ANY WARRANTY; without even the implied warranty of\n"
                                "MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the\n"
                                "GNU General Public License for more details.\n"
                                "You should have received a copy of the GNU General Public License\n"
                                "along with this program.  If not, see <https://www.gnu.org/licenses/>\n")
        self.dialog.set_website("https://cbiot.fr")
        self.dialog.set_website_label("cbiot.fr")
        self.dialog.set_website("https://github.com/CyrilleBiot/pwgen")
        self.dialog.set_website_label("GIT pwgen")
        self.dialog.set_authors(authors)
        self.dialog.set_documenters(documenters)
        self.dialog.set_translator_credits("Cyrille BIOT")
        self.dialog.connect("response", self.cliquer_sur_bouton_a_propos_reponse)
        self.dialog.run()

    def cliquer_sur_bouton_a_propos_reponse(self, widget, response):
        """
        Fonction fermant la boite de dialogue About
        :param widget:
        :param response:
        :return:
        """
        self.dialog.destroy()
        self.notebook.set_current_page(0)

    # CALLBACK POUR LE SCROLL
    def scale_moved(self, event):
        # Synchronisation du label
        self.labelScale.set_text("Longueur password : Valeur de " + str(int(self.h_scale.get_value())) + ".")
        # Synchronisation du mot de passe
        self.pwdgen()


    # CALLBACK POUR LES CHECK BUTTON
    def toggled_cb(self, button, name):
        # Mise à jour du dictionnaire d'attributs
        if button.get_active():
            self.dictAttributs[name] = True
        else:
            self.dictAttributs[name] = False
        # Synchronisation du mot de passe
        self.pwdgen()

    def pwdgen(self):

        # Gestion des attributs depuis les données stockées dans le dico
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

        # Gestion de la longueur du mot de passe
        longueur = str(int(self.h_scale.get_value()))

        # On utilise pwgen de la distribution
        cmd = 'pwgen -1 ' + longueur + ' ' + shellMaj + shellMin + shellChif + shellSpec

        # On lance un sous process
        proc = subprocess.Popen( cmd ,  shell=True,  stdout=subprocess.PIPE)

        # Recup de la sortie standard
        output = proc.stdout.read()
        self.label.set_text(str(output)[2:-3])

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