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
__version__ = "2.0"
__date__ = "2020/11/10"
__maintainer__ = "Cyrille BIOT <cyrille@cbiot.fr>"
__email__ = "cyrille@cbiot.fr"
__status__ = "Devel"
"""

import sys, string
from random import choice
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GdkPixbuf

class MyWindow(Gtk.Window):

    # a window
    def __init__(self, app):

        Gtk.Window.__init__(self, title="Password Generator", application=app)
        self.set_icon_from_file("apropos.png")
        self.set_default_size(300, 300)
        self.set_border_width(10)

        # Qq ajustements
        ad1 = Gtk.Adjustment(0, 0, 50, 5, 10, 0)

        # Presse papier
        self.clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)

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

        # Label pour le mot de passe
        self.label = Gtk.Entry()
        # set the text of the label
        self.label.set_text("Ici le password")
        self.label.set_editable(False)
        self.label.set_name('labelMdp')

        # Création d'un grid
        grid = Gtk.Grid()
        grid.set_column_spacing(6)
        grid.set_row_spacing(6)
        grid.set_row_homogeneous(True)

        # Checkbutton Majuscules
        self.buttonMaj = Gtk.CheckButton()
        self.buttonMaj.set_label("Majuscules")
        self.buttonMaj.connect("toggled", self.toggled_cb, "maj")

        # Checkbutton Minuscules
        self.buttonMin = Gtk.CheckButton()
        self.buttonMin.set_label("Minuscules")
        self.buttonMin.connect("toggled", self.toggled_cb, "min")

        # Checkbutton Chiffres
        self.buttonChif = Gtk.CheckButton()
        self.buttonChif.set_label("Chiffres")
        self.buttonChif.connect("toggled", self.toggled_cb, "chif")

        # Checkbutton Speciaux
        self.buttonSpec = Gtk.CheckButton()
        self.buttonSpec.set_label("Speciaux")
        self.buttonSpec.connect("toggled", self.toggled_cb, "spec")

        # Par défaut, tous les boutons sont actifs
        self.buttonMaj.set_active(True)
        self.buttonMin.set_active(False)
        self.buttonChif.set_active(True)
        self.buttonSpec.set_active(True)

        # Bouton A PROPOS
        buttonAbout = Gtk.Button("A PROPOS")

        # SIGNAL SUR FCT
        buttonAbout.connect("clicked", self.cliquer_sur_bouton_a_propos)

        # Bouton COPIER
        button_copy_text = Gtk.Button(label="Vers le Presse Papier")

        # SIGNAL SUR LE BOUTON
        button_copy_text.connect("clicked", self.copier_texte)

        # Creation d'une grille
        grid.attach(self.buttonMaj, 0, 0, 1, 1)
        grid.attach(self.buttonMin, 0, 1, 1, 1)
        grid.attach(buttonAbout,1,0,2,1)
        grid.attach(self.buttonChif, 0, 2, 1, 1)
        grid.attach(self.buttonSpec, 0, 3, 2, 1)
        grid.attach(button_copy_text,1,2,1,1)
        grid.attach(self.h_scale, 0, 4, 2, 1)
        grid.attach(self.labelScale, 0, 5, 2, 1)
        grid.attach(self.label,0,7,2,1)

        # On ajoute tout cela à la windows
        self.add(grid)

    # Fonction COPIER
    def copier_texte(self, widget):
        print((self.label.get_text()))
        self.clipboard.set_text(self.label.get_text(), -1)

    def cliquer_sur_bouton_a_propos(self, widget):
        """
        Fonction de la Boite de Dialogue About
        :param widget:
        :return:
        """
        # Recuperation n° de version
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

    # CALLBACK POUR LE SCROLL
    def scale_moved(self, event):
        # Synchronisation du label
        self.labelScale.set_text("Longueur password : Valeur de " + str(int(self.h_scale.get_value())) + ".")

        self.label.set_width_chars(self.h_scale.get_value() + 2)

        # Synchronisation du mot de passe
        self.pwdgen()

    # CALLBACK POUR LES CHECK BUTTON
    def toggled_cb(self, button, name):
        # Mise à jour du dictionnaire d'attributs
        if button.get_active():
            self.name = True
        else:
            self.name = False

        # Synchronisation du mot de passe
        self.pwdgen()

    def pwdgen(self):

        # Recup des valeurs des checkbuttons
        # a Mjuscule , b minuscule
        # c Chiffres, d Caractères spéciaux
        # e longueur mot de passe
        a = 1 if self.buttonMaj.get_active() else 0
        b = 1 if self.buttonMin.get_active() else 0
        c = 1 if self.buttonChif.get_active() else 0
        d = 1 if self.buttonSpec.get_active() else 0
        e = str(int(self.h_scale.get_value()))

        # SI aucun paramètre
        if bool(a) is False and bool(b) is False and bool(c) is False and bool(d) is False:
            self.labelScale.set_text("Cocher au moins un case")
        else:
            self.labelScale.set_text("Longueur password : Valeur de " + str(int(self.h_scale.get_value())) + ".")

        # Gestion des paramètres
        modele = ''
        if bool(a) is True:
            modele = modele + string.ascii_uppercase
        if bool(b) is True:
            modele = modele + string.ascii_lowercase
        if bool(c) is True:
            modele = modele + string.digits
        if bool(d) is True:
            modele = modele + string.punctuation

        # Genere et synchronise le mot de passe
        mot_de_passe = ''.join(choice(modele) for i in range(int(e)))
        self.label.set_text(str(mot_de_passe))
        #print(mot_de_passe)

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