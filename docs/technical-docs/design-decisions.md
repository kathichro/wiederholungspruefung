---
title: Design Decisions
parent: Technical Docs
nav_order: 5
---

Katharina Chroszczinsky
{: .label }

# Design decisions
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

Zwischen welchen der Flask-Eweiterungen soll ich wählen, um meine RESTful API zu implementieren? Zur Wahl stehen mir Flask-RESTful,Flask-Restless-NG, Flask-RESTX und Flask-smorest.

Jede dieser Erweiterungen hat seine Vor- und Nachteile. Es gilt nun herauszufinden, welche für die Anwendung und für mich am besten ist. 

Um mich für eine Erweiterung zu entscheiden, werde ich:

+ mir den bereits vorgegeben Code genau anschauen und verstehen müssen

+ den generellen Aufbau von APIs verstehen

+ mich mit allen vier vorgeschlagenen Erweiterungen genauer befassen und informieren und Kosten- und Nutzen für mich abwägen


### Decision

Ich benutze für diese Anwendung Flask-RESTful. 

Ich habe mich mit allen vier Methoden auseinandergesetzt und mir den Aufbau angeschaut. Da ich mich generell noch in das Thema API einlesen musste, und ich auch längere Zeit gebraucht habe, den vorgegeben Code zu verstehen, habe ich mich letztendlich für Flask-RESTful entschieden. 

Mit dieser Erweiterung konnte ich am unkompliziertesten die RESTful-API in den Code hinzufügen. Mit den anderen Optionen hätte ich zwar die Möglichkeit gehabt, mehr Funktionen mit einzubinden (siehe Tabelle Regarded options). Allerdings hätte dies dann entsprechend deutlich mehr Zeit und Aufwand für mich bedeutet. Da ich ohnehin schon Probleme hatte, den Aufbau zu verstehen, war es für mich nicht vordergründig wichtig, noch weitere Funktionen zu implementieren, die ich nicht unbedingt benötige.

### Regarded options

| Flask-Erweiterung | Know-How | Komplexität | Entscheidung |
| :-: | :-: | :-: | :-: |
| ** Flask-RESTful ** | Ein wenig Vorwissen vorhanden durch das vorherige Web-Projekt. Da viele Entwickler mit dieser Flask-Erweiterung arbeiten, gibt es viele Möglichkeiten, sich in das Thema einzuarbeiten. | Klare Strukturen für die Erstellung der API. Ressourcen und Endpunkte können vergleichsweise leicht definiert werden. Funktionen können so angepasst werden, dass projektspezifische Anforderungen erfüllt werden. | ✔️ Ich habe mich für diese Variante entschieden, weil diese Erweiterung am unkompliziertesten und am verständlichsten für mich war. Da dies kein großes und komplexes Projekt ist, benötige ich auch nicht viele Erweiterungen, die es teilweise in den anderen gegeben hätte. |
| ** Flask-Restless-NG ** | Kein Vorwissen | Die RESTful-API wird durch bereits vorhandene SQL-Alchemie Datenbanken heraus erstellt. Das Tutorial war gut verständlich geschrieben. | ❌ Da ich mit SQL-Alchemie arbeite, habe ich zwischen dieser Erweiterung und Flask-RESTful abgewägt. Der Einstieg bei Flask-RESTful fiel mir allerdings etwas leicher. Deshalb habe ich mich gegen diese Erweiterung entschieden. |
| ** Flask-RESTX ** | Kein Vorwissen | Der Umfang dieser Erweiterung ist sehr hoch. Der Handhabung mit Swagger erfordert viel Einarbeitungszeit und auch die Konfiguration des response marshalling ist äußerst umfangreich | ❌ Nachdem ich mir das vorgegebene Tutorial durchgesehen hatte, empfand ich die gesamte Erweiterung als äußerst komplex. Da ich bereits die beiden oben genannten Erweiterungen in Betracht gezogen hatte, fiel meine Entscheidung gegen Flask-RESTX recht zügig, da ich bereits gute Alternativen in Betracht gezogen hatte. |
| ** Flask-Smorest ** | Kein Vorwissen. Hier kamen im Tutorial viele Begriffe auf, von denen ich bisher noch nichts gehört habe. | Die Integration sowie Dokumentation der API wird mit OpenAPI und Swagger unterstützt. Durch die vielen möglichen Funktionen wäre ein Overhead gut möglich | ❌ Da mir die Begrifflichkeiten wie OpenAI, ETag und Pagination, sowie auch die dort verwendeten Methoden unbekannt waren, hätte ich sehr viel Zeitaufwand investieren müssen, mich darin einzuarbeiten. |
---
