# Poker

## Description du projet
Génération d'un jeu de poker entre un joueur et 3 IA avec une interface graphique(Tkinter)

## Installation Tkinter
Dans le terminal, lancer la commande:

    pip install tk

Redémarrer votre ide

## Fonctionnalités mises en place

### Python
Création d'une Class Card contenant deux attributs(value et sign):

    Méthode str() pour représenter la string

Création d'une Class Deck qui génére:

    Méthode generate_a_blended_deck(self) pour créer un mélange de jeu de carte aléatoire
    Méthode seed_generator(self) pour générer un seed aléatoire
    Méthode pick_a_card(self) pour piocher une carte aléatoirement

Création d'une Class Player contenant deux attributs(name et hand):

    Méthode draw(self) pour ajouter la carte piocher aléatoirement dans la "main" du joueur
    Méthode showHand(self) pour afficher la main du joueur

Création d'une classe Main:

    Méthode initializa_game() pour mélanger les cartes et les distribuer aux joueurs et à la table
    Méthode new_game() pour lancer une nouvelle partie

### Tkinter

Dans la classe main:
        
    Bouton reloadGame qui appel la méthode new_game
    Bouton buttonSearchSeed qui appel une méthode pour retrouver le jeu de la seed
    Affichage des cartes pour les différents joueurs et la table