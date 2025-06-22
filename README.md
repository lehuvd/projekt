# Bildbearbeitungsprogramm

Ein einfaches grafisches Programm zur Bearbeitung von Bildern.  
Man kann ein Bild laden, es heller oder dunkler machen, die Sättigung ändern oder es horizontal spiegeln. Danach kann man das bearbeitete Bild speichern oder zum Original zurücksetzen.

## Funktionen

- Helligkeit ändern
- Sättigung ändern
- Horizontal spiegeln
- Vorschau der Bearbeitung
- Bild speichern
- Zurücksetzen auf das Original

## Funktionsweise

### Bildbearbeitung

- Helligkeit: Multiplikation aller Farbwerte mit einem Faktor (0.1–3.0).
- Sättigung: Umwandlung in HSV, Anpassung des Sättigungswertes (S), Rückumwandlung zu RGB.
- Spiegelung: Vertauschen der Spalten zur horizontalen Spiegelung.

### Technisch umgesetzt mit

- numpy: Array-Manipulation der Bilddaten
- matplotlib: Vorschauanzeige, Umrechnung zwischen RGB und HSV
- tkinter: Dialoge und grafische Oberfläche
- PIL (Pillow): Laden und Speichern von Bildern

## Voraussetzungen

- Python 3.x
- Abhängigkeiten installieren mit:

```bash
pip install numpy matplotlib pillow tkinter
```
- Oder einfach .exe, der mit PyInstaller kompiliert wurde.
  
```bash
pyinstaller --onefile --windowed ^ 
  --hidden-import=tkinter ^
  --hidden-import=PIL ^
  --hidden-import=numpy ^
  --hidden-import=matplotlib ^
  --hidden-import=matplotlib.colors ^
  --add-data "pfad\zum\bbp.py;." ^
  "pfad\zum\bbp.py"
```
### Erklärungen

- `--onefile`: erzeugt eine einzelne `.exe`-Datei  
- `--windowed`: unterdrückt das Konsolenfenster (ideal für GUI-Anwendungen)  
- `--hidden-import`: zwingt PyInstaller, wichtige Module einzubeziehen  
- `--add-data`: fügt zusätzliche Dateien oder Pfade zur EXE hinzu  

## Ausführen mit:

```bash
python bbp.py
```
Oder durch Doppelklick auf die erzeugte .exe. (nur Windows)
