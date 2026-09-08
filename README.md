# Bildassets — Kijimea Case Study

Dieses Verzeichnis ist ein **eigenständiges, öffentliches Repository**. Es liefert
über GitHub Pages die 14 Bilddateien aus, auf die `praesentation.md` per Link
verweist.

**Es enthält bewusst keine Case-Inhalte** — keine Aufgabenstellung, keine
Unternehmensanlagen, keine Analyse, keinen Präsentationstext. Nur Bilder. Das ist der
Grund, warum es getrennt vom Arbeitsrepository liegt: GitHub Pages setzt auf der
kostenlosen Stufe ein öffentliches Repository voraus, und das Arbeitsrepository
enthält Originalanlagen von Kijimea, die nicht öffentlich werden dürfen.

## Hinweis zu KI-erzeugten Inhalten

**Die vier Porträts und die acht Motivbilder in `bilder/` sind mit künstlicher
Intelligenz erzeugt.** Die abgebildeten Personen existieren nicht. Die Bilder zeigen
keine realen Kunden, keine Mitarbeitenden und keine echten Produktaufnahmen.

Nicht KI-erzeugt sind:

- `kijimea-logo.svg` — offizielle Wortmarke des Unternehmens, unverändert
- `markensuchvolumen-kijimea-de.svg` — selbst erstellte Grafik aus Google-Trends-Daten

## Inhalt

| Pfad | Inhalt |
| --- | --- |
| `bilder/` | Die 14 Bilddateien, erzeugt von `tools/link-assets.py` im Arbeitsrepository |
| `bilder/manifest.json` | Maschinenlesbares Manifest: Verweis, Datei, Alt-Text, Verwendung, KI-Kennzeichnung, Maße |
| `index.html` | Kontaktabzug zur Sichtprüfung — erscheint jedes Bild, sind alle Links erreichbar |
| `.github/workflows/pages.yml` | Deployment auf GitHub Pages |

`bilder/` und `index.html` werden **erzeugt, nicht von Hand gepflegt.** Quelle sind die
Originale in `ci/assets/` des Arbeitsrepositorys.

## Einrichtung

Einmalig, im Arbeitsrepository von dessen Wurzelverzeichnis aus:

```bash
# 1. Repository auf GitHub anlegen (öffentlich, Name z. B. kijimea-case-bilder)
gh repo create kijimea-case-bilder --public

# 2. Dieses Verzeichnis als Repository initialisieren und pushen
cd bild-repo
git init -b main
git add .
git commit -m "Bildassets der Kijimea Case Study"
git remote add origin https://github.com/thomasreinel/kijimea-case-bilder.git
git push -u origin main

# 3. Auf GitHub: Settings → Pages → Source: "GitHub Actions"
```

Danach liegen die Bilder unter:

```
https://thomasreinel.github.io/kijimea-case-bilder/bilder/<datei>
```

## Basis-URL im Arbeitsrepository — bereits eingetragen

In `tools/bild-basis-url.txt` steht
`https://thomasreinel.github.io/kijimea-case-bilder/bilder`, und die 14 Links in
`praesentation.md` sind damit erzeugt. Hier ist **nichts mehr zu tun**, solange sich
Nutzername oder Repository-Name nicht ändern.

Falls doch: die Adresse dort ändern und `python tools/link-assets.py` erneut
ausführen. Steht in der Datei der Platzhalter `NUTZERNAME`, schreibt das Skript eine
sichtbare Warnung in `praesentation.md` — die Datei ist dann **nicht
übergabefertig**.

## Nach einer Bildänderung

Im Arbeitsrepository `python tools/link-assets.py` ausführen, dann hier committen und
pushen. Die Dateinamen bleiben stabil, die Links in `praesentation.md` ändern sich
also nicht.

## Prüfung nach dem Deployment

`https://thomasreinel.github.io/kijimea-case-bilder/` im Browser öffnen. Erscheinen
alle 14 Bilder, sind alle Links in `praesentation.md` erreichbar. Fehlt eines, fehlt
es auch bei der Gestaltung.
