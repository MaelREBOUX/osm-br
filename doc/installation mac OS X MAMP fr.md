
# Installation de la partie API sous Mac OS X et MAMP

MAMP (https://www.mamp.info/) est un paquetage complet de logiciels serveurs (apache php mysql) qui permet de disposer d'un environnement serveur sans procéder à aucune installation "en dur" sur le système d'exploitation.

La seule difficulté réside à installer les bibliothèques complémentaires Python pour nécessaires comme Flask.

## Installation des logiciels requis

### MAMP

Télécharger et installer MAMP : https://www.mamp.info/


### Homebrew + python + flask

Homebrew installe les paquets dans leurs propres répertoires puis ensuite fait un lien symbolique dans /usr/local/ permettant ainsi leur usage par le système d'exploitation.

Ouvrir un Terminal. Installer Brew.

```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

Installer python
```
brew install python
```

Installer Flask
```
pip install Flask
```

Tester
```
python
>>> import flask
>>>
```
Tout se passe bien si rien ne s'affiche. ctrl + D pour sortir de la console python


### Modifier le python de MAMP

/!\ pb : le python utilisé par MAMP ne voit pas / ne connaît pas les librairies utilisées / installées dans le python de OS X. Donc, à ce stade, il ne voit pas flask.
On y pare en faisant des liens symboliques vers les "packages" nécessaires.

**rajout des librairies python OS X à MAMP**
```
cd /Applications/MAMP/Library/lib/python2.7
ln -s /usr/local/lib/python2.7/site-packages/flask/ flask
ln -s /usr/local/lib/python2.7/site-packages/jinja2/ jinja2
ln -s /usr/local/lib/python2.7/site-packages/markupsafe/ markupsafe
ln -s /usr/local/lib/python2.7/site-packages/itsdangerous.py itsdangerous.py
ln -s /usr/local/lib/python2.7/site-packages/itsdangerous.pyc itsdangerous.pyc
```


## git clone + configuration apache

Nous allons installer le répertoire du site web dans un répertoire "Sites" de l'utilisateur OS X. Soit sous /Users/{moi}/Sites/htdocs/

Ouvrir un Terminal.
```
cd /Users/{moi}/Sites/htdocs/
git clone https://github.com/MaelREBOUX/osm-br
```

Modifier le fichier global de apache pour rajouter le site osm-br 

```
nano /Applications/MAMP/conf/apache/httpd.conf
```

Tout en bas, rajouter `Include /Users/{moi}/Sites/htdocs/osm-br/web-conf/osm-br.conf`

Ouvrir ensuite osm-br.conf et ajuster les chemins vers les répertoires.

Nous sommes en train de créer un site http://osm-br.local . Il convient donc de modifier le fichier `/etc/hosts` pour "résoudre" les requêtes et pointer sur le serveur web local.

```
nano /etc/hosts/
```

Rajouter `127.0.0.1       osm-br.local`

Relancer le apache de MAMP pour charger le nouveau site. Soit par l'interface de MAMP, soit par cette ligne de commande.

```/Applications/MAMP/Library/bin/apachectl restart```

Ouvrir un navigateur et aller à http://osm-br.local

Tester également http://osm-br.local/api/kerofis/infos pour voir si la partie API écrite en python répond bien par un JSON.

```
{ "infos": { "name": "kerofis database", "last_file_import": "2016-02-09" } }
```



 



