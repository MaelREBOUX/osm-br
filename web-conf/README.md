# configuration du serveur web apache

copier le fichier osm-br dans /etc/apache2/sites-available

sudo cp osm-br /etc/apache2/sites-available

activer le site

sudo a2ensite osm-br.conf
sudo service apache2 reload

Bien entenud, pour un usage local, modifier le fichier /etc/hosts
exemple : 127.0.0.1	osm-br.local

