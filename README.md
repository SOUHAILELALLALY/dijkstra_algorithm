# Algorithme de Dijkstra pour la Recherche du Chemin le Plus Court

## Overview

Ce code Python est une implémentation de l'algorithme de Dijkstra pour trouver le chemin le plus court entre deux nœuds dans un graphe pondéré. L'algorithme est défini par trois fonctions principales : `chemin`, `actualiser`, et `graf`.

## Fonctions

### `chemin(t, s, fin)`

Cette fonction prend trois arguments :

- `t` : Tableau de tuples contenant la distance minimale, le nœud précédent et le nœud actuel.
- `s` : Nœud de départ.
- `fin` : Nœud de fin.

Elle retourne le chemin le plus court entre le nœud de départ et le nœud de fin.

### `actualiser(v, t, e, w, y)`

Cette fonction met à jour la table des distances minimales. Elle prend cinq arguments :

- `v` : Liste des nœuds.
- `t` : Tableau de tuples.
- `e` : Dictionnaire des arêtes.
- `w` : Liste de toutes les lignes de la table.
- `y` : Indice du nœud actuel.

Elle retourne la table mise à jour, l'indice du nœud avec la distance minimale et cette distance minimale.

### `graf(s, v, e, fin)`

Cette fonction implémente l'algorithme de Dijkstra pour trouver le chemin le plus court entre un nœud de départ `s` et un nœud de fin `fin`. Elle prend quatre arguments :

- `s` : Nœud de départ.
- `v` : Liste des nœuds.
- `e` : Dictionnaire des arêtes.
- `fin` : Nœud de fin.

Elle retourne la distance minimale entre `s` et `fin` ainsi que le chemin le plus court.

## Interface Graphique Turtle

Une interface graphique est implémentée avec `turtle`.


## Conclusion

Le code retourne la distance minimale entre deux nœuds spécifiés ainsi que le chemin le plus court pour atteindre cette distance.
