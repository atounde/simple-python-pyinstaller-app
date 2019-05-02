# Installation de docker 

## Installation selon votre système d'exploitation

- Pour **Ubuntu 18.04** un script d'installation est disponible dans le dossier docker/scripts/docker_install.sh
  - Executer : 
    - sudo chmod 777 docker_install.sh
    - ./docker_install.sh  
    - Redémarrer l'ordinateur
    - docker run hello-world (Si il n'y a aucun soucis de permission, nous pouvons continuer)

- Pour les autres distributions linux et windows rendez-vous au lien suivant:
  - <https://docs.docker.com/install/>

## Mise en place de l'environnement de développement

- Se rendre dans le dossier /btp/docker/

  - Executer la commande :

    - docker build --tag=image_name .

      > **image_name** correspond au nom de l'image
      >
      > Le " . " correspond au chemin du fichier Dockerfile, dans notre cas il se trouve dans le dossier dans lequel nous nous trouvons actuellement   
      >
      > La compilation de l'image sera longue !
      >
      > e.g : docker build --tag=sotracom_baamtu:0.1 .

A la fin de la compilation, vérifier que tout c'est bien déroulé en executant la commande :

- docker images 

Vous devrier voir l'image que nous venons juste de créer dans la liste des images.

La prochaine étape consiste à lancer notre image avec nos différents fichiers addons :

### Lancement de l'image de postgresql version 10 

> docker run -d -e POSTGRES_USER=odoo -e POSTGRES_PASSWORD=odoo -e POSTGRES_DB=postgres --name db postgres:10

### Lancement de notre image Odoo 

> docker run -v /home/tounde/projects/btp/addons:/mnt/btp -v /home/tounde/projects/btools:/mnt/btools -p 8089:8069 --name sotracom_docker --link db:db -t sotracom_baamtu:0.1