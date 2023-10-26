---
title: Data Model
parent: Technical Docs
nav_order: 3
---

Katharina Chroszczinsky
{: .label }

# Data model
{: .no_toc }

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

## Data model before and after

![ERM](<../images/ERM richtig (1).gif>)


# What did I changed compared to the baseline

Um Useraccounts hinzuzufügen, benötigte ich zuerst eine neue Klasse User in db.py. Ein User erhält eine id, welche gleichzeitig als Primärschlüssel dient. Weiterhin hat ein User einen Username und ein Passwort, um sich später zum Einloggen verifizieren zu können. Die beiden Klassen "List" und "Todo" haben jeweils die id (Primärschlüssel) von der Klasse User als "user_id" als Fremdschlüssel übergeben bekommen.

Ein User kann keine, ein oder mehrere Todos haben. Ein User kann ebenfalls keine, ein oder mehrere Listen erstellen.
Anderherum ist ein Todo sowie eine Liste **genau einem User** zugeordnet.


![Code db.py](<../images/Screenshot 2023-10-26 131626.png>)

Die Zeilen 92 und 93 in der Klasse User in db.py gehören zum Object-Relational Mapping (ORM) System von SQLAlchemie und definieren die Beziehungen zwischen den drei Tabellen. 
Damit wird der Zugriff auf die miteinander verknüpften Daten erleichtert. 
Die Beziehungen in beide Richtungen (von "User" zu "List" und von "User" zu "Todo") werden in meinem Fall durch die db.relationship-Deklarationen in der "User"-Klasse festgelegt. 

In den Tabellen List und Todo befindet sich dann entsprechend jeweils eine Zeile, welche die Bezihung zur Userklasse zurückgibt. (Zeile 19 und 33 in db.py)

![db.py List und Todo](<../images/Screenshot 2023-10-26 133744.png>)