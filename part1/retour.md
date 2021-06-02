
# Correction Part1

Deja on a un soucis:
```bash
 ls
__azurite_db_blob_extent__.json  __azurite_db_blob__.json  __azurite_db_queue_extent__.json  __azurite_db_queue__.json
```
Que font ces fichier dans le repository ?


## Warrior

`def damaged(self, dmg):`
Ligne 39 et 40 `elif dmg < 0: dmg = dmg* -1`
Est-ce que cela semble logique.

Si jamais je te tape avec 5 de force et que tu a 10 de defense.
Je te tape avec une valeur de -5 de force. est-ce qu'avec une force negative je te fait mal ?

Par chance comme cela est dans un branch if/elif/else tu n'applique pas les dmg recus.
Mais le code n'est pas logique, tu aurai voulu simplement `return` a la ligne 40.

Ligne 46 a 49. Peut-etre simplifier (regarde la ligne 11).

## Defender

Nickel !

## Fight

Des lignes remplis d'espace a la fin du fichier ce qui n'est pas tres propre.

## Army

Nickel !

## Battlefield

Tu a une erreur dans `simpleFight`
Etat de la list army
Ligne 17 army = [W0, W1, W2, W3], unit_1 = Wx
Ligne 18 army = [W1, W2, W3], unit_1 = W0
ligne 21 army = [W1, W2, W3], unit_1 = W1

Pareil pour l'armee 2.
Les tests passent mais le comportement n'est pas le bon (Puisqu'a chaque fois il y a des soldat qui ne ce bat pas).
