import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
from PIL import Image

def helligkeit_andern(bild, faktor):
    # Macht bild heller oder dunkler, einfach multiplizieren und abschneiden
    bild2 = bild * faktor
    for i in range(bild2.shape[0]):
        for j in range(bild2.shape[1]):
            for k in range(bild2.shape[2]):
                if bild2[i, j, k] > 1:
                    bild2[i, j, k] = 1
                if bild2[i, j, k] < 0:
                    bild2[i, j, k] = 0
    return bild2

def saettigung_andern(bild, faktor):
    # Macht bild bunter oder grauer, geht über hsv
    import matplotlib.colors as mcolors
    hsv = mcolors.rgb_to_hsv(bild)
    for i in range(hsv.shape[0]):
        for j in range(hsv.shape[1]):
            hsv[i, j, 1] = hsv[i, j, 1] * faktor
            if hsv[i, j, 1] > 1:
                hsv[i, j, 1] = 1
            if hsv[i, j, 1] < 0:
                hsv[i, j, 1] = 0
    rgb = mcolors.hsv_to_rgb(hsv)
    return rgb

def spiegeln(bild):
    # Dreht bild von links nach rechts
    h, w, c = bild.shape
    gespiegelt = np.zeros_like(bild)
    for i in range(h):
        for j in range(w):
            gespiegelt[i, j] = bild[i, w - 1 - j]
    return gespiegelt

def bild_laden_dialog():
    # Dateiauswahl öffnen
    root = tk.Tk()
    root.withdraw()
    pfad = filedialog.askopenfilename(
        title="Bild auswählen",
        filetypes=[("Bilder", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff")]
    )
    return pfad

def bild_als_array(pfad):
    # Bilddatei zu array machen
    bild = Image.open(pfad).convert("RGB")
    arr = np.array(bild).astype(np.float32) / 255.0
    return arr

def array_als_bild(arr):
    # Array zu bilddatei machen
    arr2 = arr * 255
    arr2[arr2 > 255] = 255
    arr2[arr2 < 0] = 0
    arr2 = arr2.astype(np.uint8)
    return Image.fromarray(arr2)

def bild_anzeigen(arr, titel="Vorschau"):
    # Zeigt bild mit matplotlib
    plt.figure()
    plt.imshow(arr)
    plt.title(titel)
    plt.axis('off')
    plt.show()

def faktor_abfragen(option):
    # Faktor abfragen
    root = tk.Tk()
    root.withdraw()
    if option == "helligkeit":
        faktor = simpledialog.askfloat(
            "Faktor",
            "Helligkeitsfaktor (0.1 bis 3.0):",
            minvalue=0.1, maxvalue=3.0)
    elif option == "saettigung":
        faktor = simpledialog.askfloat(
            "Faktor",
            "Saettigungsfaktor (0.0 bis 3.0):",
            minvalue=0.0, maxvalue=3.0)
    else:
        faktor = None
    return faktor

def bild_speichern(arr):
    # Bild speichern
    root = tk.Tk()
    root.withdraw()
    pfad = filedialog.asksaveasfilename(
        title="Bild speichern",
        defaultextension=".png",
        filetypes=[("PNG", "*.png"), ("JPEG", "*.jpg;*.jpeg"), ("BMP", "*.bmp")]
    )
    if pfad:
        array_als_bild(arr).save(pfad)
        messagebox.showinfo("Gespeichert", f"Bild gespeichert: {pfad}")

def main():
    pfad = bild_laden_dialog()
    if not pfad:
        print("Kein Bild ausgewählt.")
        return
    original = bild_als_array(pfad)
    bearbeitet = np.copy(original)

    root = tk.Tk()
    root.title("Bildbearbeitung")
    root.geometry("300x220")

    def aktion(option):
        nonlocal bearbeitet
        if option == "spiegeln":
            bearbeitet = spiegeln(bearbeitet)
            bild_anzeigen(bearbeitet, titel="Vorschau")
            aktionen_fenster()
            return
        faktor = faktor_abfragen(option)
        if faktor is None:
            auswahl_fenster()
            return
        if option == "helligkeit":
            bearbeitet = helligkeit_andern(bearbeitet, faktor)
        else:
            bearbeitet = saettigung_andern(bearbeitet, faktor)
        bild_anzeigen(bearbeitet, titel="Vorschau")
        aktionen_fenster()

    def speichern():
        bild_speichern(bearbeitet)
        root.quit()
        root.destroy()

    def reset():
        nonlocal bearbeitet
        bearbeitet = np.copy(original)
        bild_anzeigen(bearbeitet, titel="Zurückgesetzt")
        auswahl_fenster()

    def beenden():
        root.quit()
        root.destroy()

    def auswahl_fenster():
        for widget in root.winfo_children():
            widget.destroy()
        tk.Label(root, text="Wähle eine Funktion:").pack(pady=5)
        tk.Button(root, text="Helligkeit ändern", width=25, command=lambda: aktion("helligkeit")).pack(pady=2)
        tk.Button(root, text="Sättigung ändern", width=25, command=lambda: aktion("saettigung")).pack(pady=2)
        tk.Button(root, text="Bild spiegeln", width=25, command=lambda: aktion("spiegeln")).pack(pady=2)

    def aktionen_fenster():
        for widget in root.winfo_children():
            widget.destroy()
        tk.Label(root, text="Was möchtest du als nächstes tun?").pack(pady=5)
        tk.Button(root, text="Weiter bearbeiten", width=25, command=auswahl_fenster).pack(pady=2)
        tk.Button(root, text="Bild speichern", width=25, command=speichern).pack(pady=2)
        tk.Button(root, text="Zurücksetzen", width=25, command=reset).pack(pady=2)
        tk.Button(root, text="Beenden", width=25, command=beenden).pack(pady=2)

    auswahl_fenster()
    root.mainloop()

if __name__ == "__main__":
    main()
