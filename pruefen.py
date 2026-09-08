# -*- coding: utf-8 -*-
"""
Prueft, ob jede Datei aus bilder/manifest.json vorhanden und nicht leer ist.

Laeuft im Pages-Workflow vor dem Deployment und ist auch von Hand aufrufbar:

    python pruefen.py

Zweck: Ein fehlendes Bild fiele sonst erst in der fertigen Praesentation auf -
als leerer Bildrahmen, ohne Fehlermeldung, weil die Content-Security-Policy
eines Artifacts blockierte Bildquellen nicht meldet.
"""
import io
import json
import os
import sys

WURZEL = os.path.dirname(os.path.abspath(__file__))
MANIFEST = os.path.join(WURZEL, 'bilder', 'manifest.json')

if not os.path.isfile(MANIFEST):
    sys.exit('FEHLER: bilder/manifest.json fehlt.')

eintraege = json.load(io.open(MANIFEST, encoding='utf-8'))
fehler = []

for e in eintraege:
    pfad = os.path.join(WURZEL, 'bilder', e['datei'])
    if not os.path.isfile(pfad):
        fehler.append('fehlt:  bilder/%s  (Verweis [%s])' % (e['datei'], e['verweis']))
    elif os.path.getsize(pfad) == 0:
        fehler.append('leer:   bilder/%s  (Verweis [%s])' % (e['datei'], e['verweis']))

# Ueberzaehlige Dateien sind kein Fehler, aber ein Hinweis: sie werden von
# praesentation.md nicht referenziert und liegen ohne Grund oeffentlich.
bekannt = set(e['datei'] for e in eintraege) | {'manifest.json'}
vorhanden = set(os.listdir(os.path.join(WURZEL, 'bilder')))
ueberzaehlig = sorted(vorhanden - bekannt)

for f in fehler:
    print(f)
if ueberzaehlig:
    print('Hinweis: nicht im Manifest und deshalb unreferenziert: %s'
          % ', '.join(ueberzaehlig))

if fehler:
    sys.exit('\n%d Problem(e). Im Arbeitsrepository "python tools/link-assets.py" '
             'ausfuehren und erneut committen.' % len(fehler))

print('%d Dateien aus manifest.json vollstaendig vorhanden.' % len(eintraege))
