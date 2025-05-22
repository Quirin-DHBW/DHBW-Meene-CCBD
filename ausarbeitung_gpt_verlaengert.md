## Big Data: VIELE Daten

Der Begriff „Big Data“ bezeichnet riesige Mengen an digitalen Informationen, die systematisch gesammelt, gespeichert und analysiert werden können. In dieser Ausarbeitung wird untersucht, wie diese Daten, speziell aus sozialen Netzwerken, genutzt werden können, um Erkenntnisse zu gewinnen.

## Warum Social Media Analyse?

Gesellschaftliche Studien profitieren enorm von Social Media Analysen, da sie aktuelle Trends, Einstellungen und soziale Dynamiken in Echtzeit widerspiegeln können.

Ein weiteres Einsatzfeld ist die Vorhersage öffentlicher Meinungen oder wirtschaftlicher Entwicklungen, wie zum Beispiel Aktienkurse, basierend auf Online-Stimmungen.

Marktsentiment-Analysen ermöglichen es Unternehmen, die Haltung der Konsumenten zu Produkten oder Dienstleistungen besser zu verstehen.

Zusätzlich eröffnen sich viele weitere Anwendungsmöglichkeiten – von politischer Forschung bis hin zu Kulturwissenschaften.

## Methoden

Zur Datenerhebung wurde automatisiert auf die Bluesky API (AT Proto) zugegriffen, um große Mengen an Social Media Posts zu sammeln.

Die Speicherung dieser Daten erfolgte mithilfe von DuckDB, einer Datenbanklösung, die gut für große Datenmengen geeignet ist.

Für die schnelle Verarbeitung großer Datenmengen wurde erneut DuckDB verwendet, da sie sich für Big-Data-Anwendungen besonders anbietet.

Im nächsten Schritt wurden die Texte bereinigt. Hierbei kamen Techniken wie Stopword-Entfernung und Stemming (mit NLTK) zum Einsatz.

Es wurde außerdem untersucht, welche Wörter häufig gemeinsam auftreten, um Verbindungen zwischen Personen und Themen zu erkennen.

Zur besseren Darstellung der Ergebnisse wurde Plotly genutzt, ein Tool für interaktive Datenvisualisierung.

Geplant, aber noch nicht umgesetzt, ist die Extraktion von Sentimentwerten, die Bewertung von Ratings, sowie eine gewichtete Engagementanalyse.

## Info zur Verarbeitung

Der analysierte Datensatz umfasst einen Zeitraum von vier Monaten – vom 1. Januar bis zum 1. April.

Als Suchbegriff wurde ausschließlich „Trump“ verwendet, um relevante Posts aus den sozialen Medien zu sammeln.

Die Daten wurden in täglichen Intervallen erhoben, jeweils die Top 100 Posts eines Tages (z.B. 1.–2. Januar, 2.–3. Januar usw.).

## Ergebnisse

Wie erwartet, war „Trump“ das am häufigsten auftretende Wort im Datensatz.

Darauf folgten Namen wie „Donald“, „Musk“, „Putin“ und „Elon“, was auf häufige gemeinsame Erwähnungen hindeutet.

Ein bemerkenswerter Befund war, dass das einzige emotional oder beschreibend wirkende Wort im Datensatz „FUCK“ war – was der Stimmung rund um das Thema wohl treffend entspricht.

## Was ging gut?

Die API von Bluesky erwies sich als sehr hilfreich, da sie kostenlos und funktional gut einsetzbar ist.

DuckDB konnte durch seine Spezialisierung im Bereich Big Data und Data Science punkten.

Auch das Natural Language Toolkit (NLTK) ermöglichte eine effiziente Verarbeitung der Texte und half dabei, Struktur in den Datensatz zu bringen.

## Was ging nicht so gut?

Trotz moderner Dokumentation war das Einlesen der gescrapten Daten in die Datenbank nicht ganz trivial und erforderte einige Trial-and-Error-Versuche.

Das Schreiben der Ausarbeitung selbst war eine eher unangenehme Aufgabe – eine ehrliche, wenn auch subjektive Beobachtung.

