# Semaine 2 — HTTP et HTTPS

## Le principe
Le client envoie une **requête**, le serveur renvoie une **réponse**. Toujours dans ce sens.

Une requête = un verbe + une adresse + des en-têtes (+ parfois un corps).
Une réponse = un code de statut + des en-têtes + un corps (la page, du JSON...).

## Les verbes
| Verbe | Rôle |
|---|---|
| GET | Lire une ressource |
| POST | Créer une ressource |
| PUT / PATCH | Modifier (entièrement / en partie) |
| DELETE | Supprimer |

## Les codes de statut
| Famille | Sens | Exemples |
|---|---|---|
| 2xx | Succès | 200 OK, 201 Created, 204 No Content |
| 3xx | Redirection | 301 déplacé définitivement, 302 temporairement |
| 4xx | Erreur du **client** | 400, 401 non connecté, 403 interdit, 404 introuvable |
| 5xx | Erreur du **serveur** | 500 erreur interne, 502 Bad Gateway, 503 indisponible |

Règle simple : **4xx = c'est la faute de la requête, 5xx = c'est la faute du serveur.**

## Les en-têtes à connaître
- `Host` : le site demandé.
- `Content-Type` : le format du contenu (text/html, application/json).
- `Authorization` : la preuve d'identité (jeton).
- `Location` : où aller en cas de redirection.
- `Set-Cookie` : le serveur demande au navigateur de garder une info (ex. une session).
- `Cookie` : le navigateur renvoie cette info à chaque requête.

## HTTPS
- **Protège** : le contenu échangé (chiffré) et l'identité du domaine (certificat).
- **Ne protège pas** : contre un site malhonnête. Le cadenas dit « tu parles bien à ce domaine », pas « ce domaine est fiable ».

## Mes requêtes curl
⚠️ Dans PowerShell, taper `curl.exe` (et non `curl`, qui lance une autre commande).

| Commande | Code prédit | Code obtenu |
|---|---|---|
| `curl.exe -I https://example.com` | 200OK | 200OK |
| `curl.exe -I http://google.com` |  301 | 301 |
| `curl.exe -I https://example.com/page-inexistante` | 404 | 404 |

## Honnêteté
Je n'ai pas terminé tous les exercices de vérification de cette semaine.
À reprendre : ceux les codes et comprendre chacun leur interprétations.