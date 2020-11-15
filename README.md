# pwgen

Juste un test pour programmer un utilitaire gtk3 / python

Générer un mot de passe de façon aléatoire

Excuse pour manipuler
  * checkbutton
  * clipboard
  * aboutDialog


## pwgen2
Version réécrite sans appel de programme externe
Utilisation des modules string et random.choice en alternative
Meilleure gestion des labels

### Nécessite les modules python
Gtk, Gdk, GdkPixbuf
sys, random (choice), string

### Screenshoot

![screenshoot](https://cbiot.fr/site/pwgen_2.png)



## pwgen
Version initiale, nécessite 

### Nécessite les modules python
Gtk, Gdk, GdkPixbuf
sys, subprocess

### Dépendances DEBIAN

```
# apt install pwgen
```
### Screenshoot

![screenshoot](https://cbiot.fr/site/pwgen.png)

