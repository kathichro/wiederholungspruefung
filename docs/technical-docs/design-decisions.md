---
title: Design Decisions
parent: Technical Docs
nav_order: 5
---

[ Kathi]
{: .label }

# [Design decisions]
{: .no_toc }

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

## 01: Benutzung von Flask-Login um User-Accounts hinzuzufügen

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 26-Sep-2023

### Problem statement

Soll ich Flask-HTTPAuth, Flask-Login, Flask-Praetorian oder Flask-User verwenden, um Useraccounts samt Verifizierung und Registrierung in meine To-Do WebApp zu implementieren?

Für diese Webanwendung verwende ich Python und Flask. Vieles an Code war bereits vorgegeben. Meine Aufgabe ist es, die bereits vorhandene Applikation, um User-handling und eine API zu erweitern. 

Deshalb werde ich während der Bearbeitung vermutlich:

+ Mehrere Ansätze versuchen, um das User-handling erfolgreich zu implementieren

+ Den bereits vorhandenen Code teilweise verändern


### Decision

Nachdem ich mir alle vier Möglichkeiten angeschaut habe und die Vorteile und Nachteile der jeweiligen Methode abgewägt habe, habe ich mich dafür entschieden, Flask-Login zu verwenden. Dort war das Kosten-Nutzen-Verhältnis am besten für mich. Da ich mich noch viel mit dem Thema API beschäftigen musste, entschied ich mich für die Variante, über die ich bereits am besten bescheid wusste. Weitere Entscheidungsgründe siehe in der Tabelle.

### Regarded options

Es gab wie bereits beschrieben, vier Möglichkeiten zu Auswahl.
In der Tabelle habe ich beschrieben, wie ich zu meinem Ergebnis gekommen bin, Flask-Login zu verwenden:


| Flask-Erweiterung | Know-How | Komplexität | Entscheidung |

| :-: | :-: | :-: | :-: |

| **Flask-HTTPAuth** | Kein Vorwissen, ich habe davon aber schonmal gehört | Die Vorgehensweise war verständlich, allerdings gibt es dort viele Wege (basic, digest, token authentication) die Erweiterung zu implemetieren | ❌
Ich habe mich gegen diese Anwendung entschieden, da ich mir unsicher war, welcher Weg am besten für die Applikation gewesen wäre und ich darüber auch noch kein Vorwissen hatte |

| **Flask-Login** | Vorwissen durch das vorherige Projekt bereits vorhanden, in vielen Tutorials wird damit gearbeitet | Für mich am verständlichsten, weil ich während der Einarbeitung in Flask und Webseitenerstellung schon von alleine viel darüber gesehen habe | ✔️
Da ich in dieser Flask-Erweiterung bereits über Vorwissen beherrschte und für mich auch die Anleitung in der verlinkten Seite der PowerPoint am verständlichsten war |

| **Flask- Praetorian** | Kein Vorwissen vorhanden und auch noch nicht davon gehört | Wirkte für mich am Komplextesten, da viel (unbekannter) code benötigt wurde, um diese Methode zu implementieren | ❌
Diese Methode wäre für mich als letztes in Frage gekommen, weil ich mir für diese Erweiterung am meisten Arbeit bedeutet hätte und mich dies in meinem Zeitplan verlangsamt hätte |

| **Flask-User** | Etwas Vorwissen durch das vorherige Projekt vorhanden | Erforderte für mich mehr Einarbeitungszeit als Flask-Login, weil die Übersichtlichkeit und Verständlichkeit auf der verlinkten Seite nicht so verständlich war und ich mir dazu noch einige extra Tutorials angucken musste, um die | ❌
Ich habe mich dagegen entschieden, weil ich über die Flask-Login Methode mehr wusste und auch mit dem Tutorial davon besser arbeiten konnte. Hätte ich die Implementation aber mit Flask-Login nicht hinbekommen, wäre Flask-User meine zweite Wahl gewesen |

---

## 01: Verwendung von Flask_RESTful um die API zu implementieren

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 05-Okt-2023

### Problem statement

[Describe the problem to be solved or the goal to be achieved. Include relevant context information.]

### Decision

[Describe **which** design decision was taken for **what reason** and by **whom**.]

### Regarded options

[Describe any possible design decision that will solve the problem. Assess these options, e.g., via a simple pro/con list.]

---
