---
title: Data Model
parent: Technical Docs
nav_order: 3
---

Katharina Chroszczinsky
{: .label }

# Data Model
{: .no_toc }

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

## Data Model before and after

Die rot gekennzeichneten Zeilen habe ich hinzugefügt, um User hinzuzufügen.
Die Tabellen, wo nur blaue Zeilen sind, ist das ursprüngliche Datenmodell.
Das Bild mit den rot gekennzeichneten Zeilen ist also das Datenmodell danch!

![ERM](<../images/ERM richtig (1).gif>)

---

## What I changed compared to the baseline

Um Useraccounts hinzuzufügen, benötigte ich zuerst eine neue Klasse 'User' in db.py. Ein User erhält eine id, welche gleichzeitig als Primärschlüssel dient. Weiterhin hat ein User einen Username und ein Passwort, um sich später zum Einloggen verifizieren zu können. Die beiden Klassen 'List' und 'Todo' haben jeweils die id (Primärschlüssel) von der Klasse 'User' (genannt "user_id") als Fremdschlüssel übergeben bekommen.

Ein User kann keine, ein oder mehrere Todos haben. Ein User kann ebenfalls keine, ein oder mehrere Listen erstellen.
Andersherum ist ein Todo sowie eine Liste **genau einem User** zugeordnet.


Die Zeilen 92 und 93 in der Klasse User in db.py gehören zum Object-Relational Mapping (ORM) System von SQLAlchemie und definieren die Beziehungen zwischen den drei Tabellen 'User', 'List' und 'Todo'. 
Damit wird der Zugriff auf die miteinander verknüpften Daten erleichtert. 
Die Beziehungen in beide Richtungen (von "User" zu "List" und von "User" zu "Todo") werden in meinem Fall durch die db.relationship-Deklarationen in der "User"-Klasse festgelegt. 

![Code db.py](<../images/Screenshot 2023-10-26 131626.png>)

In den Tabellen List und Todo in db.py befindet sich entsprechend jeweils eine Zeile, welche die Beziehung zur Userklasse zurückgibt (Zeile 19 und 33 in db.py).

![db.py List und Todo](<../images/Screenshot 2023-10-26 133744.png>)