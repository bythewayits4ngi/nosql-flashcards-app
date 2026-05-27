
04.05.2026
- Thema ausgewählt (Lernkarten-App)
- MongoDB lokal installiert und MongoDB Compass zur Verwaltung eingerichtet
- Datenmodell entworfen (JSON-Struktur)
- Skript seed_Data.py erstellt, um 10 Beispieldatensätze aus einer ExampleCards.json in die Datenbank zu importieren

Probleme: Installation durch Rechtesystem erschwert -> Docker genutzt

aktueller Stand: Datenbank ist lokal installiert, erreichbar und mit 10 Test-Datensätzen gefüllt

KI-Nutzung: 
- Anleitung MongoDB und Fehleranalyse Installation
    -> Ergebnis hilfreich, aber nicht jeder Schritt der Anleitung konnte so umgesetzt werden, da unterschiedliche Ausgangssituationen vorlagen (deshalb Fehleranalyse)

05.05.2026
- FastAPI-Grundgerüst implementiert (api_main.py)
- Verbindung hergestellt (pymongo)
- CRUD-Endpunkte erstellt: 
    - GET (alle Karten anzeigen), 
    - POST (neue Karte erstellen), 
    - PUT (Karte updaten), 
    - DELETE (eine Karte löschen)

- zusätzliche Funktion: Filterfunktion für Level/Tags

Probleme: von MongoDB erzeugte Id -> String-Konvertierung 

aktueller Stand: API ist funktionsfähig (Swagger UI)

KI-Nutzung: 
- Anleitung/Übersicht Endpunkte mit FastAPI einrichten und Testen
    -> Ergebnis hilfsreich, aber Codebeispiele musste angepasst werden 

06.05.2026
- Client in Python entwickelt (nutzt requests für API-Aufrufe)
- Dokumentation fertiggestellt und Reflexionsfragen beantwortet

aktueller Stand: System läuft lokal

KI-Nutzung:
- main- und print_cards-Methode des Clients erstellen lassen 
    -> Ergebnis teilweise hilfreich, weil einige Fehler vorhanden, sodass Code noch angepasst werden musste


Reflexion: 

Wie sieht Ihr Datenmodell aus?
Wir nutzen eine Collection 'cards'. Jedes Dokument enthält eine eindeutige _id (generiert durch MongoDB), die Felder question (String), answer (String), category (String), level (Integer) und tags (Array von Strings).

Warum haben Sie sich für diese Struktur entschieden?
Wir haben uns für eine einfache Struktur entschieden, da die App hauptsächlich dazu dient, Lernkarten abzurufen und zu filtern. Sie ermöglicht schnelle Lesezugriffe ohne komplexe Joins. Außerdem haben wir die Möglichkeit, sollten wir in Zukunft weitere Typen wie Bilder oder Audios hinzufügen wollen, können wir dies ohne größeren Aufwand in der Datenbank tun.

Wo entstehen Redundanzen?
In unserem Modell entstehen Redundanzen durch die Verwendung von Textfeldern für Kategorien. Wenn z.B. mehrere Karten dieselbe Kategorie "Informatik" haben, wird dieser String in jedem Dokument gespeichert. 

Welche Probleme sind aufgetreten?
Ein Problem war die Serialisierung der von MongoDB erzeugten _id (ObjectId) für die REST-API, da FastAPI keine Objekttypen von MongoDB als JSON ausgeben kann. Ansonsten hatten wir hauptsächlich technische Probleme (z.B. Installationen von MongoDB, etc. durch Rechtesystem auf Arbeitsgeräten erschwert) und eine klare Aufgabenteilung zu finden. 

Was würden Sie beim nächsten Mal anders machen?
Wir würden für diese Projektgröße nicht erst GitHub einrichten, da es zu viel Zeit gekostet und z.B. dazu geführt hat, dass wir keine Zeit meht für die Fehlerbehandlung hatten. Außerdem hätten wir Aufgaben besser trennen sollen. Wir haben oft in den Aufgabenbereich der anderen hinein gearbeitet und damit für Verwirrung und fehlender Übersicht gesorgt. 

Wann wäre eine relationale Datenbank sinnvoller gewesen?
Eine relationale Datenbank wäre sinnvoller gewesen, wenn das Projekt mehr Beziehungen zwischen den Daten hätte.
Wir haben jetzt alles in eine einzige Liste (Collection) gepackt, was für die 10 Karten super funktioniert. Wenn wir aber ein System hätten, in dem viele verschiedene Benutzer ihre eigenen Lernkarten erstellen oder ihren Lernfortschritt festhalten wollten, würde man schnell den Überblick verlieren. Dafür könnte man dann besser eine relationale Datenbank verwenden, um die Informationen besser zu trennen (z.B. extra Tabelle für Kategorien) und so auch Fehler in den Daten selbst zu verhindern.