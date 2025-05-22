Big Data: VIELE daten

Warum Social Media Analyse?
- Gesellschaftliche Studien
- Vorhersagen (z.B. Öffentliche Meinung, Aktien, etc.)
- Marktsentiment
- Und mehr!

Methoden:
- Automatisiertes API aufrufen zum scrapen von großen Datenmengen (AT Proto -> Blueskys API)
- Datenbanken zum organisierten Speichern großer Datenmengen (DuckDB)
- Auf Big Data spezialisierte Datenbankwerkzeuge, zum schnellen verarbeiten der Daten (DuckDB)
- Textbereinigung (Stopword removal, Stemming -> NLTK)
- Wortkommonalitätsanalyse, und weitere Personen (z.B: Bei Trump wurden oft Elon und Putin erwähnt)
- Visualisierung mit Plotly für interactive Datenvisualisierung
- Sentimentextrahierung, Ratings Bewerten, Engagementanalyse, Gewichtete Analysen (NOCH NICHT IMPLEMENTIERT - WENN ÜBERHAUPT)

Info zur Verarbeitung:
- Datensatz umfasst 4 Monate (1 Jan bis 1 Apr)
- Suchbegriff war einfach "Trump"
- Immer in Tages Schritten wurden die Top 100 Posts gezogen (1-2 Jan, dann 2-3 Jan, dann 3-4 Jan, etc...)

Ergebnisse:
- Wie zu erwarten ist bei dem Suchbegriff "Trump" das am meisten vorkommende Wort "Trump"
- Gefolgt von "Donald", "Musk", "Putin", "Elon"
- Das einzige wirklich beschreibende Wort im Datensatz ist "FUCK" -> Sehr passend UwU

Was ging gut?
- Bluesky hat eine wunderbare Kostenlose API
- DuckDB eignet sich für Data Science und Big Data anwendungen dank Spezialisierung
- NLTK ermöglicht effiziente Satz-Verarbeitung

Was ging nicht so gut?
- Selbst mit moderner und ausführlicher Dokumentation, war das einlesen der gescrapten Posts in die Datenbank ein bisschen Trial-and-Error
- Text schreiben böse, ich nicht mögen :(
- 

