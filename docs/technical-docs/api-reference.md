---
title: API Reference
parent: Technical Docs
nav_order: 4
---

Katharina Chroszczinsky
{: .label }

# API reference
{: .no_toc }

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>


### `def get(self, todo_id=None)`

**Route:** `/api/todos/`, `/api/todos/<int:todo_id>`

**Methods:**  `GET`

**Purpose:** Um Todos im json-Format anzeigen zu lassen 

**Sample output:**

![json von api/todos](<../images/Screenshot 2023-10-27 055539.png>)


![json von api/todos/2](<../images/Screenshot 2023-10-27 055800.png>)

---

### `def post(self)`

**Route:** `/api/todos/`

**Methods:** `POST`

**Purpose:** Um neue Todos zu erstellen

**Sample output:**

id:	2
description:	"Essen kochen"
complete:	false
user_id:	1

---

### `def patch(self, todo_id)`

**Route:** `/api/todos/<int:todo_id>`

**Methods:** `PATCH`

**Purpose:** Um Todos verändern (updaten) zu können

**Sample output:**

id:	2
description:	"Essen für Kinder kochen"
complete:	false
user_id:	1

---

### `def delete(self, todo_id)`

**Route:** `/api/todos/<int:todo_id>`

**Methods:** `DELETE`

**Purpose:** Um Daten von dem User zu löschen

**Sample output:**

Kein Output