# Dijkstra's Algorithm for Shortest Path Search
## Overview

This Python code implements Dijkstra's algorithm to find the shortest path between two nodes in a weighted graph. The algorithm is defined by three main functions: chemin, actualiser, and graf.

Functions

## chemin(t, s, fin)

This function takes three arguments:

    t: An array of tuples containing the minimum distance, the previous node, and the current node.

    s: Starting node.

    fin: Ending node.
    It returns the shortest path between the starting node and the ending node.

## actualiser(v, t, e, w, y)

This function updates the minimum distance table. It takes five arguments:

    v: List of nodes.

    t: Array of tuples.

    e: Dictionary of edges.

    w: List of all rows in the table.

    y: Index of the current node.
    It returns the updated table, the index of the node with the minimum distance, and this minimum distance.

## graf(s, v, e, fin)

This function implements Dijkstra’s algorithm to find the shortest path between a starting node s and an ending node fin. It takes four arguments:

    s: Starting node.

    v: List of nodes.

    e: Dictionary of edges.

    fin: Ending node.
    It returns the minimum distance between s and fin as well as the shortest path.

Turtle Graphical Interface

A graphical interface is implemented using the turtle module.

## Conclusion

The code returns the minimum distance between two specified nodes along with the shortest path to achieve this distance.
