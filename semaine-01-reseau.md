# Semaine 1 — Internet et réseau

## Ce qui se passe quand je tape une URL
1. **DNS** : le navigateur demande l'adresse IP du nom de domaine (comme un annuaire).
2. **Connexion TCP** : il ouvre un canal vers cette IP, sur un port (80 pour HTTP, 443 pour HTTPS).
3. **TLS** : navigateur et serveur se mettent d'accord sur un chiffrement.
4. **Requête** : le navigateur envoie `GET /` avec ses en-têtes.
5. **Réponse** : le serveur renvoie un code (ex. 200) et la page.
6. **Affichage** : le navigateur lit la page et redemande images, CSS et scripts.

## Les notions clés
- **Adresse IP** : l'adresse d'une machine sur le réseau.
- **Port** : la porte d'un service sur cette machine (22 = SSH, 80 = HTTP, 443 = HTTPS).
- **DNS** : traduit un nom (google.com) en adresse IP.
- **TCP** : garantit que les données arrivent complètes et dans l'ordre.

## Mes commandes (Windows PowerShell)
| Commande | À quoi elle sert | Mon résultat |
|---|---|---|
| `nslookup google.com` | Trouver l'IP d'un domaine | [IP trouvée + serveur DNS] |
| `ping 8.8.8.8` | Vérifier qu'une machine répond, mesurer le temps | [temps en ms] |
| `tracert google.com` | Voir les routeurs traversés | [nombre d'étapes] |
| `Test-NetConnection google.com -Port 443` | Vérifier qu'un port est ouvert | [True/False] |

## Diagnostic : un site ne charge pas, où chercher ?
- `nslookup` échoue → problème **DNS**.
- `ping` échoue → machine injoignable ou ping bloqué.
- Port 443 fermé → le **service** ou le **pare-feu**.
- Erreur de certificat → problème **TLS**.
- Code 500 → problème **dans l'application** du serveur.

## Ce que j'ai appris / ce qui reste flou
Les 6 étapes qui s'exécutent lorsqu'on tapee un site sur un navigateur. j'ai également compris que ce n'est pas parcequ'un ping a échoué que le site est blosqué ou a un problème