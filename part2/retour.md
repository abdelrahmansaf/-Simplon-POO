
# Part 2

La norme ! certain fichier finissent par \r\n ou \r au lieu de \n
C'est pas parfait, Ca fonctionne, encore quelque petite erreurs, mais dans l'ensemble c'est bien.
Essaye de faire plus de petite fonction et d'eviter de repeter/copier-coller ton propre code.


## Army

Ligne 36 on prefere comparer les type de classe avec `is` et le type d'une instance avec `isinstance`. (ici `cls is 
Warrior`).

Tres bien la methods `inWarlord` !
`moveUnits` est pas tres propre Mais tu peux etre fier de toi !!!

## Battlefield

Beaucoup de repetition de code, Je suis sur que tu peux decouper cela en methods plus courte et plus lisible (et 
reutilisable).

## Defender & Warlord 

Pourquoi le Warlod redefini un etat du Defender ? (self.defense)

## Healer

La methods `heal` est redeclarer a plein d'endroit. Comment peut on changer le code ppour eviter cela ? (2 
possibiliter tres simple).

