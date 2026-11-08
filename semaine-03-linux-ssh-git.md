Semaine 3 — Linux, SSH, Git

Travail fait en local, sous Windows avec WSL Ubuntu, sans VPS.

Nginx

Un serveur web : il reçoit les visiteurs, sert lui-même les fichiers simples, transmet le reste à Django et note chaque visite dans ses logs (/var/log/nginx/access.log).

Clé SSH

Une paire de clés pour se connecter sans mot de passe :

~/.ssh/id_ed25519 : clé privée, ne quitte jamais ma machine ;
~/.ssh/id_ed25519.pub : clé publique, je peux la donner (à GitHub, à un serveur).

À la connexion, ma machine prouve qu'elle possède la clé privée sans jamais l'envoyer.

bash
ssh-keygen -t ed25519 -C "aladjkamel@gmail.com"
ssh -T git@github.com

À la première connexion, l'empreinte du serveur est vérifiée puis enregistrée dans ~/.ssh/known_hosts.

Git
Dépôt cloné en SSH dans Ubuntu : git@github.com:KamSylla229/backend90.git
Cycle : git add → git commit -m "..." → git push
Bon message de commit : une ligne, un verbe, ce qui change.
Leçons du terminal
Un espace sépare les arguments : ls ~/.ssh et non ls ~/ .ssh.
Les fichiers qui commencent par . sont cachés : ls -a.
Le disque Windows est visible depuis Ubuntu dans /mnt/c/.
Fins de ligne : Windows (CRLF) et Linux (LF) peuvent créer de faux changements dans git diff.
Reste à faire
Page Nginx ouverte depuis mon téléphone
Ma requête retrouvée dans les logs Nginx
Ports ouverts vérifiés avec sudo ss -tlnp
Atteindre 10 commits propres